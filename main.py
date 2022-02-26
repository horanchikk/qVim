from sys import path
from subprocess import call
from webbrowser import open_new_tab
from time import sleep
# Import from /py
path.insert(1, 'py/')
from tests import test # importing tests and launching it
test()
from server import flaskrun
from psutil import process_iter

def initThread(typeserver):
    match typeserver:
        case "flask":
            flaskrun()

        case "npm":
            call('yarn serve', shell=True)

def main():
    import multiprocessing
    g = multiprocessing.Process(target=initThread, args=("npm", ))
    j = multiprocessing.Process(target=initThread, args=("flask", ))
    g.daemon = True
    j.daemon = True
    g.start()
    j.start()
    while True:
        pass

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()