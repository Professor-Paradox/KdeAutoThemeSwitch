#!/bin/bash
# passing required environment variables,don't change these, if doesn't work use env | grep -i command,copy that and paste here.If needed change the user name to your home directory

export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
export DESKTOP_SESSION=plasma
export DISPLAY=:0
export PATH=/home/t/.local/bin:/home/t/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:JAVA_HOME/bin:JAVA_HOME/bin
export SHELL=/bin/bash
export XDG_CURRENT_DESKTOP=KDE
export XDG_DATA_DIRS=/usr/share/plasma:/usr/local/share:/usr/share:/var/lib/snapd/desktop
export XDG_RUNTIME_DIR=/run/user/1000

# export COLORFGBG=0;15
# export COLORTERM=truecolor
# export GPG_AGENT_INFO=/run/user/1000/gnupg/S.gpg-agent:0:1
# export GTK_MODULES=gail:atk-bridge
# export HOME=/home/t
# export JAVA_HOME=/usr/lib/jvm/java-14-openjdk-amd64/
# export KDE_FULL_SESSION=true
# export KDE_SESSION_UID=1000
# export KDE_SESSION_VERSION=5
# export KONSOLE_DBUS_SERVICE=:1.46
# export KONSOLE_DBUS_SESSION=/Sessions/1
# export KONSOLE_VERSION=191203
# export LANG=en_IN.UTF-8
# export LANGUAGE=en_IN:en
# export LESSCLOSE=/usr/bin/lesspipe %s %s
# export LESSOPEN=| /usr/bin/lesspipe %s
# export LOCAL=/home/t/.local/bin
# export LOGNAME=t
# export PAM_KWALLET5_LOGIN=/run/user/1000/kwallet5.socket
# export PROFILEHOME=
# export PWD=/home/t
# export QT_ACCESSIBILITY=1
# export QT_AUTO_SCREEN_SCALE_FACTOR=0
# export QT_SCREEN_SCALE_FACTORS=VGA-0=1;DVI-D-0=1;HDMI-0=1;
# export SESSION_MANAGER=local/Mr-T-Kde-Pc:@/tmp/.ICE-unix/435857,unix/Mr-T-Kde-Pc:/tmp/.ICE-unix/435857
# export SHELL_SESSION_ID=4a8dd494278e4d5ea2f064b0603897df
# export SHLVL=1
# export SSH_AGENT_PID=435788
# export SSH_AUTH_SOCK=/tmp/ssh-S2Cgv84D5u4g/agent.435744
# export TERM=xterm-256color
# export USER=t
# export WINDOWID=0
# export XAUTHORITY=/home/t/.Xauthority
# export XCURSOR_SIZE=32
# export XCURSOR_THEME=material_dark_cursors
# export XDG_CONFIG_DIRS=/etc/xdg/xdg-plasma:/etc/xdg
# export XDG_SEAT=seat0
# export XDG_SEAT_PATH=/org/freedesktop/DisplayManager/Seat0
# export XDG_SESSION_CLASS=user
# export XDG_SESSION_DESKTOP=KDE
# export XDG_SESSION_ID=139
# export XDG_SESSION_PATH=/org/freedesktop/DisplayManager/Session8
# export XDG_SESSION_TYPE=x11
# export XDG_VTNR=1

# light theme variables,dark theme variables start with D
# look and feel
# LAF=""
# plasmatheme
# PL=""
#application style
# APS=""
# window decoration
# WD=""
#gtk theme
# G=""
#color scheme
# CS=""
#icons
# I=""
#cursor
# C=""
#gtk cursor
# GC=""
#kvantum
# K=""
#splash screen
# SP=""

# changing to scripts directory and making this script path independent
DIR="$(dirname $0)"
cd $DIR

# reading the file with data saved
date &>> ./log.txt
source ./userInput.txt &>>./log.txt

# edits lookandfeel
function lookAndFeel(){
   echo "changing look and feel"
   lookandfeeltool -a  "$1" ;
   sleep 0.5
}

# edits plasmatheme
function plasmaTheme(){
   echo "changing plasmatheme"
   kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name "$1" ;
   sleep 0.5
}

# plasmaTheme $PL &>> ./log.txt/


#application style edit
function applicationStyleEdit(){
   echo "changing applicationStyleEdit"
   kwriteconfig5 --file ~/.config/kdeglobals --group KDE --key widgetStyle "$1" ;
   sleep 0.5
}

# applicationStyleEdit $APS &>> ./log.txt


# window decoration
function windowDecoration(){
   echo "changing windowDecoration"
   kwriteconfig5 --file ~/.config/kwinrc --group org.kde.kdecoration2 --key theme "__aurorae__svg__$1" ;
   sleep 0.5
}

