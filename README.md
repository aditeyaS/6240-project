# SysC: Linux System Monitor

![SysC](https://github.com/aditeyaS/6240-project/blob/main/img/icon.gif)

SysC (C = See) is a Linux System Monitor tool which is the final project for the course System Administration and Security (CPSC 6240)
## Tech Stack

**Languages:** Python, Bash

**Python Libraries:** psutil, colorama, Tkinter


## Installation

Clone the project
```bash
  git clone https://github.com/aditeyaS/6240-project
```

Go to the project directory
```bash
  cd 6240-project
```

Install linux requirements
```bash
  xargs sudo apt install < linux-requirements.txt
```

Install python requirements
```bash
  pip3 install -r pip-requirements.txt
```

Make script executable
```bash
  chmod u+x sysc.sh
```

## Run Locally

Run UI app
```bash
  ./sysc.sh
```

Run CLI app
```bash
  ./sysc.sh --cli
```

## Screenshot

UI App Screenshot
![UI App](https://github.com/aditeyaS/6240-project/blob/main/img/ui_scshot.png)

CLI App Screenshot
![CLI App](https://github.com/aditeyaS/6240-project/blob/main/img/cli_scshot.png)

## ToDo

UI App
- feature to kill a process

CLI App
- network monitor
- process monitor

## Authors

- [Aditeya Srivastava](https://www.github.com/aditeyaS)
- [David Fernandez](https://github.com/David-FR)
- [Sejal Bansal](https://www.github.com/)
- [Tarun Prathipati](https://www.github.com/)