#!/usr/bin/python3
"""
#############################################################################
#       Automatic Media Access Control [MAC] Address Spoofig Tool           #
#############################################################################
# Copyright 2021 Team Alchemists                                            #
#############################################################################
# Automatic Media Access Control [MAC] Address Spoofig Tool (c) 2021,       #
# This work is marked with CC0 1.0 Universal.                               #
# To view a copy of this license, visit                                     #
#                                                                           #
# http://creativecommons.org/publicdomain/zero/1.0                          #
#                                                                           #
# Unless required by applicable law or agreed to in writing, software       #
# distributed under the License is distributed on an "AS IS" BASIS,         #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
# See the License for the specific language governing permissions and       #
# limitations under the License.                                            #
#############################################################################
#                           ABOUT TEAM ALCHEMISTS                           #
#############################################################################
# Research & Developer  :   Dipen Chavan                                    #
# Research & Testing    :   Aniket Kumbhar, Ankita Hendre, Shreyas Kulkarni #
# Guide                 :   Anshul Tayal                                    #
#############################################################################
# this script is written in Python3 using PyCharm Community Edition 2021    #
# for Linux operating system. We hope you enjoy our work.                   #
# This software program is written for educational purposes only if you     #
# received any legal notice from cyber cell/ police then we will not        #
# responsible for that. use this script for your own risk.                  #
#############################################################################
"""
# Importing some important libraries
import argparse
import socket
import sys
import subprocess
from os import system, name, popen
from time import sleep

amc_project_version = '2.0.0.4'
amc_project_build = 'BETA-KALI_LINUX_2021.3-16102021PM0643'
amc_project_license = 'CC0 1.0 Universal'
amc_project_ide_name = 'PyCharm (Community Edition)'
amc_project_ide_version = '11.0.12+7-b1504.28 amd64'
amc_project_programming_language = 'Python3'
amc_project_programming_language_version = '3.9'


