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
      x=SD.getCurrentThemeInfo('/.config/gtk-3.0/settings.ini','Settings','gtk-cursor-theme-name')
      print(x)


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

   # when clicked switches on all elements inside the box.
   def toggleWidget(self,checkBoxValue,gridLayout,themeName):
      # using given checkbox to trigger the given gridlayout
      # passing them to enablewidgets which will switch them on/off
      if (checkBoxValue.isChecked() == True):
         # switches on elements
         self.enableWidgets(gridLayout,True)  
         x=SD.getSystemData(themeName)
         print(x)
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
         # temp=gridLayout.itemAt(i).widget().objectName()
         # print(temp)
         # here exec is used to execute on a edited string,raises no errors
         # code in the brackets gets the widget name,which would be enabled
         exec(f"self.ui.{gridLayout.itemAt(i).widget().objectName()}.setEnabled(isEnable)")
         
   
         # fetching data from SystemData class,passing it to comboBoxe items.


      

# main method used to call when file is being executed.
def main():
   app = QtWidgets.QApplication(sys.argv)
   customWindow = MyWindow()
   customWindow.show()
   sys.exit(app.exec_())

# calls main when executing this file
if __name__ == "__main__":
   main()

# lookAndFeel
# print(SD.getCurrentThemeInfo('/.config/kdeglobals','KDE','LookAndFeelPackage'))
# plasmaTheme
# print(SD.getCurrentThemeInfo('/.config/plasmarc','Theme','name'))
# applicationStyleEdit
# print(SD.getCurrentThemeInfo('/.config/kdeglobals','org.kde.kdecoration2','theme'))
# windowDecoration
# print(SD.getCurrentThemeInfo('/.config/kwinrc','org.kde.kdecoration2','theme'))
# gtkTheme
# print(SD.getCurrentThemeInfo('/.config/gtk-3.0/settings.ini','Settings','gtk-theme-name'))
# colorScheme
# print(SD.getCurrentThemeInfo('/.config/kdeglobals','General','ColorScheme'))
# icons
# print(SD.getCurrentThemeInfo('/.config/kdeglobals','Icons','Theme'))
# cursor
# print(SD.getCurrentThemeInfo('/.config/kcminputrc','Mouse','cursorTheme'))
# gtkCursor
# print(SD.getCurrentThemeInfo('/.config/gtk-3.0/settings.ini','Settings','gtk-cursor-theme-name'))
# kvantumTheme
# print(SD.getCurrentThemeInfo('/.config/Kvantum/kvantum.kvconfig','General','theme'))
# splashScreen
# print(SD.getCurrentThemeInfo('/.config/ksplashrc','KSplash','Theme'))
# alt-tab theme
# print(SD.+getCurrentThemeInfo('/.config/kwinrc','TabBox','LayoutName'))
# TODO function to push data to drop downs
# TODO function to create a file with user given data,from save button.
# TODO check rescue time completely,sync everything and create a list of options to create.