# AutomaticThemeSwitcher

Configurable theme switching script.

takes user input for the customization of light theme and dark theme.

after set up the script will run  based on the time(crontab).


**Files Guide**
the files in scripts folder will be needed to change theme.

**run in terminal**     
`sh ./userInput.sh`     

* this will generate a *exisitingThemeInfo.txt* file.    
* This file will have all the customization details of exisiting system.     
* copy and paste the names of relavent theme names when asked.attaching my theme details for reference.           
* open settings app and follow along for better understanding of theme/icons names.         

           
* the names of themes,icons,cursor,colors etc,. are needed with out them the theming can be messed up.
* After entering all data will be saved in scripts folder with name userInput.txt(don't delete this as this is used for every script for switching theme)      

   Once you run the userInput and everything is setup you don't have to run any script.all is taken care of.          

After running the script,it will setup a cronjob so the theme can be changed automatically. 
the script folder and the data needed will be copied to **./.themeScripts/** and a log for any errors will be present their.
It works fine for me. tweaked the scripts for errors i faced.        

**For Devs**     
I took data from user and stored the theming details he would like to switch on time and saved in a file and used it in all scripts.      
Created a exisitingThemeinfo file to assist the  user while entering the names of themes.     
switching themes by editing the user files related to their category.
* plasmarc
* kdeglobals
* kwinrc
* gtk-3.0/settings.ini
* kcminputrc
* ksplashrc
* kvantum(if installed)

created a cron job that runs every five minutes to check the condition,whether to switch the theme or not.
all files are interlinked(don't delete them.)
a log for theme is generated everytime a script is executed to debug any errors.
I am including my theme data for reference with a different name.uploading all the files in my setup.