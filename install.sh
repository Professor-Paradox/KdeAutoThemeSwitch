python3 -m venv env1
source ./env1/bin/activate
pip install pyqt5
pip install pyqt5-tools
echo "python tools installed successfully"
python src/UiControl.py
mkdir ~/.kdeAutoThemeSwitch
cp src/userSelection.txt ~/.kdeAutoThemeSwitch
cp src/theme.sh ~/.kdeAutoThemeSwitch
# setting a cron job1
echo "setting a cron job to switch theme at specified time"
crontab -l > tmp.txt
echo -e "#cronjob for changing theme \n* * * * *    ~/.kdeAutoThemeSwitch/theme.sh" >> tmp.txt  
crontab tmp.txt
rm tmp.txt