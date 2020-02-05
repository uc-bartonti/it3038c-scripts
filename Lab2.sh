#!/bin/bash

emailaddress=tbarton38@yahoo.com
today=$(date)
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')
bash=$BASH_VERSION
hostname=$HOSTNAME
content="User '$USER' with bash version '$bash' from '$hostname' '$ip' at '$today'" 
mail -s "IT3038c Linux IP" $emailaddress <<< $(echo -e $content)
