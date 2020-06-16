#!/bin/bash
# passing required environment variables,don't change these, if doesn't work use env | grep -i command,copy that and paste here.
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
export DESKTOP_SESSION=plasma
export DISPLAY=:0
export SHELL=/bin/bash
export XDG_CURRENT_DESKTOP=KDE
export XDG_RUNTIME_DIR=/run/user/1000

# changing to scripts directory and making this script path independent
DIR="$(dirname $0)"
cd $DIR

# reading the file with data saved
source ./userInput.txt

hour=`date +%H`
if [[ "$hour" -ge $switchTime ]]
then
   if [ $currentTheme == "light" ]
   then
      ./dark.sh
   fi
fi
if [[ "$hour" -lt $switchTime ]]
then
   if [ $currentTheme == "dark" ]
   then
      ./light.sh 
   fi
fi

