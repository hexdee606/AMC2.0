# AMC- Automatic Media Access Control [MAC] Address Spoofing Tool

[![banner](https://github.com/hexdee606/AMC2.0/blob/main/User/Banner.png)](#)

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
1 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux | 2021.2 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
2 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux | 2021.1 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
3 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux | 2020.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
4 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux | 2019.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
5 | <img align="center" src="https://img.icons8.com/color/25/000000/kali-linux.png"> Kali Linux | 2018.4 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
6 | <img align="center" src="https://img.icons8.com/ios/25/000000/ubuntu.png">  Ubuntu | 20.04 | [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/4.0.1)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![network](https://badgen.net/badge/Network/NAT/brown)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
7 | <img align="center" src="https://img.icons8.com/ios-glyphs/25/000000/debian.png">  Debian | 10.0 | [![status](https://badgen.net/github/status/micromatch/micromatch/f4809eb6df80b)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on)| [![status](https://badgen.net/github/status/micromatch/micromatch/f4809eb6df80b)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) | [![network](https://badgen.net/badge/Network/NAT/red)](https://github.com/hexdee606/AMC2.0/blob/main/README.md#tested-on) |
 
## **Features** 

1. Lightweight and multiple methods for use.
2. User-friendly and easily understandable for new users.
3. Automatically change network hardware address without losing internet connectivity.
4. User-friendly command-line-based user interface.


## **User Type**
`User must be super user / root user.`


## **Required packages**
- net-tools `required`
- network-manager `required`
- macchanger `required`
- pyinstaller `Optional`

## Process of installation

### Update your Debian based Linux

```console
sudo apt-get clean -y
```

```console
sudo apt-get update -y
```

### Create new directory

```console
mkdir 'AMC20' && cd 'AMC20'
```

### Let's Clone AMC-2.0 from GitHub

```console
git clone "https://github.com/hexdee606/AMC2.0.git"
```

### Install required packages

> #### Method 1: `Automatically`

```console
sudo pip3 install requirement.txt
```

> #### Method 2: `Manually`

```console
sudo apt-get install net-tools -y
```

```console
sudo apt-get install network-manager -y
```

```console
sudo apt-get install macchanger -y
```

```console
sudo pip3 install pyinstaller -y
```

## First-time Run AMC-2.0

> #### Method 1: Using `python3`

```console
 sudo python3 amc.py -h
```

> #### Method 2 : Using `shell script`

```console
sudo chmod +x amc.sh
```

```console
sh ./amc.sh
```

> #### Method 3 : Using `desktop file`

```console
sudo chmod +x amc.sh
```

```console
sudo chmod +x run-amc.desktop
```

```
Double click on run-amc.desktop
```

> #### Method 4 : By creating an `executable` file

```console
pyinstaller --onefile amc.py
```
```console
cd dist
```
```console
./amc -h
```


> #### Available options
 
    [-h]    Help menu 
    
    -a/--about	: About Alchemists.
    
    -i/--interface	: Network interface name.
    
    -j/--join	: Join Alchemists.
    
    -l/--license	: AMC License.
    
    -n/--network	: Available network interface.
    
    -t/--time	: Time in seconds.
    
    -v/--version	: Version information.


## Troubleshooting methods:

> #### If unable to access internet/ connection not established then do the following step (`after using AMC`): 

```console
macchanger -p {Network Interface}
```

> #### If AMC is not working then do the following process:

```console
sudo nano /etc/NetworkManager/NetworkManager.conf
```

```console
default: managed=false
To change: managed=true
```

## Connect Us

### <img src="https://img.icons8.com/color/15/000000/developer--v2.png"/> Research and Development

[![twitter](https://badgen.net/badge/icon/hexdee606?icon=twitter&label)](https://twitter.com/hexdee606)
[![github](https://badgen.net/badge/icon/hexdee606?icon=github&label)](https://github.com/hexdee606)
[![email](https://badgen.net/badge/email/hexdee606/blue)](mailto:hexdee606@gmail.com)

### <img src="https://img.icons8.com/color-glass/15/000000/test-partial-passed.png"/> Research and Testing

[![twitter](https://badgen.net/badge/icon/itachi_9197?icon=twitter&label)](https://twitter.com/itachi_9197)
[![github](https://badgen.net/badge/icon/Itachi-91?icon=github&label)](https://github.com/Itachi-91)
[![email](https://badgen.net/badge/email/itachiuchiha9197/blue)](mailto:itachiuchiha9197@gmail.com)
[![twitter](https://badgen.net/badge/icon/athena_077?icon=twitter&label)](https://twitter.com/athena_077)
[![github](https://badgen.net/badge/icon/athena-077?icon=github&label)](https://github.com/athena-077)
[![email](https://badgen.net/badge/email/athena74047/blue)](mailto:athena74047@gmail.com)
[![twitter](https://badgen.net/badge/icon/Paradox_044?icon=twitter&label)](https://twitter.com/Paradox_044)
[![github](https://badgen.net/badge/icon/Paradox44?icon=github&label)](https://github.com/Paradox44)
[![email](https://badgen.net/badge/email/paradoxhex44/blue)](mailto:paradoxhex44@gmail.com)

> ###### We hope you like our project. If 'Yes' click on the star icon at the top right corner or leave a comment so we can improve this script.

<p>&hearts; from Alchemists.</p>
