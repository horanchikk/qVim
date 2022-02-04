from subprocess import call

try:
    call('cd src/pybackend/ && python core.py runserver', shell=True)
except:
    pass