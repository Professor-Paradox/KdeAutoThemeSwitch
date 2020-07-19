from plasma import Ui_MainWindow
import sys
import SystemData as SD
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout

class MyWindow(QtWidgets.QMainWindow):
   def __init__(self):
      super(MyWindow, self).__init__()
      self.ui = Ui_MainWindow()
      self.ui.setupUi(self)
      # disable all widgets by default.
      self.disableAll()
      # self.toggleWidget()
      self.ui.dark.setEnabled(False)

      # calls given function on button Click(UI),by default doesn't accept any parameters.
      # we can use lambda to pass extra parameters,below line is an example
      # self.ui.checkBox.toggled.connect(lambda: self.toggleWidget("hello"))
      # print(SystemData.userDirFiles('/.local/share/plasma/look-and-feel/'))
      
      # linking relevant grid elements with checkbox
      self.ui.checkBox.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox,self.ui.gridLayout,SD.lookAndFeel))
      self.ui.checkBox2.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox2,self.ui.gridLayout2,SD.plasmaTheme))
      self.ui.checkBox3.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox3,self.ui.gridLayout3,SD.applicationStyles))
      self.ui.checkBox4.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox4,self.ui.gridLayout4,SD.windowDecorations))
      self.ui.checkBox5.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox5,self.ui.gridLayout5,SD.gtkTheme))
      self.ui.checkBox6.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox6,self.ui.gridLayout6,SD.colorScheme))
      self.ui.checkBox7.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox7,self.ui.gridLayout7,SD.icons))
      self.ui.checkBox8.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox8,self.ui.gridLayout8,SD.kvantum))
      self.ui.checkBox9.toggled.connect(
         lambda: self.toggleWidget(self.ui.checkBox9,self.ui.gridLayout9,SD.splashScreen))
      self.ui.savePushButton.clicked.connect(self.getDataOnSave)
      # x=SD.getCurrentThemeInfo('/.config/gtk-3.0/settings.ini','Settings','gtk-cursor-theme-name')
      # print(x)
      # print(SD.getCurrentThemeInfo('/.config/kdeglobals','KDE','LookAndFeelPackage'))
      # self.dataToBox()


   # disable all widgets
   def disableAll(self):
      self.enableWidgets(self.ui.gridLayout)
      self.enableWidgets(self.ui.gridLayout2)
      self.enableWidgets(self.ui.gridLayout3)
      self.enableWidgets(self.ui.gridLayout4)
      self.enableWidgets(self.ui.gridLayout5)
      self.enableWidgets(self.ui.gridLayout6)
      self.enableWidgets(self.ui.gridLayout7)
      self.enableWidgets(self.ui.gridLayout8)
      self.enableWidgets(self.ui.gridLayout9)
      self.ui.savePushButton.setEnabled(False)

   # when clicked switches on all elements inside the box.
   def toggleWidget(self,checkBoxValue,gridLayout,themeName):
      # using given checkbox to trigger the given gridlayout
      # passing them to enablewidgets which will switch them on/off
      if (checkBoxValue.isChecked() == True):
         # switches on elements
         self.enableWidgets(gridLayout,True)  
         
         # self.dataToBox(themeName)
         self.dataToBox(gridLayout,SD.getSystemData(themeName))
      else:
      # if (self.ui.checkBox.isChecked() == False):
         # switches off elements
         self.enableWidgets(gridLayout)
         print("bye")

   # this function takes a gridlayout to enable/disable widgets in it.
   def enableWidgets(self,gridLayout,isEnable=False):
      # don't use exec,it works better for single lines,for blocks of code can raise errors.
      # use another way,like storing data,inside a list,dictionary.then using it.  
      # using exec raises an error,string class has a count function which conflicts with widget functions. 
      # value=gridLayout.count()
      # print(value)
      # getting the widgets inside the gridlayout,then enabling/disabling them.
      for i in range(gridLayout.count()):
         # objectName gives widget name declared in code.
         temp=gridLayout.itemAt(i).widget().objectName()
         # if temp == (f"lightTheme{i}") or temp == (f"darkTheme{i}"):
         # print(temp)
         # here exec is used to execute on a edited string,raises no errors
         # code in the brackets gets the widget name,which would be enabled
         exec(f"self.ui.{gridLayout.itemAt(i).widget().objectName()}.setEnabled(isEnable)")
      
      # enables save button on a checkbox activation
      self.ui.savePushButton.setEnabled(True)
   
         # fetching data from SystemData class,passing it to comboBox items.
   def dataToBox(self,gridValue,themeData):
      print("hello")
      # defaultValue=SD.getLookAndFeel()
      # gives back names of widgets
      # lightDropDown=(gridValue.itemAt(1).widget().objectName())
      # gives back widget object
      lightDropDown=(gridValue.itemAt(1).widget())
      darkDropDown=(gridValue.itemAt(0).widget())
      # print(lightDropDown,darkDropDown)
      lightDropDown.addItems(themeData)
      darkDropDown.addItems(themeData)

   # saving selected data to a new file
   def saveDataToFile(self,dict):
      print("saving data to file")
      with open('userSelection.txt','w') as f:
         # getting individual key and value to append to file
         for i in dict:
            f.write(f'{i}=')
            f.write(f"'{dict[i]}'\n")
   # gets options selected by the user for each category
   def getDataOnSave(self):
      # selectedOptionsList=[
      LAF=self.ui.lightTheme.currentText()
      PL=self.ui.lightTheme2.currentText()
      AP=self.ui.lightTheme3.currentText()
      WD=self.ui.lightTheme4.currentText()
      G=self.ui.lightTheme5.currentText()
      CS=self.ui.lightTheme6.currentText()
      I=self.ui.lightTheme7.currentText()
      K=self.ui.lightTheme8.currentText()
      SP=self.ui.lightTheme9.currentText()
      # C=
      # GC=
      DLAF=self.ui.darkTheme.currentText()
      DPL=self.ui.darkTheme2.currentText()
      DAP=self.ui.darkTheme3.currentText()
      DWD=self.ui.darkTheme4.currentText()
      DG=self.ui.darkTheme5.currentText()
      DCS=self.ui.darkTheme6.currentText()
      DI=self.ui.darkTheme7.currentText()
      DK=self.ui.darkTheme8.currentText()
      DSP=self.ui.darkTheme9.currentText()
      lightThemeTime=self.ui.lightThemeTime.time().hour()
      darkThemeTime=self.ui.darkThemeTime.time().hour()
      selectedOptionsList={'LAF':LAF,
      'PL':PL,
      'AP':AP,
      'WD':WD,
      'G':G,
      'CS':CS,
      'I':I,
      'K':K,
      'SP':SP,
      'DLAF':DLAF,
      'DPL':DPL,
      'DAP':DAP,
      'DWD':DWD,
      'DG':DG,
      'DCS':DCS,
      'DI':DI,
      'DK':DK,
      'DSP':DSP,
      'currentTheme':'light',
      'lightThemeTime':lightThemeTime,
      'darkThemeTime':darkThemeTime}
      # print(selectedOptionsList)  # ]
      self.saveDataToFile(selectedOptionsList)
      # for i in selectedOptionsList:
      #  self.saveDataToFile(i)
         
   

# main method used to call when file is being executed.
def main():
   app = QtWidgets.QApplication(sys.argv)
   customWindow = MyWindow()
   customWindow.show()
   sys.exit(app.exec_())

# calls main when executing this file
if __name__ == "__main__":
   main()


# TODO function to create a file with user given data,from save button.



