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
#########################################################################################
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
hour=`date +%H`
if [[ "$hour" -ge $switchTime ]]
then
   if [ $currentTheme == "light" ]
   then
      dark #calling the dark theme function
   fi
fi
if [[ "$hour" -lt $switchTime ]]
then
   if [ $currentTheme == "dark" ]
   then
      light # calling the light theme function
   fi
fi

