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



# changing to scripts directory and making this script path independent
DIR="$(dirname $0)"
cd $DIR

# reading the file with data saved
date &>> ./log.txt
source ./userInput.txt &>>./log.txt

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


# functions for light theme and dark theme
function light(){
{
echo `date` 
echo "inside light script" ; } &>./log.txt

# edits lookandfeel
{
echo "changing look and feel"
lookandfeeltool -a  "$LAF" ; } &>>./log.txt
sleep 0.5


# edits plasmatheme
{
echo "changing plasmatheme"
kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name "$PL" ; } &>>./log.txt
sleep 0.5

#application style edit
{
echo "changing application style"
kwriteconfig5 --file ~/.config/kdeglobals --group KDE --key widgetStyle "$APS" ; } &>>./log.txt
sleep 0.5

# window decoration
{
echo "changing window decoration"
kwriteconfig5 --file ~/.config/kwinrc --group org.kde.kdecoration2 --key theme "__aurorae__svg__$WD" ; } &>>./log.txt
sleep 0.5

# editing gtk theme
{
echo "changing gtk theme" 
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name "$G" ; } &>>./log.txt
sleep 0.5

#edits color scheme
{
echo "changing color scheme" 
kwriteconfig5 --file ~/.config/kdeglobals --group General --key ColorScheme "$CS" ; } &>>./log.txt
sleep 0.5

#change icons
{
echo "changing icons" 
kwriteconfig5 --file ~/.config/kdeglobals --group Icons --key Theme "$I" ; } &>>./log.txt
sleep 0.5

# change cursor
{
echo "changing cursor" 
kwriteconfig5 --file ~/.config/kcminputrc --group Mouse --key cursorTheme "$C" ; } &>>./log.txt
sleep 0.5

#editing cursor theme for gtk
{
echo "changing gtk cursor theme" &>>./log.txt
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-cursor-theme-name "$GC" ; } &>>./log.txt
sleep 0.5

{
# applying kvantum theme 
echo "changing kvantum theme" 
kvantummanager --set "$K" ; } &>>./log.txt
sleep 0.5

# editing splash screen
{
echo "changing splash screen" 
kwriteconfig5 --file ~/.config/ksplashrc --group KSplash --key Theme "$SP" ; } &>>./log.txt
sleep 0.5

# editing task switcher
{
echo "changing task switcher"
kwriteconfig5 --file ~/.config/kwinrc --group TabBox --key LayoutName "MediumRounded" ; } &>>./log.txt
sleep 0.5

#restart plasma shell and latte-dock and kwin
{
echo "restarting kwin"
qdbus org.kde.KWin /KWin reconfigure ; } &>>./log.txt
sleep 0.5

# to see the output of command/errors replace ./log.txt with a file name
{
echo "restarting plasmashell & latte-dock" 
kquitapp5 plasmashell && kstart5 plasmashell ; } &>>./log.txt
sleep 0.5

# updating theme variable
sed -i 's/currentTheme\=.*/currentTheme="light"/' userInput.txt

# don't remove the & symbol.it gives back the control of shell to user.
# killall latte-dock
echo "applied Light theme" &>>./log.txt
latte-dock -r & 
sleep 0.5

}

function dark(){
{
echo `date` 
echo "inside dark script" ; } &>./log.txt

# edits lookandfeel
{
echo "changing look and feel" 
lookandfeeltool -a  "$DLAF" ; } &>>./log.txt
sleep 0.5


# updating theme variable
sed -i 's/currentTheme\=.*/currentTheme="dark"/' userInput.txt


# edits plasmatheme
{
echo "changing plasmatheme" 
kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name "$DPL" ; } &>>./log.txt
sleep 0.5

#application style edit
{
echo "changing application style" 
kwriteconfig5 --file ~/.config/kdeglobals --group KDE --key widgetStyle "$DAPS" ; } &>>./log.txt
sleep 0.5

# window decoration
{
echo "changing window decoration" 
kwriteconfig5 --file ~/.config/kwinrc --group org.kde.kdecoration2 --key theme "__aurorae__svg__$DWD" ; } &>>./log.txt
sleep 0.5

# editing gtk theme
{
echo "changing gtk theme" 
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name "$DG" ; } &>>./log.txt
sleep 0.5

#edits color scheme
{
echo "changing color scheme" 
kwriteconfig5 --file ~/.config/kdeglobals --group General --key ColorScheme "$DCS" ; } &>>./log.txt
sleep 0.5

#change icons
{
echo "changing icons" 
kwriteconfig5 --file ~/.config/kdeglobals --group Icons --key Theme "$DI" ; } &>>./log.txt
sleep 0.5

# change cursor
{
echo "changing cursor" 
kwriteconfig5 --file ~/.config/kcminputrc --group Mouse --key cursorTheme "$DC" ; } &>>./log.txt
sleep 0.5

#editing cursor theme for gtk
{
echo "changing gtk cursor theme" 
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-cursor-theme-name "$DGC" ; } &>>./log.txt
sleep 0.5

# applying kvantum theme 
{
echo "changing kvantum theme" 
kvantummanager --set "$DK" ; } &>>./log.txt
sleep 0.5

# editing splash screen
{
echo "changing splash screen" 
kwriteconfig5 --file ~/.config/ksplashrc --group KSplash --key Theme "$DSP" ; } &>>./log.txt
sleep 0.5

# editing task switcher
{
echo "changing task switcher" 
kwriteconfig5 --file ~/.config/kwinrc --group TabBox --key LayoutName "MediumRounded" ; } &>>./log.txt
sleep 0.5

#restart plasma shell and latte-dock and kwin
{
echo "restarting kwin" 
qdbus org.kde.KWin /KWin reconfigure ; } &>>./log.txt
sleep 0.5

# to see the output of command/errors replace ./log.txt with a file name
{
echo "restarting plasmashell & latte-dock" 
kquitapp5 plasmashell && kstart5 plasmashell ; } &>>./log.txt
sleep 0.5

# don't remove the & symbol.it gives back the control of shell to user.
latte-dock -r & 
echo "applied Dark theme" &>>./log.txt
sleep 0.5
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

