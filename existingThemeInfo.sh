#!/bin/bash

# printing look and feel data
echo -e "lookAndFeel" &> existingThemeInfo.txt
echo -e "==============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.local/share/plasma/look-and-feel/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/plasma/look-and-feel/ &>> existingThemeInfo.txt

# printing plasma theme data
echo -e "\nplasmaTheme" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.local/share/plasma/desktoptheme/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/plasma/desktoptheme/ &>> existingThemeInfo.txt


# printing applicationStyle data
echo -e "\napplicationStyle" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "manually check this one\n" &>> existingThemeInfo.txt

# printing windowdecorations data
echo -e "\nwindowDecorations" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.local/share/aurorae/themes/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/kwin/decorations/ &>> existingThemeInfo.txt

# printing colorScheme data
echo -e "\ncolorScheme" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.local/share/color-schemes/color-schemes/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/color-schemes/ &>> existingThemeInfo.txt

# printing Icons data
echo -e "\nIcons" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.local/share/icons/icons/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/icons/ &>> existingThemeInfo.txt

# printing Cursor data
echo -e "\nCursor" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.icons/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/icons/ | grep cursor &>> existingThemeInfo.txt

# printing splash screen data
echo -e "\nsplashScreen" &>> existingThemeInfo.txt
echo -e "=============" &>> existingThemeInfo.txt
echo -e "----------\nuserThemes\n-------------" &>> existingThemeInfo.txt
ls ~/.local/share/plasma/look-and-feel/ &>> existingThemeInfo.txt
echo -e  "----------\nsystemThemes\n-----------" &>> existingThemeInfo.txt
ls /usr/share/plasma/look-and-feel/ &>> existingThemeInfo.txt
