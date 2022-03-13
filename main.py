from sys import path
path.insert(1, 'py/')
from tests import test, serverstats
from sys import platform
from time import sleep
from webbrowser import open_new_tab
from subprocess import PIPE, call
import multiprocessing
from psutil import process_iter


# Import from /py


if platform == 'win32':
    python = 'python'
    pip = 'pip'
else:
    python = 'python3.10'
    pip = 'pip3.10'

log = open('out/server.log', 'w')


def initThread(typeserver):
    match typeserver:
        case "flask":
            call(f'{python} py/server.py', stdout=PIPE,
                 stderr=log, stdin=log, shell=True)
            while True:
                pass

        case "npm":
            call("yarn serve", shell=True)
            while True:
                pass


g = multiprocessing.Process(target=initThread, args=("npm", ))
j = multiprocessing.Process(target=initThread, args=("flask", ))
g.daemon = True
j.daemon = True


def server(args):
    match args:
        case 'kill':
            g.kill()
            j.kill()
            
            for proc in process_iter():
                if proc.name() == 'node.exe':
                    proc.kill()
                elif proc.name == 'node':
                    proc.kill()
        case 'run':
            g.start()
            j.start()
            serverstats()
            sleep(2)
            open_new_tab('http://localhost:8080')
            while True:
                sleep(10000)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    try:
        test()
        server('run')
    except KeyboardInterrupt or SystemExit:
        server('kill')
        print('\nqVim server has been stopped')
    except Exception as e:
        server('kill')
        print("\n" + str(e))
        print('\nqVim server has been stopped')
