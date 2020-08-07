from DesignerUi import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import QEvent
import ThemeData as TD
import CurrentConfig as CC

"""Adds functionality to existing Ui"""


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        """
        __init__ initializes the Ui object and sets below methods for use on demand
        """
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # disabling all widgets by default.
        self.disableAll()

        # linking relevant grid,layout,theme methods/objects
        self.ui.checkBox1.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox1, self.ui.gridLayout1, CC.get_Look_And_Feel
            )
        )
        self.ui.checkBox2.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox2, self.ui.gridLayout2, CC.get_Plasma_Themes
            )
        )
        self.ui.checkBox3.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox3, self.ui.gridLayout3, CC.get_Application_Styles
            )
        )
        self.ui.checkBox4.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox4, self.ui.gridLayout4, CC.get_Window_Decorations
            )
        )
        self.ui.checkBox5.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox5, self.ui.gridLayout5, CC.get_Gtk_Themes
            )
        )
        self.ui.checkBox6.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox6, self.ui.gridLayout6, CC.get_Color_Schemes
            )
        )
        self.ui.checkBox7.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox7, self.ui.gridLayout7, CC.get_Icons
            )
        )
        self.ui.checkBox8.toggled.connect(
            lambda: self.toggle_Widgets(
                self.ui.checkBox8, self.ui.gridLayout8, CC.get_Kvantums
            )
        )

        # setting eventhandlers to all the dropdown menus
        self.set_Dropdown_Events()
        self.ui.savePushButton.clicked.connect(self.on_Save_Button_Clicked)

    def disableAll(self):
        """
        disables all buttons and layouts
        """
        self.enable_Widgets(self.ui.gridLayout1)
        self.enable_Widgets(self.ui.gridLayout2)
        self.enable_Widgets(self.ui.gridLayout3)
        self.enable_Widgets(self.ui.gridLayout4)
        self.enable_Widgets(self.ui.gridLayout5)
        self.enable_Widgets(self.ui.gridLayout6)
        self.enable_Widgets(self.ui.gridLayout7)
        self.enable_Widgets(self.ui.gridLayout8)
        self.ui.savePushButton.setEnabled(False)

    def toggle_Widgets(self, checkBoxValue, gridLayout, themeName):
        """
        toggle_Widgets makes the layouts interactable on clicking relevant checkbox

        Args:
            checkBoxValue (QCheckBox): toggles the gridLayout
            gridLayout (QGridLayout): layout to be interactable
            themeName (function): function reference to get list for drop down
        """
        tempThemeData = themeName()
        if checkBoxValue.isChecked() == True:
            # appending current theme to dropdown on checkbox click
            self.enable_Widgets(gridLayout, switch=True)
            self.themes_To_Dropdown(gridLayout, tempThemeData, clearComboBox=False)

        else:
            # disables and clears widgets
            self.enable_Widgets(gridLayout, switch=False)
            self.themes_To_Dropdown(gridLayout, tempThemeData, clearComboBox=True)

    def enable_Widgets(self, gridLayout, switch=False):
        """
        enable_Widgets enables all the widgets inside a layout

        Args:
            gridLayout (QGridLayout): widgets in this layout are enabled
            switch (bool, optional): 
                True: Enables widgets to use
                False(Default): Disables widgets
        """
        # selecting individual widgets in gridlayout
        for i in range(gridLayout.count()):
            """
                itemAt: gets single widget/layout from a layout
                widget: gets the widget from layout at itemAt
                objectName: returns the widget name used in our code
            """
            # formatting a string to contain a single Q widget item,then enabling them
            exec(
                f"self.ui.{gridLayout.itemAt(i).widget().objectName()}.setEnabled(switch)"
            )

        self.ui.savePushButton.setEnabled(True)

    def themes_To_Dropdown(self, gridLayout, themeData, clearComboBox=False):
        """
        themes_To_Dropdown adds themes to dropdown menu

        Args:
            gridLayout (QGridLayout): selects dropdowns present in layout
            themeData (themes): themes to insert to dropdowns
            clearComboBox (bool, optional): 
                True clears dropdowns.
                False(default) doesn't clear dropdowns
        """
        # selects widget objects inside a layout
        lightDropDown = gridLayout.itemAt(1).widget()
        darkDropDown = gridLayout.itemAt(0).widget()
        if clearComboBox == True:
            lightDropDown.clear()
            darkDropDown.clear()
        else:
            # appends single item or a list of items to dropdowns
            if type(themeData) == list:
                lightDropDown.addItems(themeData)
                darkDropDown.addItems(themeData)
            else:
                lightDropDown.addItem(themeData)
                darkDropDown.addItem(themeData)

    def on_Save_Button_Clicked(self):
        """
        on_Save_Button_Clicked when save button is clicked,saves selected items in drop downs to a file
        """
        LAF = self.ui.lightTheme1.currentText()
        PL = self.ui.lightTheme2.currentText()
        AP = self.ui.lightTheme3.currentText()
        WD = self.ui.lightTheme4.currentText()
        G = self.ui.lightTheme5.currentText()
        CS = self.ui.lightTheme6.currentText()
        I = self.ui.lightTheme7.currentText()
        K = self.ui.lightTheme8.currentText()
        DLAF = self.ui.darkTheme1.currentText()
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
            "APS": AP,
            "DAPS": DAP,
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
        self.write_Dict_To_File(selectedOptionsList)

    def write_Dict_To_File(self, dict):
        """
        write_Dict_To_File writes individual key value pairs to a file

        Args:
            dict (dictionary): a dictionary of theme categories and theme names
        """
        with open("userSelection.txt", "w") as f:
            for i in dict:
                f.write(f"{i}='{dict[i]}'\n")

    def set_Dropdown_Events(self):
        """
        set_Dropdown_Events installs event filter to each combobox
        """
        numberOfThemeCategories = 8
        for i in range(numberOfThemeCategories):
            # hard coding theme objects
            exec(f"self.ui.darkTheme{i+1}.installEventFilter(self)")
            exec(f"self.ui.lightTheme{i+1}.installEventFilter(self)")

    def eventFilter(self, target, event):
        """
        eventFilter makes dropdown menus function callable

        Returns:
            fills dropdown menus with theme names only when checkbox is selected
        """
        if (
            target == self.ui.lightTheme1
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox1.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout1, TD.get_Look_And_Feel())

        if (
            target == self.ui.lightTheme2
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox2.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout2, TD.get_Plasma_Themes())

        if (
            target == self.ui.lightTheme3
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox3.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout3, TD.get_Application_Styles())

        if (
            target == self.ui.lightTheme4
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox4.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout4, TD.get_Window_Decorations())

        if (
            target == self.ui.lightTheme5
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox5.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout5, TD.get_Gtk_Themes())

        if (
            target == self.ui.lightTheme6
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox6.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout6, TD.get_Color_Schemes())

        if (
            target == self.ui.lightTheme7
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox7.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout7, TD.get_Icons())

        if (
            target == self.ui.lightTheme8
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox8.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout8, TD.get_Kvantums())

        if (
            target == self.ui.darkTheme1
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox1.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout1, TD.get_Look_And_Feel())

        if (
            target == self.ui.darkTheme2
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox2.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout2, TD.get_Plasma_Themes())

        if (
            target == self.ui.darkTheme3
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox3.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout3, TD.get_Application_Styles())

        if (
            target == self.ui.darkTheme4
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox4.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout4, TD.get_Window_Decorations())

        if (
            target == self.ui.darkTheme5
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox5.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout5, TD.get_Gtk_Themes())

        if (
            target == self.ui.darkTheme6
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox6.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout6, TD.get_Color_Schemes())

        if (
            target == self.ui.darkTheme7
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox7.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout7, TD.get_Icons())

        if (
            target == self.ui.darkTheme8
            and event.type() == QEvent.MouseButtonPress
            and self.ui.checkBox8.isChecked() == True
        ):
            target.clear()
            self.themes_To_Dropdown(self.ui.gridLayout8, TD.get_Kvantums())

        return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    customWindow = MyWindow()
    customWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
