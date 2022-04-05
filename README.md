# Welcome to qVim!

qVim - it is vim plugin manager with graphic interface. Here you can find some plugins and qVim install it to your favorite text editor automatically.

## Why qVim?

- This is more convenient than using the default terminal
- It is using vim-plug technology
- You can manage your plugins
- You can load your favorite config and qVim can working with it
- Store of configs for vim in one utility
- And many functions for easiest plugin management...

## Requirements

- Python 3.10 or later
- Node.JS 16.14.X

# First launch

## Linux users

Auto install:

```sh
sudo apt-get update && curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash - && sudo apt-get install nodejs software-properties-common -y && sudo add-apt-repository ppa:deadsnakes/ppa -y && sudo apt install python3.10 python3.10-distutils -y && pip3.10 install -r requirements.txt && sudo npm install --global yarn && yarn && python3.10 main.py
```

If you use WSL, add this in /etc/wsl.conf:

```conf
[interop]
appendWindowsPath = false
```

and execute shell command again.

## Windows users

Please make sure that nVim or Vim added in PATH

---

Install all dependencies:

```sh
pip install -r requirements.txt
npm install --global yarn
yarn
```

And execute main.py script using:

```sh
python main.py
```

## About developing

Our product is currently under development, so some functions may not be working. Please, wait, when product has been released. If you have any suggestions for improving the product or you have found a bug, please contact us: horandev.service@gmail.com.

## Nightly updates

It's here: https://github.com/horanDEV/qVim/tree/dev
