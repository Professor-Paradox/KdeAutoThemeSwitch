#!/bin/bash
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

# taking exisiting data
. ./userInput.txt

echo `date` &>./log.txt
echo "inside light script" &>>./log.txt

# edits lookandfeel
echo "changing look and feel" &>>./log.txt
lookandfeeltool -a  "$LAF" &>>./log.txt
sleep 0.5


# edits plasmatheme
echo "changing plasmatheme" &>>./log.txt
kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name "$PL" &>>./log.txt
sleep 0.5

#application style edit
echo "changing application style" &>>./log.txt
kwriteconfig5 --file ~/.config/kdeglobals --group KDE --key widgetStyle "$APS" &>>./log.txt
sleep 0.5

# window decoration
echo "changing window decoration" &>>./log.txt
kwriteconfig5 --file ~/.config/kwinrc --group org.kde.kdecoration2 --key theme "__aurorae__svg__$WD" &>>./log.txt
sleep 0.5

# editing gtk theme
echo "changing gtk theme" &>>./log.txt
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name "$G" &>>./log.txt
sleep 0.5

#edits color scheme
echo "changing color scheme" &>>./log.txt
kwriteconfig5 --file ~/.config/kdeglobals --group General --key ColorScheme "$CS" &>>./log.txt
sleep 0.5

#change icons
echo "changing icons" &>>./log.txt
kwriteconfig5 --file ~/.config/kdeglobals --group Icons --key Theme "$I" &>>./log.txt
sleep 0.5

# change cursor
echo "changing cursor" &>>./log.txt
kwriteconfig5 --file ~/.config/kcminputrc --group Mouse --key cursorTheme "$C" &>>./log.txt
sleep 0.5

#editing cursor theme for gtk
echo "changing gtk cursor theme" &>>./log.txt
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-cursor-theme-name "$GC" &>>./log.txt
sleep 0.5

# applying kvantum theme 
echo "changing kvantum theme" &>>./log.txt
kvantummanager --set "$K" &>>./log.txt
sleep 0.5

# editing splash screen
echo "changing splash screen" &>>./log.txt
kwriteconfig5 --file ~/.config/ksplashrc --group KSplash --key Theme "$SP" &>>./log.txt
sleep 0.5

# editing task switcher
echo "changing task switcher" &>>./log.txt
kwriteconfig5 --file ~/.config/kwinrc --group TabBox --key LayoutName "MediumRounded" &>>./log.txt
sleep 0.5

#restart plasma shell and latte-dock and kwin
echo "restarting kwin" &>>./log.txt
qdbus org.kde.KWin /KWin reconfigure &>>./log.txt
sleep 0.5

# to see the output of command/errors replace ./log.txt with a file name
echo "restarting plasmashell & latte-dock" &>>./log.txt
kquitapp5 plasmashell && kstart5 plasmashell &>>./log.txt

sleep 0.5

# updating theme variable
sed -i 's/currentTheme\=.*/currentTheme="light"/' userInput.txt

# don't remove the & symbol.it gives back the control of shell to user.
# killall latte-dock
echo "applied Light theme" &>>./log.txt
latte-dock -r & 
sleep 0.5
