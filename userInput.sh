#!/bin/bash

# taking system theme data
echo "take data from existingThemeinfo.txt file"
function existingthemedata(){
# printing look and feel data
{ #grouping to redirect all output at once to a file
echo -e "lookAndFeel\n=================\n----------\nuserThemes\n-------------" 
ls ~/.local/share/plasma/look-and-feel/ ; } &> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/plasma/look-and-feel/ ; } &>> ./existingThemeInfo.txt

#printing plasma theme data
{
echo -e "\nplasmaTheme\n=============\n----------\nuserThemes\n-------------"  
ls ~/.local/share/plasma/desktoptheme/ ; } &>> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/plasma/desktoptheme/ ; } &>> ./existingThemeInfo.txt


# printing applicationStyle data
{
echo -e "\napplicationStyle\n=============\nmanually check this one\nwindowDecorations\n==============" 
# printing windowdecorations data
echo -e "----------\nuserThemes\n-------------" 
ls ~/.local/share/aurorae/themes/ ; } &>> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/kwin/decorations/ ; } &>> ./existingThemeInfo.txt

# printing colorScheme data
{
echo -e "\ncolorScheme\n=============\n----------\nuserThemes\n-------------"
ls ~/.local/share/color-schemes/color-schemes/ ; } &>> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/color-schemes/ ; } &>> ./existingThemeInfo.txt

# printing Icons data
{
echo -e "\nIcons\n=============\n----------\nuserThemes\n-------------" 
ls ~/.local/share/icons/icons/ ; } &>> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/icons/ ; } &>> ./existingThemeInfo.txt

# printing Cursor data
{
echo -e "\nCursor\n=============\n----------\nuserThemes\n-------------" 
ls ~/.icons/ ; } &>> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/icons/ | grep cursor ; } &>> ./existingThemeInfo.txt

# printing splash screen data
{
echo -e "\nsplashScreen\n=============\n----------\nuserThemes\n-------------" 
ls ~/.local/share/plasma/look-and-feel/ ; } &>> ./existingThemeInfo.txt

{
echo -e  "----------\nsystemThemes\n-----------" 
ls /usr/share/plasma/look-and-feel/ ; } &>> ./existingThemeInfo.txt

}

# calling theme data function
existingthemedata

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

# displaying entered data
echo -e "
look and feel     = $LAF
plasmatheme       = $PL
application style = $APS
window decoration = $WD
gtk theme         = $G
color scheme      = $CS
icons             = $I
cursor            = $C
gtk cursor        = $GC
kvantum           = $K
splash screen     = $SP" 

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

# displaying entered data
echo -e "
look and feel     = $DLAF
plasmatheme       = $DPL
application style = $DAPS
window decoration = $DWD
gtk theme         = $DG
color scheme      = $DCS
icons             = $DI
cursor            = $DC
gtk cursor        = $DGC
kvantum           = $DK
splash screen     = $DSP" 

# saving user entered data to a file
echo -e "
LAF='$LAF'
PL='$PL'
APS='$APS'
WD='$WD'
G='$G'
CS='$CS'
I='$I'
C='$C'
GC='$GC'
K='$K'
SP='$SP'

DLAF='$DLAF'
DPL='$DPL'
DAPS='$DAPS'
DWD='$DWD'
DG='$DG'
DCS='$DCS'
DI='$DI'
DC='$DC'
DGC='$DGC'
DK='$DK'
DSP='$DSP'

currentTheme='light'" &> ./scripts/userInput.txt | &> /dev/null

echo -e "Enter the time to switch from light to dark\n Ex: 18 will be 6pm, theme will be light before 6pm,dark after 6pm."
read switchTime
echo -e "switchTime='$switchTime'" &>> ./scripts/userInput.txt | &> /dev/null

echo "copying theme files to home directory in .themeScripts/files"
mkdir ~/.themeScripts
cp scripts/* ~/.themeScripts/

# setting a cron job
echo "setting a cron job to switch theme at specified time"
crontab -l > tmp.txt
echo -e "#cronjob for changing theme \n*/5 * * * *    ~/.themeScripts/theme.sh" >> tmp.txt  
crontab tmp.txt
rm tmp.txt