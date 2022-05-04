#!/bin/bash

while true; do

clear
sudo clear

echo '######################################################################'
echo '#                   _/_/        _/      _/        _/_/_/             #'
echo '#                _/    _/      _/_/  _/_/      _/                    #'
echo '#               _/_/_/_/      _/  _/  _/      _/                     #'
echo '#              _/    _/      _/      _/      _/                      #'
echo '#             _/    _/      _/      _/        _/_/_/                 #'
echo '#                                                                    #'
echo '#             Coded  by Dipen   Chavan   - @hexdee606                #'
echo '#             Tested by Shreyas Kulkarni - @paradox44                #'
echo '#             Tested by Aniket  Kumbhar  - @itachi-91                #'
echo '#             Tested by Ankita  Hendre   - @athena-077               #'
echo '######################################################################'
echo '#     Automatic Media Access Control [MAC] Address Spoofig Tool      #'
echo '######################################################################'
echo '# Choose # For                                                       #'
echo '######################################################################'
echo '# 1      # Automatic Media Access Control [MAC] Address Spoofing     #'
echo '# 2      # Available Network Interfaces                              #'
echo '# 3      # About Alchemists Community                                #'
echo '# 4      # Join Alchemists Community                                 #'
echo '# 5      # CC0 1.0 Universal License                                 #'
echo '# 6      # Version                                                   #'
echo '# 0      # Exit                                                      #'
echo '######################################################################'
read input_option


case $input_option in

#case 0
"0") exit 1
;;

#case 1
"1")  clear
      sudo clear
      echo '######################################################################'
      echo '#                   _/_/        _/      _/        _/_/_/             #'
      echo '#                _/    _/      _/_/  _/_/      _/                    #'
      echo '#               _/_/_/_/      _/  _/  _/      _/                     #'
      echo '#              _/    _/      _/      _/      _/                      #'
      echo '#             _/    _/      _/      _/        _/_/_/                 #'
      echo '#                                                                    #'
      echo '#             Coded  by Dipen   Chavan   - @hexdee606                #'
      echo '#             Tested by Shreyas Kulkarni - @paradox44                #'
      echo '#             Tested by Aniket  Kumbhar  - @itachi-91                #'
      echo '#             Tested by Ankita  Hendre   - @athena-077               #'
      echo '######################################################################'
      echo '#     Automatic Media Access Control [MAC] Address Spoofig Tool      #'
      echo '######################################################################'
      echo '# Please enter network interface name [Ex. eth0] :                   #' 
      read ntwrk_inter
      echo '######################################################################' 
      echo '# Please enter interval time [between 30 to 60 ] :                   #'
      read intrvl_tm
      echo '######################################################################'
      sudo python3 amc.py -i $ntwrk_inter -t $intrvl_tm
      echo "Press Enter to continue."
      read wt
;;

#case 2
"2") sudo python3 amc.py -n True
echo "Press Enter to continue."
read wt
;;

#case 3
"3") sudo python3 amc.py -a True
echo "Press Enter to continue."
read wt
;;

#case 4
"4") sudo python3 amc.py -j True
echo "Press Enter to continue."
read wt
;;

#case 5
"5") sudo python3 amc.py -l True
echo "Press Enter to continue."
read wt
;;

#case 6
"6") sudo python3 amc.py -v True
echo "Press Enter to continue."
read wt
;;

*)  
      clear
      sudo clear
      echo '######################################################################'
      echo '#                   _/_/        _/      _/        _/_/_/             #'
      echo '#                _/    _/      _/_/  _/_/      _/                    #'
      echo '#               _/_/_/_/      _/  _/  _/      _/                     #'
      echo '#              _/    _/      _/      _/      _/                      #'
      echo '#             _/    _/      _/      _/        _/_/_/                 #'
      echo '#                                                                    #'
      echo '#             Coded  by Dipen   Chavan   - @hexdee606                #'
      echo '#             Tested by Shreyas Kulkarni - @paradox44                #'
      echo '#             Tested by Aniket  Kumbhar  - @itachi-91                #'
      echo '#             Tested by Ankita  Hendre   - @athena-077               #'
      echo '######################################################################'
      echo '#     Automatic Media Access Control [MAC] Address Spoofig Tool      #'
      echo '######################################################################'
      echo '# ERROR AMCSH0000x000001 : Please select valid option.               #'
      echo '######################################################################'
      echo "Press Enter to continue."
      read wt
;;

esac

done 

exit 1
