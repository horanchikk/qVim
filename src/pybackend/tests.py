from multiprocessing import Process, freeze_support
from time import sleep
from sys import exit

def thread(value):
    while True:
        try:
            print(f'Thread {value}')
            sleep(1)
        except SystemExit:
            print('terminated')
            exit(0)


def main():
    for i in range(10):
        sleep(0.1)
        g = Process(target=thread, args=(str(i), ))
        g.daemon = True
        g.start()
    
    g.kill()
    print('terminate')

if __name__ == '__main__':
    freeze_support()
    main()