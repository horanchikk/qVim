import subprocess

subprocess.call('python py/update.py', shell=True)
subprocess.call('python py/server.py', shell=True)