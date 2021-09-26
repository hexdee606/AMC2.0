#!/bin/bash

echo '############################################################'
echo '#   Automatic Media Access Control [MAC] Address Changer   #'
echo '############################################################'
echo '# Choose # For                                             #'
echo '############################################################'
echo '# 1      # Change MAC Address Automatically                #'
echo '# 2      # Display Available Network Interfaces            #'
echo '# 3      # About Alchemists                                #'
echo '# 4      # Join Alchemists                                 #'
echo '# 5      # Version                                         #'
echo '# 0      # Exit                                            #'
echo '############################################################'
read input_option

case $input_option in

#case 0
"0") exit 1
;;

#case 1
"1")  clear
      sudo clear
      echo '############################################################'
      echo '#   Automatic Media Access Control [MAC] Address Changer   #'
      echo '############################################################'
      echo '# Please enter network interface name [Ex. eth0] :  ' 
      read ntwrk_inter
      echo '############################################################' 
      echo '# Please enter interval time [between 25 to 60 ] :  '
      read intrvl_tm
      echo '############################################################'
      sudo python3 amc.py -i $ntwrk_inter -t $intrvl_tm
;;

#case 2
"2") sudo python3 amc.py -n True
;;

#case 3
"3") sudo python3 amc.py -a True
;;

#case 4
"4") sudo python3 amc.py -j True
;;

#case 5
"5") sudo python3 amc.py -v True
;;

*)  
      clear
      sudo clear
      echo '############################################################'
      echo '#   Automatic Media Access Control [MAC] Address Changer   #'
      echo '############################################################'
      echo '# ERROR : PLEASE ENTER VALID OPTION                        #'
      echo '############################################################' 
;;
esac

echo "Press Enter to Exit code."
read wt
exit 1