# windowDecoration $WD &>> ./log.txt

# editing gtk theme
function gtkTheme(){
   echo "changing gtkTheme"
   kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name "$1" ;
   sleep 0.5
}

# gtkTheme $G &>> ./log.txt

#edits color scheme
function colorScheme(){
   echo "changing colorScheme"
   kwriteconfig5 --file ~/.config/kdeglobals --group General --key ColorScheme "$1" ;
   sleep 0.5
}

# colorScheme $CS &>> ./log.txt

#change icons
function icons(){
   echo "changing icons"
   kwriteconfig5 --file ~/.config/kdeglobals --group Icons --key Theme "$1" ;
   sleep 0.5
}

# icons $I &>> ./log.txt

# change cursor
function cursor(){
   echo "changing cursor"
   kwriteconfig5 --file ~/.config/kcminputrc --group Mouse --key cursorTheme "$1" ;
   sleep 0.5
}

# cursor $C &>> ./log.txt

#editing cursor theme for gtk
function gtkCursor(){
   echo "changing gtkCursor"
   kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-cursor-theme-name "$1" ;
   sleep 0.5
}

# gtkCursor $GC &>> ./log.txt


# applying kvantum theme 
function kvantumTheme(){
   echo "changing kvantumTheme"
   kvantummanager --set "$1" ;
   sleep 0.5
}

# kvantumTheme $K &>> ./log.txt

# editing splash screen
function splashScreen(){
   echo "changing splashScreen"
   kwriteconfig5 --file ~/.config/ksplashrc --group KSplash --key Theme "$1" ;
   sleep 0.5
}

# splashScreen $SP &>> ./log.txt


# editing task switcher
function taskSwitcher(){
   echo "changing taskSwitcher"
   kwriteconfig5 --file ~/.config/kwinrc --group TabBox --key LayoutName "MediumRounded" ;
   sleep 0.5
}

# taskSwitcher &>> ./log.txt

#restart plasma shell and latte-dock and kwin
function restartUI(){
   echo "restarting Kwin"
   qdbus org.kde.KWin /KWin reconfigure ;
   echo "restarting plasmashell & latte-dock"
   kquitapp5 plasmashell && kstart5 plasmashell ;
   sleep 0.5
}
 
function updateFile(){
   # to see the output of command/errors replace ./log.txt with a new file name
   # updating theme variable
   sed -i "s/currentTheme\=.*/currentTheme='$1'/" userInput.txt
   echo "applied $1 theme" &>>./log.txt
   latte-dock -r & 
   # don't remove the & symbol.it gives back the control of shell to user.
   sleep 0.5
}


# function for light theme
function light(){
   echo `date` &>./log.txt
   echo "inside light script" ; &>>./log.txt

   # calling the functions
   lookAndFeel $LAF &>> ./log.txt
   plasmaTheme $PL &>> ./log.txt
   applicationStyleEdit $APS &>> ./log.txt
   windowDecoration $WD &>> ./log.txt
   gtkTheme $G &>> ./log.txt
   colorScheme $CS &>> ./log.txt
   icons $I &>> ./log.txt
   cursor $C &>> ./log.txt
   gtkCursor $GC &>> ./log.txt
   kvantumTheme $K &>> ./log.txt
   splashScreen $SP &>> ./log.txt
   taskSwitcher &>> ./log.txt
   restartUI &>> ./log.txt
   updateFile "light" &>> ./log.txt
}

# function for dark theme
function dark(){
   echo `date` &>./log.txt
   echo "inside dark script" ; &>>./log.txt

   # calling the functions
   lookAndFeel $DLAF &>> ./log.txt
   plasmaTheme $DPL &>> ./log.txt
   applicationStyleEdit $DAPS &>> ./log.txt
   windowDecoration $DWD &>> ./log.txt
   gtkTheme $DG &>> ./log.txt
   colorScheme $DCS &>> ./log.txt
   icons $DI &>> ./log.txt
   cursor $DC &>> ./log.txt
   gtkCursor $DGC &>> ./log.txt
   kvantumTheme $DK &>> ./log.txt
   splashScreen $DSP &>> ./log.txt
   taskSwitcher &>> ./log.txt
   restartUI &>> ./log.txt
   updateFile "dark" &>> ./log.txt
}

# takes input from crontab and switches when conditions meet.
hour=$(date +%H | sed 's/^0//')
if [[ "$hour" -ge $switchTime ]]
then
   if [ $currentTheme == 'light' ]
   then
      dark #calling the dark theme function
   fi
fi
if [[ "$hour" -lt $switchTime ]]
then
   if [ $currentTheme == 'dark' ]
   then
      light # calling the light theme function
   fi
fi

