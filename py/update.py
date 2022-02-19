try:
    import requests, bs4, flask, flask_cors, lxml
except:
    import subprocess
    subprocess.call('pip3 install requests bs4 flask flask-cors lxml', shell=True)