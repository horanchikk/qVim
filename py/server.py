import requests
from subprocess import call, check_output
from sys import exit, platform
from time import sleep
from bs4 import BeautifulSoup as bs
from flask import Flask, request, jsonify
from flask_cors import CORS
from requests import get
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'
with open('out/config.log', 'w') as devlogfile:
    devlogfile.write('Waiting...')

def traceback(err):
    sleep(5)
    with open('out/config.log', 'w') as dev:
        dev.write(err)


def cmd(msg):
    with open('out/config.log', 'w') as dev:
        dev.write(f'Executed {msg}')
    sleep(0.4)
    with open('out/config.log', 'w') as devlogfile:
        # result = call(msg, stdout=devlogfile, shell=True)
        result = call(msg, shell=True)
        match result:
            case 1:
                devlogfile.write('Exception: command not found! Install Neovim and try again!')
                return False
            case 0:
                devlogfile.write('Waiting...')
                return True


@app.route("/", methods=["GET"])
def mainpage():
    return "", 200


@app.route("/config/set", methods=["GET"])
def configSet():
    PATH = request.args.get('path')
    with open("out/config.json") as file:
        config = json.load(file)
        return jsonify(config), 200

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
            texts.append({'name': fixname, 'description': fixdesc, 'link': link})
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
    with open('out/config.log', 'w') as log:
        log.write(f'Installing {res}...')
    sleep(2)
    cmd(f"""nvim --headless +"Plug '{link}'" +PlugInstall +qall""")
    return 'ok', 200


@app.route("/mginstall", methods=["GET"])
def mginstall():
    PATH = check_output("""nvim --headless +"echo stdpath('config')" +qall""", shell=True).decode("utf-8")
    with open(PATH, "wb") as file:
        res = get("https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim")
        file.write(res.content)
    return 'ok', 200

@app.route("/config/get", methods=["GET"])
def config():
    with open('out/config.json') as file:
        pass
    return 'ok'

@app.route("/plugupdate", methods=["GET"])
def plugupdate():
    cmd('nvim --headless +PlugUpdate +qall')
    return 'ok', 200


@app.route("/log", methods=["GET"])
def logging():
    sleep(0.1)
    try:
        devlogrd = open('out/config.log', 'r').readlines()[-1]
        return devlogrd, 200
    except:
        return "", 200

@app.route("/launch", methods=["GET"])
def launch():
    sleep(1)
    match platform: 
        case 'win32':
            cmd("start nvim")
    return "ok", 200

@app.route("/upgradevim", methods=["GET"])
def upgradevim():
    cmd('nvim --headless +PlugUpgrade +qall')
    return 'ok', 200

@app.route("/stop", methods=["GET"])
def stop():
    exit(0)
    return 0

if __name__ == "__main__":
    app.run(debug=False, port=5005)
