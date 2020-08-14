# Running this script will install a virtual environment in current directory with packages.

# Takes user input with ui,stores the data in a text file and sets up a cron job.
python3 -m venv env
source ./env/bin/activate
pip install --upgrade pip
pip install pyqt5 pyqt5-tools
echo "python packages are installed successfully"
python ./src/PythonSrc/MyUI.py
mkdir ~/.kdeAutoThemeSwitch
cp userSelection.txt ~/.kdeAutoThemeSwitch
cp src/theme.sh ~/.kdeAutoThemeSwitch

# setting a cron job
echo "setting a cron job to switch theme at specified time"
crontab -l >tmp.txt
echo -e "#cronjob for changing theme \n* * * * *    ~/.kdeAutoThemeSwitch/theme.sh" >>tmp.txt
crontab tmp.txt
rm tmp.txt
