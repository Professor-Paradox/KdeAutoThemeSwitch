#!/bin/bash

# dark theme data
# look and feel
# DLAF="/home/t/"
# plasmatheme
# DPL=""
#application style
# DAPS=""
# window decoration
# DWD=""
#gtk theme
# DG=""
#color scheme
# DCS=""
#icons
# DI=""
#cursor
# DC=""
#gtk cursor
# DGC=""
#kvantum
# DK=""
#splash screen
# DSP=""

# taking exisiting data
. ./userInput.txt

echo `date` &>./log.txt
echo "inside dark script" &>>./log.txt

# edits lookandfeel
lookandfeeltool -a  "$DLAF" &>>./log.txt
echo "changing look and feel" &>>./log.txt
sleep 0.5


# updating theme variable
sed -i 's/currentTheme\=.*/currentTheme="dark"/' userInput.txt


# edits plasmatheme
echo "changing plasmatheme" &>>./log.txt
kwriteconfig5 --file ~/.config/plasmarc --group Theme --key name "$DPL" &>>./log.txt
sleep 0.5

#application style edit
echo "changing application style" &>>./log.txt
kwriteconfig5 --file ~/.config/kdeglobals --group KDE --key widgetStyle "$DAPS" &>>./log.txt
sleep 0.5

# window decoration
echo "changing window decoration" &>>./log.txt
kwriteconfig5 --file ~/.config/kwinrc --group org.kde.kdecoration2 --key theme "__aurorae__svg__$DWD" &>>./log.txt
sleep 0.5

# editing gtk theme
echo "changing gtk theme" &>>./log.txt
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name "$DG" &>>./log.txt
sleep 0.5

#edits color scheme
echo "changing color scheme" &>>./log.txt
kwriteconfig5 --file ~/.config/kdeglobals --group General --key ColorScheme "$DCS" &>>./log.txt
sleep 0.5

#change icons
echo "changing icons" &>>./log.txt
kwriteconfig5 --file ~/.config/kdeglobals --group Icons --key Theme "$DI" &>>./log.txt
sleep 0.5

# change cursor
echo "changing cursor" &>>./log.txt
kwriteconfig5 --file ~/.config/kcminputrc --group Mouse --key cursorTheme "$DC" &>>./log.txt
sleep 0.5

#editing cursor theme for gtk
echo "changing gtk cursor theme" &>>./log.txt
kwriteconfig5 --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-cursor-theme-name "$DGC" &>>./log.txt
sleep 0.5

# applying kvantum theme 
echo "changing kvantum theme" &>>./log.txt
kvantummanager --set "$DK" &>>./log.txt
sleep 0.5

# editing splash screen
echo "changing splash screen" &>>./log.txt
kwriteconfig5 --file ~/.config/ksplashrc --group KSplash --key Theme "$DSP" &>>./log.txt
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

# don't remove the & symbol.it gives back the control of shell to user.
latte-dock -r & 
echo "applied Dark theme" &>>./log.txt
sleep 0.5