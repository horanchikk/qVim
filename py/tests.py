from sys import platform
from os import system as shell
from requests import get
from time import sleep

if platform == 'win32':
    python = 'python '
    pip = 'pip '
else:
    python = 'python3.10 '
    pip = 'pip3.10 '

def pyver():
    testme = 'ok'
    try:
        match testme:
            case 'ok':
                print('pyver is ok')
                return True
    except SyntaxError:
        raise PermissionError('Your python version is not supported!')

def pkgs():
    try:
        import requests, bs4, flask, lxml, psutil, flask_cors
        print('pkgs is ok')
    except ImportError as e:
        shell(f'{pip}install -r requirements.txt')
        # shell(f'{python} main.py')

def serverstats():
    try:
        serverreq = get('http://localhost:5000').status_code
    except:
        serverreq = "404"

    if serverreq != 200:
        sleep(5)
        try:
            serverreq = get('http://127.0.0.1:5000').status_code
        except:
            serverreq = "404"
        if serverreq != 200:
            sleep(2)
            raise ConnectionAbortedError(f'Lost connection to http://localhost:5000. Status code: {serverreq}')

def test():
    pyver()
    pkgs()