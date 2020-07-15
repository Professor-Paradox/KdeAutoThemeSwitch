from plasma import Ui_MainWindow
import sys
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

      # linking relevant grid elements with checkbox
      self.ui.checkBox.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout))
      self.ui.checkBox2.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout2))
      self.ui.checkBox3.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout3))
      self.ui.checkBox4.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout4))
      self.ui.checkBox5.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout5))
      self.ui.checkBox6.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout6))
      self.ui.checkBox7.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout7))
      self.ui.checkBox8.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout8))
      self.ui.checkBox9.toggled.connect(lambda: self.toggleWidget(self.ui.gridLayout9))

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
   def toggleWidget(self,gridLayout):
      # taking the gridlayout as innerlayout and passing them to enablewidgets which will switch them on/off
      if (self.ui.checkBox.isChecked() == True):
         # switches on elements
         self.enableWidgets(gridLayout,True)  

      if (self.ui.checkBox.isChecked() == False):
         # switches off elements
         self.enableWidgets(gridLayout)

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
         exec(f"self.ui.{gridLayout.itemAt(i).widget().objectName()}.setEnabled(isEnable)")
      

# main method used to call when file is being executed.
def main():
   app = QtWidgets.QApplication(sys.argv)
   customWindow = MyWindow()
   customWindow.show()
   sys.exit(app.exec_())

# calls main when executing this file
if __name__ == "__main__":
   main()


# TODO function to fetch data from SystemData
# TODO function to push data to drop downs
# TODO function to check the current theme data being used,from the kde files in theme.sh file
# TODO function to create a file with user given data,from save button.
