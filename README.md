
# AMC- Automatic Media Access Control [MAC] Address Spoofing Tool

[![info](https://badgen.net/badge/Project/Info/blue?icon=information)](https://github.com/hexdee606/AMC2.0#readme)
[![Open source](https://badgen.net/badge/Open%20Source%3F/Yes%20%21/blue)](#)
[![CC-0 license](https://img.shields.io/badge/License-CC--0-blue.svg)](https://github.com/hexdee606/AMC2.0/blob/main/LICENSE)
[![Python](https://badgen.net/badge/Made%20with/Python3/blue)](https://github.com/hexdee606/AMC2.0#readme)
[![status](https://badgen.net/badge/Status/Beta/yellow)](#)

## **About**

**AMC (Automatic Media Access Control [MAC] Address Spoofing tool), Helps you to protect your real network hardware identity. Each entered time interval your hardware address was changed automatically. without interrupting your internet connection.**

## Tested On 

 Sr. | Operating System | Version | Virtual Box | VM Ware | Network Type |
--- | --- | --- | --- | --- | --- |
1 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2021.2 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
2 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2021.1 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
3 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2020.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
4 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2019.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
5 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux</img > | 2018.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
6 | <img align="center" src="https://img.icons8.com/ios/25/000000/ubuntu.png">  Ubuntu</img > | 20.04 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
7 | <img align="center" src="https://img.icons8.com/ios-glyphs/25/000000/debian.png">  Debian</img > | 10.0 | [![status](https://badgen.net/github/status/micromatch/micromatch/f4809eb6df80b)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/f4809eb6df80b)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) | [![network](https://badgen.net/badge/Network/NAT/red)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
 
## **Features** 

1. Change MAC address without interrupting the internet.
2. Command Line Based Script.
3. Lightweight and easily handleable.


## **Required packages**
- git `required`
- Python3 `required`
- pip3 `optional`
- net-tools `required`
- network-manager `required`
- macchanger `required`
- pyinstaller `Optional`

## **User Type**
`User must be super user / root user.` 

## Install required packages
```console
 sudo apt update -y
```
```console
 sudo apt install git-all -y
```
```console
 sudo apt install net-tools -y
```
```console
 sudo apt install network-manager -y
```
```console
 sudo apt install -y macchanger
```

## Install optional packages
```console
 sudo apt update -y
```
```console
 sudo apt install python3-pip -y
```
```console
 pip install pyinstaller -y
```

## How to setup Automatic MAC Changer

>**Create new directory**
```console
 mkdir AMC
```
```console
 cd AMC
```

>**Clone AMC from GitHub**
```console
 git clone "https://github.com/hexdee606/AMC2.0.git"
```

>**Method 1 : By using `chmod`**
```console

 cd AMC2.0
```

```console
 sudo chmod +x *
```
```console
 python3 amc.py -h
```

>**Method 2 : By creating an `executable` file**
```console 

 cd AMC
```
```console
 cd AMC2.0
```
```console
 pyinstaller --onefile amc.py
```
```console
 cd dist
```
```console
 ./amc -h
```


>**Available options**
 
    [-h]    Help menu 
    
    -a/--about	: About Alchemists.
    
    -i/--interface	: Network interface name.
    
    -j/--join	: Join Alchemists.
    
    -l/--license	: AMC License.
    
    -n/--network	: Available network interface.
    
    -t/--time	: Time in seconds.
    
    -v/--version	: Version information.


>**Whenever you want to use AMC follow these steps.**


>**Example**
```console
 python3 amc.py  -i eth0 -t 30
```


## Troubleshooting methods if the internet is not working.

>If unable to access internet/ connection not established then do the following step (`after using AMC`): 
```console
 macchanger -p eth0 (Your Network interface)
```

>If AMC is not working then do the following process:
```console
default: managed=false
To change: managed=true
```

## Connect Us

[![twitter](https://badgen.net/badge/icon/hexdee606?icon=twitter&label)](https://twitter.com/hexdee606)
[![github](https://badgen.net/badge/icon/hexdee606?icon=github&label)](https://github.com/hexdee606)
[![email](https://badgen.net/badge/email/hexdee606/blue)](mailto:hexdee606@gmail.com)
[![twitter](https://badgen.net/badge/icon/Paradox_044?icon=twitter&label)](https://twitter.com/Paradox_044)
[![github](https://badgen.net/badge/icon/Paradox44?icon=github&label)](https://github.com/Paradox44)
[![email](https://badgen.net/badge/email/paradoxhex44/blue)](mailto:paradoxhex44@gmail.com)
[![twitter](https://badgen.net/badge/icon/itachi_9197?icon=twitter&label)](https://twitter.com/itachi_9197)
[![github](https://badgen.net/badge/icon/Itachi-91?icon=github&label)](https://github.com/Itachi-91)
[![email](https://badgen.net/badge/email/itachiuchiha9197/blue)](mailto:itachiuchiha9197@gmail.com)


>We hope you like our project. If 'Yes' click on the star icon at the top right corner or leave a comment so we can improve this script.

:heart: from Alchemists.
