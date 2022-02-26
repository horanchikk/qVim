import json, multiprocessing, requests, psutil
from webbrowser import open_new_tab
from time import sleep
from rich.console import Console
from subprocess import call, PIPE
from time import sleep

server = json.load(open("out/config.json", "r"))
log = open("out/logme.log", "w")
console = Console()    

def initThread(typeserver):
    match typeserver:
        case "flask":
            flaskserver = call('python py/server.py', shell=True, stdout=PIPE, stderr=log, stdin=log)
            print(flaskserver.stderr)
            while True:
                pass

        case "npm":
            npmserver = call("yarn serve", stdout=log, stdin=log, stderr=log, shell=True)
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


def serverRun():
    with console.status("[bold yellow] Server starting...\n", spinner="line"):
        g.start()
        j.start()
        try:
            serverreq = requests.get('http://localhost:5000').status_code
        except:
            serverreq = "404"

    if serverreq == 200:
        serverreq = "[bold green] 200"
        with console.status(f"[bold cyan] Status code: {serverreq}\n", spinner="line"):
            sleep(0.5)
    else:
        serverreq = "[bold red]" + serverreq
        with console.status(f"[bold white] Status code: {serverreq}\n", spinner="line"):
            sleep(5)
        with console.status(f"[bold white] Attempt 2...\n", spinner="line"):
            sleep(2)
            try:
                serverreq = requests.get('http://127.0.0.1:5000').status_code
            except:
                serverreq = "404"

            if serverreq == 200:
                    sleep(0.5)
            else:
                serverreq = "[bold red]" + serverreq
                sleep(2)
                raise ConnectionAbortedError('Lost connection to http://localhost:5000')

    open_new_tab('http://localhost:8080')

    with console.status("[bold green] Server has been started! Url: http://localhost:8080\n        For exit use: Ctrl+C\n", spinner="bouncingBar", refresh_per_second=7) :
        while True:
            sleep(10000)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    try:
        serverRun()
    except KeyboardInterrupt or SystemExit:
        killall()
        console.print('[red bold]qVim server has been stopped')
    except Exception as e:
        killall()
        print("\n" + str(e))
        console.print('[red bold]qVim server has been stopped')