from plasma import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QEvent
import SystemData as SD
import currentConfig as CC

"""Adds functionality to existing Ui"""


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # disable all widgets by default.
        self.disableAll()
        self.ui.dark.setEnabled(False)

        # calls given function on button Click(UI),by default doesn't accept any parameters.
        # we can use lambda to pass extra parameters,below line is an example
        # linking relevant grid elements with checkbox
        self.ui.checkBox.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox, self.ui.gridLayout, CC.get_Look_And_Feel
            )
        )
        self.ui.checkBox2.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox2, self.ui.gridLayout2, CC.get_Plasma_Themes
            )
        )
        self.ui.checkBox3.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox3, self.ui.gridLayout3, CC.get_Application_Styles
            )
        )
        self.ui.checkBox4.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox4, self.ui.gridLayout4, CC.get_Window_Decorations
            )
        )
        self.ui.checkBox5.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox5, self.ui.gridLayout5, CC.get_Gtk_Themes
            )
        )
        self.ui.checkBox6.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox6, self.ui.gridLayout6, CC.get_Color_Schemes
            )
        )
        self.ui.checkBox7.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox7, self.ui.gridLayout7, CC.get_Icons
            )
        )
        self.ui.checkBox8.toggled.connect(
            lambda: self.toggleWidget(
                self.ui.checkBox8, self.ui.gridLayout8, CC.get_Kvantums
            )
        )

        # self.ui.lightTheme.installEventFilter(self)

        self.ui.savePushButton.clicked.connect(self.getDataOnSave)

    # disable all widgets
    def disableAll(self):
        """
        will disable all grid layouts
        """
        self.enable_Widgets(self.ui.gridLayout)
        self.enable_Widgets(self.ui.gridLayout2)
        self.enable_Widgets(self.ui.gridLayout3)
        self.enable_Widgets(self.ui.gridLayout4)
        self.enable_Widgets(self.ui.gridLayout5)
        self.enable_Widgets(self.ui.gridLayout6)
        self.enable_Widgets(self.ui.gridLayout7)
        self.enable_Widgets(self.ui.gridLayout8)
        self.ui.savePushButton.setEnabled(False)

    # when clicked switches on all elements inside the box.
    def toggleWidget(self, checkBoxValue, gridLayout, themeName):
        """
        makes given theme menu interactive

        Args:

            checkBoxValue (QCheckBox): toggle the gridLayout
            gridLayout (QGridLayout): items in this layout are triggered
            themeName (function): [theme name as function to call on demand]
        """
        # using given checkbox to trigger the given gridlayout
        # passing them to enable_widgets which will switch them on/off
        if checkBoxValue.isChecked() == True:
            # switches on elements

            self.enable_Widgets(gridLayout, switch=True)
            # appends list to dropdown only once
            self.current_Theme_To_Dropdown(gridLayout, themeName())
        else:
            # switches off elements
            self.enable_Widgets(gridLayout)
            self.themes_To_Dropdown(gridLayout, themeName(), True)

    # this function takes a gridlayout to enable/disable widgets in it.
    def enable_Widgets(self, gridLayout, switch=False):
        # don't use exec,it works better for single lines,for blocks of code can raise errors.
        # use another way,like storing data,inside a list,dictionary.then using it.
        # using exec raises an error,string class has a count function which conflicts with widget functions.
        # getting the widgets inside the gridlayout,then enabling/disabling them.
        for i in range(gridLayout.count()):
            # objectName gives widget name declared in code.
            # here exec is used to execute on a edited string,raises no errors
            # code in the brackets gets the widget name,which would be enabled
            exec(
                f"self.ui.{gridLayout.itemAt(i).widget().objectName()}.setEnabled(switch)"
            )

        self.ui.savePushButton.setEnabled(True)
        # fetching data from SystemData class,passing it to comboBox items.

    def themes_To_Dropdown(self, gridValue, themeData, clearComboBox=False):
        """[summary]

        Parameters
        ----------
        gridValue : [type]
            [description]
        themeData : [type]
            [description]
        """
        # gives back names of widgets
        # gives back widget object
        lightDropDown = gridValue.itemAt(1).widget()
        darkDropDown = gridValue.itemAt(0).widget()
        if clearComboBox == True:
            lightDropDown.clear()
            darkDropDown.clear()
        else:
            lightDropDown.addItems(themeData)
            darkDropDown.addItems(themeData)

    def values_To_Dropdown(self, gridValue, themeData):
        lightDropDown = gridValue.itemAt(1).widget()
        darkDropDown = gridValue.itemAt(0).widget()

        lightDropDown.addItem(themeData)
        darkDropDown.addItem(themeData)

    def current_Theme_To_Dropdown(self, gridValue, themeData):
        self.values_To_Dropdown(gridValue, themeData)

    # saving selected data to a new file
    def saveDataToFile(self, dict):
        print("saving data to file")
        with open("userSelection.txt", "w") as f:
            # getting individual key and value to append to file
            for i in dict:
                f.write(f"{i}=")
                f.write(f"'{dict[i]}'\n")

    # gets options selected by the user for each category
    def getDataOnSave(self):
        LAF = self.ui.lightTheme.currentText()
        PL = self.ui.lightTheme2.currentText()
        AP = self.ui.lightTheme3.currentText()
        WD = self.ui.lightTheme4.currentText()
        G = self.ui.lightTheme5.currentText()
        CS = self.ui.lightTheme6.currentText()
        I = self.ui.lightTheme7.currentText()
        K = self.ui.lightTheme8.currentText()
        DLAF = self.ui.darkTheme.currentText()
        DPL = self.ui.darkTheme2.currentText()
        DAP = self.ui.darkTheme3.currentText()
        DWD = self.ui.darkTheme4.currentText()
        DG = self.ui.darkTheme5.currentText()
        DCS = self.ui.darkTheme6.currentText()
        DI = self.ui.darkTheme7.currentText()
        DK = self.ui.darkTheme8.currentText()
        lightThemeTime = self.ui.lightThemeTime.time().hour()
        darkThemeTime = self.ui.darkThemeTime.time().hour()
        selectedOptionsList = {
            "LAF": LAF,
            "DLAF": DLAF,
            "PL": PL,
            "DPL": DPL,
            "AP": AP,
            "DAP": DAP,
            "WD": WD,
            "DWD": DWD,
            "G": G,
            "DG": DG,
            "CS": CS,
            "DCS": DCS,
            "I": I,
            "DI": DI,
            "K": K,
            "DK": DK,
            "currentTheme": "light",
            "lightThemeTime": lightThemeTime,
            "darkThemeTime": darkThemeTime,
        }
        self.saveDataToFile(selectedOptionsList)




    # def eventFilter(self,target,event):
    #     if target == self.ui.lightTheme and event.type() == QEvent.MouseButtonPress:
    #         print("Button press")
    #         self.fillComboBox()

    #     return False

    # def fillComboBox(self):
    #     self.ui.lightTheme.clear()
    #     self.ui.lightTheme.addItem('foo')
    #     self.ui.lightTheme.addItem('bar')










# main method used to call when file is being executed.
def main():
    app = QtWidgets.QApplication(sys.argv)
    customWindow = MyWindow()
    customWindow.show()
    sys.exit(app.exec_())


# calls main when executing this file
if __name__ == "__main__":
    main()

# TODO Learn clean coding principals and a guide
