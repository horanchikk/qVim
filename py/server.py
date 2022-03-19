import requests
from subprocess import call
from sys import exit, platform
from time import sleep
from bs4 import BeautifulSoup as bs
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
with open('out/config.log', 'w') as devlogfile:
    devlogfile.write('Waiting...')

def traceback(err):
    return '[{"name": "Traceback", "descs": "' + str(err) + '"}]'


def cmd(msg):
    with open('out/config.log', 'w') as dev:
        dev.write(f'Executed {msg}')
    sleep(0.4)
    with open('out/config.log', 'w') as devlogfile:
        # result = call(msg, stdout=devlogfile, shell=True)
        result = call(msg, shell=True)
        match result:
            case 1:
                devlogfile.write('Exception: command not found!')
                return False
            case 0:
                devlogfile.write('Waiting...')
                return True


@app.route("/", methods=["GET"])
def mainpage():
    return "", 200


@app.route("/vimcheck", methods=["GET"])
def vimcheck():
    match cmd('nvim --headless +qall'):
        case False:
            match cmd('vim --headless +qall'):
                case False:
                    return jsonify(editor='none')
                case True:
                    return jsonify(editor='vim')
        case True:
            return jsonify(editor='nvim')


@app.route("/topics", methods=["GET"])
def topics():
    page = request.args.get('page')
    url = f"https://github.com/topics/vim-plugins?page={page}"
    texts = []

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return traceback("Check your internet connection!")
    except requests.exceptions.ConnectTimeout:
        return traceback("Server is not working. Please choose another server in 'Settings'")

    response = requests.get(url)

    soup = bs(response.text, 'lxml')

    names = soup.select(".px-3 > .d-flex > .d-flex > .f3 > .text-bold")
    descs = soup.select(".color-bg-default > .px-3 > div")
    links = soup.select(
        ".px-3 > .d-flex > .d-flex > .f3 > .text-bold", href=True)

    try:
        for i in range(len(names)):
            namereq = names[i].decode_contents()
            fixname = namereq.replace("\n", "").replace(" ", "")
            descreq = descs[i].text
            fixdesc = descreq.replace("\n", "")
            link = str(links[i]['href'])
            texts.append(
                {'name': fixname, 'description': fixdesc, 'link': link})
    except Exception as e:
        print(app.logger.warn(e))

    response = jsonify(texts)

    match texts:
        case []:
            return "", 400
    return response


@app.route("/pluginstall", methods=["GET"])
def pluginstall():
    res = request.args.get('link')
    link = res[1:]
    print(f'\n{link}')
    sleep(1)
    match platform:
        case 'win32':
            with open('out/config.log', 'w') as log:
                log.write(f'Installing {res}...')
            sleep(1.2)
            if cmd(f""" "C:/Program Files/Neovim/bin/nvim.exe" --headless +"Plug '{link}'" +PlugInstall +qall """) == True:
                return 'ok', 200
            else:
                return '', 404
            
        case 'linux':
            cmd(f"""nvim --headless +"Plug '{link}'" +PlugInstall +qall""")
            return 'ok', 200
        case 'darwin':
            return 'Mac OS systems is not supported!', 404


@app.route("/mginstall", methods=["GET"])
def mginstall():
    match platform:
        case 'win32':
            cmd('powershell ./scripts/install.ps1')
            return 'ok', 200
        case 'linux':
            pass
        case 'darwin':
            return 'Mac OS systems is not supported!'


@app.route("/plugupdate", methods=["GET"])
def plugupdate():
    match platform:
        case 'win32':
            cmd(
                """ "C:/Program Files/Neovim/bin/nvim.exe" --headless +PlugUpdate +qall """
            )
            return 'ok', 200
        case 'linux':
            cmd('nvim --headless +PlugUpdate +qall')
            return 'ok', 200
        case 'darwin':
            return 'Mac OS systems is not supported!', 404


@app.route("/log", methods=["GET"])
def logging():
    sleep(0.1)
    try:
        devlogrd = open('out/config.log', 'r').readlines()[-1]
        return devlogrd, 200
    except:
        return "", 200


@app.route("/stop", methods=["GET"])
def stop():
    exit(0)
    return 0


if __name__ == "__main__":
    app.run(debug=False, port=5000)
