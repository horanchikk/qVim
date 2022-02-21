from subprocess import call, PIPE
from threading import Thread
from time import sleep

def flaskserver():
    call('python py/update.py', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    sleep(2)
    call('python py/server.py', shell=True)

def nodeserver():
    sleep(2)
    call('yarn', shell=True, stdout=PIPE, stderr=PIPE, stdin=PIPE)
    call('yarn serve', shell=True)

a = Thread(target=flaskserver)
b = Thread(target=nodeserver)

def main():    
    a.start()
    b.start()
    b.join()
    a.join()

if __name__ == "__main__":
    main()
