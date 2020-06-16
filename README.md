# AutomaticThemeSwitcher

Configurable theme switching script.

takes user input for the customization of light theme and dark theme.

after set up the script will run  based on the time.


**Files Guide**
this folder can be kept hidden in the home directory or in a separate directory,but need the files to run the script every time.

**run in terminal**     
`sh ./userInput.sh`     

* this will generate a *exisitingThemeInfo.txt* file.    
* This file will have all the customization details of exisiting system.     
* copy and paste the names of relavent theme names when asked.           
* open settings app and follow along for better understanding of theme/icons names.         

           
* the names of themes,icons,cursor,colors etc,. are needed with out them the theming can be messed up.
* After entering all data will be saved in scripts folder with name userInput.txt(don't delete this as this is used for every script for switching theme)      

   Once you run the userInput and everything is setup you don't have to run any script.all is taken care of .          

a log file in the scripts folder is created everytime a theme switch takes place for debugging.
It works fine for me. tweaked the scripts for errors i faced.        



**For Devs**     
I took data from user and stored the theming details he would like to switch on time and saved in a file and used it in all scripts.          
took exisiting system themes lists and saved in a file,for taking better input from user, what he would like to switch to.     
switching themes by editing the user files related to their category.    
have a separate script for dark and light and a theme script that gets triggered by a cron job every thirty minutes to check the condition,whether to switch the theme or not.
all of them  are interlinked(don't delete them.)
a log for theme is generated everytime a script is executed to debug any errors.
I am including my theme data for reference with a different name.