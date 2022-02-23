import requests
import subprocess
import sys
from time import sleep
from bs4 import BeautifulSoup as bs
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'

def traceback(err):
    return '[{"name": "Traceback", "descs": "' + str(err) + '"}]'

def cmd(msg):
    devlogfile = open('out/config.log', 'w')
    subprocess.call(msg, stdout=devlogfile, shell=True)
    devlogfile.write('Waiting...')

@app.route("/", methods=["GET"])
def mainpage():
    return "", 200

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
    links = soup.select(".px-3 > .d-flex > .d-flex > .f3 > .text-bold", href=True)
    
    try:
        for i in range(len(names)):
            namereq = names[i].decode_contents()
            fixname = namereq.replace("\n","").replace(" ","")
            descreq = descs[i].text
            fixdesc = descreq.replace("\n", "")
            link = "https://github.com" + str(links[i]['href'])
            texts.append({'name':fixname, 'description':fixdesc, 'link':link})
    except Exception as e:
        print(app.logger.warn(e))

    response = jsonify(texts)
    
    match texts:
        case []:
            return "", 400
    return response

@app.route("/install", methods=["GET"])
def install():
    link = request.args.get('link')
    print(link)
    sleep(1)
    cmd(f'curl {link}')
    return 'ok', 200

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
    sys.exit(0)

if __name__ == "__main__":
    app.run(debug=True, port=5000)