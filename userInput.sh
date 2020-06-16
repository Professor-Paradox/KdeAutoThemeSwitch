#!/bin/bash

# taking system theme data
echo "take data from exisitingThemeinfo.txt file"
./existingThemeInfo.sh

echo -e "Starting to take input,specify configuration of desired LIGHT theme.\n"

# taking input from user about theme and displaying
echo -e "Enter look and feel name"
read LAF

echo -e "Enter plasmatheme name "
read PL

echo -e "Enter application style name "
read APS

echo -e "Enter window decoration name"
read WD

echo -e "Enter gtk theme name"
read G

echo -e "Enter color scheme name "
read CS

echo -e "Enter icons name "
read I

echo -e "Enter cursor name "
read C

echo -e "Enter gtk cursor name "
read GC

echo -e "Enter kvantum name "
read K

echo -e "Enter splash screen name "
read SP

echo "look and feel     = $LAF"
echo "plasmatheme       = $PL"
echo "application style = $APS"
echo "window decoration = $WD"
echo "gtk theme         = $G"
echo "color scheme      = $CS"
echo "icons             = $I"
echo "cursor            = $C"
echo "gtk cursor        = $GC"
echo "kvantum           = $K"
echo "splash screen     = $SP"


echo -e "Starting to take input,specify configuration of desired DARK theme.\n \n\n"
# taking input from user about theme and displaying

echo -e "Enter look and feel name"
read DLAF

echo -e "Enter plasmatheme name "
read DPL

echo -e "Enter application style name "
read DAPS

echo -e "Enter window decoration name"
read DWD

echo -e "Enter gtk theme name"
read DG

echo -e "Enter color scheme name "
read DCS

echo -e "Enter icons name "
read DI

echo -e "Enter cursor name "
read DC

echo -e "Enter gtk cursor name "
read DGC

echo -e "Enter kvantum name "
read DK

echo -e "Enter splash screen name "
read DSP


echo "look and feel     = $DLAF" 
echo "plasmatheme       = $DPL"
echo "application style = $DAPS"
echo "window decoration = $DWD"
echo "gtk theme         = $DG"
echo "color scheme      = $DCS"
echo "icons             = $DI"
echo "cursor            = $DC"
echo "gtk cursor        = $DGC"
echo "kvantum           = $DK"
echo "splash screen     = $DSP"

# storing the data in to a file
echo -e "LAF='$LAF'\nPL='$PL'\nAPS='$APS'\nWD='$WD'\nG='$G'\nCS='$CS'\nI='$I'\nC='$C'\nGC='$GC'\nK='$K'\nSP='$SP'" &> ./scripts/userInput.txt
echo -e "DLAF='$DLAF'\nDPL='$DPL'\nDAPS='$DAPS'\nDWD='$DWD'\nDG='$DG'\nDCS='$DCS'\nDI='$DI'\nDC='$DC'\nDGC='$DGC'\nDK='$DK'\nDSP='$DSP'" &>> ./scripts/userInput.txt

echo -e "currentTheme='light'" &>> ./scripts/userInput.txt | &> /dev/null

echo -e "Enter the time to switch from light to dark\n Ex: 18 will be 6pm, theme will be light before 6pm,dark after 6pm."
read switchTime

echo -e "switchTime='$switchTime'" &>> ./scripts/userInput.txt | &> /dev/null
# setting a cron job
crontab -l | { cat; echo "*/30 * * * * ~/Documents/Bash/scripts/theme.sh"; } | crontab -
