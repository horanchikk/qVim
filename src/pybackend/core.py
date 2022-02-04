# Exceptions can be: FileNotFoundError(config.json); IndexError(sys.argv); ImportError
import sys, json
import subprocess
import multiprocessing
import requests
import psutil
from webbrowser import open_new_tab
from time import sleep
from rich.console import Console

args = sys.argv[1]
server = json.load(open("out/config.json", "r"))
log = open("out/logs.qvim", "w")
console = Console()

def initThread(typeserver):
    match typeserver:
        case "flask":
            flaskserver = subprocess.call('python server.py', stdout=log, stdin=log, stderr=log, shell=True)
            print(flaskserver.stderr)
            while True:
                pass

        case "npm":
            npmserver = subprocess.call("cd .. & cd .. & yarn serve", stdout=log, stdin=log, stderr=log, shell=True)
            print(npmserver.stderr)
            while True:
                pass

g = multiprocessing.Process(target=initThread, args=("npm", ))
j = multiprocessing.Process(target=initThread, args=("flask", ))
g.daemon = True
j.daemon = True

def killall():
    g.kill()
    j.kill()

    for proc in psutil.process_iter():
        if proc.name() == 'node.exe':
            proc.kill()
        elif proc.name == 'node':
            proc.kill()


def serverInstall():
    pass

def serverRun():
    with console.status("[bold yellow] Server starting...\n", spinner="line") as status:
        g.start()
        j.start()
        try:
            serverreq = requests.get('http://localhost:5000').status_code
        except:
            serverreq = "404"

    if serverreq == 200:
        serverreq = "[bold green] 200"
        with console.status(f"[bold cyan] Status code: {serverreq}\n", spinner="line") as status:
            sleep(0.5)
    else:
        serverreq = "[bold red]" + serverreq
        with console.status(f"[bold white] Status code: {serverreq}\n", spinner="line") as status:
            sleep(2)
            raise ConnectionAbortedError('Lost connection to http://localhost:5000')

    open_new_tab('http://localhost:8080')

    with console.status("[bold green] Server has been started! Url: http://localhost:8080\n        For exit use: Ctrl+C\n", spinner="bouncingBar", refresh_per_second=7) as status:
        while True:
            sleep(10000)

def run():
    match args:
        case "runserver":
            serverRun()
        case "install":
            serverInstall()

if __name__ == "__main__":
    multiprocessing.freeze_support()
    try:
        run()
    except KeyboardInterrupt or SystemExit:
        killall()
        console.print('[red bold]qVim server has been stopped')
    except Exception as e:
        killall()
        print("\n" + str(e))
        console.print('[red bold]qVim server has been stopped')