def clear():
    """
    :return: this function helps to clear terminal window.
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_error(error_code, error_message, critical_error):
    """
    This function is use to display error message.
    :param error_code: Short error code define by developer to identify error.
    :param error_message: Exception received by function.
    :param critical_error: is boolean if True exit from AMC.
    :return:
    """
    try:
        clear()
        print("######################################################################")
        print("# ERROR : {:<58} #".format(error_code))
        print("######################################################################")
        print("#                         ERROR MESSAGE                              #")
        print("######################################################################")
        print("# {:<66} #".format(str(error_message)))
        print("######################################################################")
        if critical_error:
            sys.exit()
    except Exception as display_errors:
        clear()
        print("######################################################################")
        print("# ERROR : {:<58} #".format("CE0000X0001"))
        print("######################################################################")
        print("#                         ERROR MESSAGE                              #")
        print("######################################################################")
        print("# {:<66} #".format(str(display_errors)))
        print("######################################################################")
        sys.exit()


try:
    """
    Command line colour options
    """
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white
except Exception as no_colour_error:
    G = Y = B = R = W = ''


def banner():
    """
    Fancy and attractive graphical banner for AMC
    :return: Nothing
    """
    print("%s######################################################################" % W)
    print("%s#                   _/_/        _/      _/        _/_/_/             #" % R)
    print("%s#                _/    _/      _/_/  _/_/      _/                    #" % G)
    print("%s#               _/_/_/_/      _/  _/  _/      _/                     #" % Y)
    print("%s#              _/    _/      _/      _/      _/                      #" % B)
    print("%s#             _/    _/      _/      _/        _/_/_/                 #" % W)
    print("%s#                                                                    #" % W)
    print("%s#             Coded  by Dipen   Chavan   - @hexdee606                #" % G)
    print("%s#             Tested by Aniket  Kumbhar  - @itachi-91                #" % B)
    print("%s#             Tested by Ankita  Hendre   - @athena-077               #" % R)
    print("%s#             Tested by Shreyas Kulkarni - @paradox44                #" % Y)


def welcome_message():
    """
    welcome message: display common welcome message after every cleaning of command line.
    :return: nothing
    """
    clear()
    banner()
    print("%s######################################################################" % W)
    print("%s#     Automatic Media Access Control [MAC] Address Spoofig Tool      #" % G)
    print("%s######################################################################" % W)
    print("%s# {:<20} | {:<43} #".format("Version", amc_project_version) % Y)
    print("%s# {:<20} | {:<43} #".format("Build", amc_project_build) % Y)
    print("%s######################################################################" % W)
    print("%s# Information: This script helps you to change your MAC              #" % B)
    print("%s# Address automatically to spoof your Original MAC Address           #" % B)
    print("%s######################################################################" % W)
    print("%s# Warning: If you receive any legal warrant from cyber               #" % R)
    print("%s# Branch then we are not responsible for this.                       #" % R)
    print("%s######################################################################" % W)
    print("%s# Made for Educational purpose only.                                 #" % Y)
    print("%s######################################################################" % W)


def reset_mac(network_interface):
    """
    This function is use to reset mac address to there original one.
    :param network_interface: network interface name Ex. eth0, wlan0
    :return: Nothing
    """
    try:
        clear()
        welcome_message()
        print("# Please wait...                                                     #")
        subprocess.call(["service", "NetworkManager", "stop"], shell=False)
        subprocess.call(["ifconfig", network_interface, "down"], shell=False)
        print("# Flushing default MAC Address...                                    #")
        command_line_process(f"macchanger -p {network_interface}", network_interface)
        print("# Resetting network manager...                                       #")
        subprocess.call(["ifconfig", network_interface, "up"], shell=False)
        subprocess.call(["service", "NetworkManager", "start"], shell=False)
        print("# Connecting to Internet...                                          #")
        print("######################################################################")
        sleep(2)
    except Exception as reset_mac_error:
        display_error('RM0000X0001', reset_mac_error, True)


def exit_msg(network_interface):
    """
    To display exit message
    :return: Nothing
    """
    try:
        reset_mac(network_interface)
        clear()
        welcome_message()
        print("# We hope you like Automatic MAC Address Changer.                    #")
        print("# If you have any suggestion please comment us on Github. Bye !      #")
        print("######################################################################")
        print("# Made and loved by Alchemists Open Source Community.                #")
        print("######################################################################")
        sys.exit()
    except Exception as exit_error:
        display_error('EE0000X0001', exit_error, False)


def command_line_process(command, network_interface):
    """
    This function read command line outputs.
    :param command: any terminal based command.
    :return: command line strings.
    """
    try:
        network_interface = network_interface
        command = command.split()
        p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, b''):
            # print(f'#{line.decode("utf-8").strip()}#')
            print("# {:<66} #".format(line.decode('UTF-8').strip()))
        sleep(0.1)
    except Exception as command_line_process_error:
        display_error('CLPE00X0001', command_line_process_error, False)
    except KeyboardInterrupt:
        exit_msg(network_interface)


def flash_new_mac(network_interface):
    """
    This function will flash new mac address to network_interface
    :param network_interface: network hardware (interface)
    :return: nothing
    """
    try:
        clear()
        welcome_message()
        print("# Please wait, do not close or cancel this process...                #")
        print("# Turning off network manager service...                             #")
        subprocess.call(["service", "NetworkManager", "stop"], shell=False)
        print("# Turning off {:<10}                                             #".format(network_interface + "..."))
        subprocess.call(["ifconfig", network_interface, "down"], shell=False)
        print("# Flashing new MAC address...                                        #")
        command_line_process(f"macchanger -a {network_interface}", network_interface)
        print("# Turning on {:<10}                                              #".format(network_interface + "..."))
        subprocess.call(["ifconfig", network_interface, "up"], shell=False)
        print("# Turning on network manager service...                              #")
        subprocess.call(["service", "NetworkManager", "start"], shell=False)
        print("######################################################################")
        print("# MAC address for {:<32}                   #".format(network_interface + " successfully changed."))
        print("######################################################################")
        print("# Please wait, reconnecting to network communication...              #")
        print("######################################################################")
        sleep(0.5)
    except Exception as flash_new_mac_error:
        display_error('CLPE00X0001', flash_new_mac_error, True)
    except KeyboardInterrupt:
        exit_msg(network_interface)


def display_network_interface():
    """
    To display all available network interface.
    :return: nothing
    """
    clear()
    welcome_message()

    print("# Sr. Number |   Network Interface Name  |   MAC Address             #")
    print("######################################################################")
    list_of_network_interface = socket.if_nameindex()
    read_mac_address = []
    for index, network_interface in list_of_network_interface:
        read_mac_address.append(popen("cat /sys/class/net/{}/address".format(network_interface)).read().split("\n"))
    list_of_mac_address = [i[0] for i in read_mac_address]

    for (index, network_interface), mac_address in zip(list_of_network_interface, list_of_mac_address):
        print("# {:<10} | {:<25} | {:<25} #".format(index, network_interface, mac_address))
    print("######################################################################")
    sys.exit()


def check_network_interface(network_interface):
    """
    check available interface
    :param network_interface: network hardware (interface).
    :return: if network interface available return True.
    """
    try:
        for index, interface in socket.if_nameindex():
            if network_interface == interface:
                return True
    except Exception as check_network_interface_error:
        display_error('CNI000X0001', check_network_interface_error, True)


def check_change_time(change_time):
    """
    to check timeout time is between 25 to 60 or not.
    :param change_time: int value input given by user
    :return: if time is between 25 to 60 return True
    """
    try:
        if int(change_time) < 25:
            clear()
            welcome_message()
            print("%s# Yes ! privacy is important. but change MAC address to often,       #" % G)
            print("%s# it will damage your Network Manager Service.                       #" % G)
            print("%s# Please enter time between 25 sec to 60 sec.                        #" % G)
            print("%s######################################################################" % W)
            sys.exit()
        elif int(change_time) > 60:
            clear()
            welcome_message()
            print("%s# Are you serious ? there no use of AMC. The time you entered it     #" % G)
            print("%s# will take more then 1 min to change your MAC Address.              #" % G)
            print("%s# Please enter time between 25 sec to 60 sec.                        #" % G)
            print("%s######################################################################" % W)
            sys.exit()
        else:
            return True
    except ValueError:
        display_error('CCT000X0001', ValueError, False)
    except Exception:
        parser_error('Error: argument -t/--time: expected one argument')


def amc_display(network_interface, time_left):
    """
    To display current process and left time.
    :param network_interface: network hardware name
    :param time_left: time to change mac
    :return: nothing
    """
    try:
        clear()
        welcome_message()
        print("# Your MAC address of {:<27}{:<18} #".format(network_interface + " will be change in next ",
                                                            str(time_left) + " Sec."))
        print("######################################################################")
        command_line_process(f"macchanger -s {network_interface}", network_interface)
        print("######################################################################")
        print("# To exit use Ctrl + C                                               #")
        print("######################################################################")
    except Exception as amc_display_error:
        display_error('AD0000X0001', amc_display_error, False)
    except KeyboardInterrupt:
        exit_msg(network_interface)


def run_amc(change_time, network_interface):
    """
    main function to run amc
    :param network_interface: network hardware name
    :param change_time: time to change mac
    :return: nothing
    """
    try:
        flash_new_mac(network_interface)
        time_increment = 0
        while True:
            time_left = change_time - time_increment
            if time_left == 0:
                time_increment = 0
                flash_new_mac(network_interface)
            else:
                time_increment += 1
                amc_display(network_interface, time_left)
            sleep(1)
    except KeyboardInterrupt:
        exit_msg(network_interface)


def display_license():
    clear()
    welcome_message()
    print("%s# Copyright 2021 Team Alchemists                                     #\n"
          "%s######################################################################\n"
          "%s# A Automatic Media Access Control [MAC] Address Changer (c) 2021,   #\n"
          "# This work is marked with CC0 1.0 Universal.                        #\n"
          "# To view a copy of this license, visit                              #\n"
          "#                                                                    #\n"
          "# http://creativecommons.org/publicdomain/zero/1.0                   #\n"
          "#                                                                    #\n"
          "# Unless required by applicable law or agreed to in writing,         #\n"
          "# software distributed under the License is distributed on an        #\n"
          "# \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND.       #\n"
          "# either express or implied.  See the License for the specific       #\n"
          "# language governing permissions and limitations under the License.  #\n"
          "%s######################################################################\n" % (G, W, G, W))


def about_alchemists():
    clear()
    banner()
    print("%s######################################################################" % W)
    print("%s# About Alchemists Community                                         #\n"
          "%s######################################################################\n"
          "%s# Alchemists, is cyber enthusiasm community. Who focus to aware      #\n"
          "# people about cyber security and develop open-source security tools.#\n"
          "%s######################################################################\n"
          "%s# Use -j/ --join to join Alchemists Community.                       #\n"
          "%s######################################################################\n" % (G, W, G, W, B, W))


def join_alchemist():
    clear()
    banner()
    print("%s######################################################################" % W)
    print("%s# Join Alchemists Community                                          #\n"
          "%s######################################################################\n"
          "%s# Tweet us: hexdee606, Itachi_9197, Paradox_044, Athena_74047        #\n"
          "%s######################################################################\n"
          "%s# To join please visit: join_alchemists_community                    #\n"
          "%s######################################################################\n" % (G, W, G, W, G, W))


def version_amc():
    clear()
    banner()
    print("%s######################################################################" % W)
    print("%s#     Automatic Media Access Control [MAC] Address Spoofig Tool      #" % G)
    print("%s######################################################################" % W)
    print("%s# {:<20} | {:<43} #".format("Version", amc_project_version) % Y)
    print("%s# {:<20} | {:<43} #".format("Build", amc_project_build) % Y)
    print("%s# {:<20} | {:<43} #".format("License", amc_project_license) % Y)
    print("%s# {:<20} | {:<43} #".format("IDE Name", amc_project_ide_name) % Y)
    print("%s# {:<20} | {:<43} #".format("IDE Version", amc_project_ide_version) % Y)
    print("%s# {:<20} | {:<43} #".format("Programed in", amc_project_programming_language) % Y)
    print("%s# {:<20} | {:<43} #".format(amc_project_programming_language + " Version",
                                         amc_project_programming_language_version) % Y)
    print("%s######################################################################" % W)


def parser_error(errmsg):
    welcome_message()
    print("# Usage: python3 {:<51} #".format(sys.argv[0] + " [Options] use -h for help."))
    print("%s# Error: {:<59} #".format(errmsg) % R)
    print("%s######################################################################" % W)
    sys.exit()


def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -i eth0 -t 30")
    parser.error = parser_error
    #parser._optionals.title = "OPTIONS"
    parser.add_argument('-a', '--about', help='show what is alchemist community.', metavar="", default=False, type=isboolean, const=True, nargs='?')
    parser.add_argument('-i', '--interface', help="network interface name to change mac address.", metavar="", type=str)
    parser.add_argument('-j', '--join', help='show how to join alchemists community.', default=False, metavar="", type=isboolean, const=True, nargs='?')
    parser.add_argument('-l', '--license', help='show open source license information.', default=False, metavar="", type=isboolean, const=True, nargs='?')
    parser.add_argument('-n', '--network', help='show available network interface list.', metavar="", default=False, type=isboolean, const=True, nargs='?')
    parser.add_argument('-t', '--time', help='time to change mac address automatically.', metavar="", type=int)
    parser.add_argument('-v', '--version', help='show version information.', default=False, metavar="", type=isboolean, const=True, nargs='?')
    return parser.parse_args()


def isboolean(boolean_value):
    if isinstance(boolean_value, bool):
        return boolean_value
    elif boolean_value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif boolean_value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        parser_error('boolean value expected')
        exit()


def amc_main():
    try:
        args = parse_args()
        about_alchemist = args.about
        network_hardware = args.interface
        join_alchemists = args.join
        amc_license = args.license
        hardware_list = args.network
        interval_time = args.time
        amc_version = args.version

        if isboolean(about_alchemist):
            about_alchemists()
            return None
        elif isboolean(join_alchemists):
            join_alchemist()
            return None
        elif isboolean(amc_license):
            display_license()
            return None
        elif isboolean(hardware_list):
            display_network_interface()
            return None
        elif isboolean(amc_license):
            display_license()
            return None
        elif isboolean(amc_version):
            version_amc()
            return None
        elif network_hardware == 'lo':
            clear()
            welcome_message()
            print("%s# The software loopback network interface is a software loopback     #" % B)
            print("# mechanism which may be used for performance analysis, software     #")
            print("# testing, and/or local communication. As with other network         #")
            print("# interfaces, the loopback interface must have network addresses     #")
            print("# assigned for each address family with which it is to be used.      #")
            print("%s######################################################################" % W)
            print("%s# AMC unable to change MAC address of loopback network interface     #" % R)
            print("%s# use -n/--network True for available network interface list.        #" % G)
            print("%s######################################################################" % W)
            return None
        elif not check_network_interface(network_hardware):
            clear()
            welcome_message()
            print("# Sorry there is no {:<48} #".format(network_hardware + ' interface found.'))
            print("# use -n/--network True for available network interface list.           #")
            print("######################################################################")
            show_network_list = input("%s# Do you want to see available network interface? (Y/n)              #\n" % R)
            if isboolean(show_network_list):
                display_network_interface()
            print("%s######################################################################" % W)
            return None
        elif check_network_interface(network_hardware) and check_change_time(interval_time):
            run_amc(interval_time, network_hardware)
            return None
        else:
            parser_error('Following arguments are required: -i/--interface, -t/--time')
            return None
    except Exception:
        parser_error('Following arguments are required: -i/--interface, -t/--time')
        return None


if __name__ == "__main__":
    amc_main()
    sys.exit()
