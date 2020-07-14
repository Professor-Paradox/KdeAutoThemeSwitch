py qt is a gui tool built on top of python,this is a interface for exisiting qt framework,their are multiple languages that can used to create gui with qt,they are java,python,C++(qt is written in C++),C,R.
we use qt designer software to create ui,with customization then use the python file to create logic.

in python we create a method/function 
Syntax:
def functionname(parameters):
   code(tab is how we create code blocks.)


designer
env/lib/python3.8/site-packages/pyqt5_tools/Qt/bin/designer

we design our ui in qt designer then run the code with python interpreter to apply logic to it. 
convert ui file to python file
pyuic5 –x filename.ui –o filename.py



combo boxes:
drop down lists with options to select are combo boxes.



method to hide/show widgets,
def disableOptions(self,widget):
   widget.setDisabled(True)

calling this method
self.disableOptions(self.checkBox)

Grey out checkboxes,drop downs
Default all grey out
check box on disable grey out


create methods for each layout
then trigger them if checkbox is pressed



## Requirements.:
Switch kde theme from light to dark on specified time.
Can do it manually,but have to change a lot.
instead create a script/program that will do it automatically.

Change theme,icons,color,windows etc.,
Can do it with bash script(done),should optimize it .

Take user input from command line,and save it to a file for data about theme switching.

## Task 
Create a Gui to take input easily.

1. Create a barebones Gui.done with pyqt
2. link logic to make it adapt to user input.
3. take system data and display for selection 
4. save the data on completion
5. switch to scripts(existing),and close the operation.

### Requirements
Pyqt
python
bash
uml

### user view
user will double click a single bash file that will install all python dependencies then run the python script.
show the gui,fetch system details,then ask for user to select input.
on save button press,will save in a txt file.then create  a hidden directory and set up a cron job.
then display confirmation message and close the python file,
in future if need to change settings,will run the python script again will update their details,done.

#### classes methods
a python ui file,that shows ui.
a python file that will take ui,and work on ui elements,
a python file that will take data and put it in the ui elements.
a bash script that will work on the data given to switch theme.
a confirmation dialog.

methods.
Ui methods,
default checkbox off,all drop down/comboboxes off,on select of a checkbox will trigger their relative comboboxes.
**enableWidget**(),**disableWidget**
on checkbox trigger,will fetch data from system,show relavent data as drop down list.
**setDroplist**()
with current detail as default.
**currentDefaultList**()
save button save the data to a file.
**saveConfig**()
set time by default and save,if user changes fetch it and save.
**getLightThemeTime**(),**getDarkThemeTime**()
trigger the file saved,script execution done popups.
**showProcessDone**()
stop the process.

UML





