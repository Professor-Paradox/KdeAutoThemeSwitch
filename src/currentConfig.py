"""
    Gets Current System theme configuration using Kde commands
    """
import subprocess, re
import cleanedData as CD

def test():
    print('hello')

def get_Look_And_Feel():

    # lookandfeel
    x = subprocess.check_output(
        "kreadconfig5 --file ~/.config/kdeglobals --group KDE --key LookAndFeelPackage",
        shell=True,
    )
    return CD.clean_Shell_Result(str(x))


def get_Plasma_Themes():

    # plasmatheme
    x = subprocess.check_output(
        "kreadconfig5 --file ~/.config/plasmarc --group Theme --key name", shell=True
    )
    return CD.clean_Shell_Result(str(x))


def get_Application_Styles():
    x = subprocess.check_output(
        "kreadconfig5 --file ~/.config/kdeglobals --group KDE --key widgetStyle",
        shell=True,
    )
    return CD.clean_Shell_Result(str(x))


def get_Window_Decorations():
    x = subprocess.check_output(
        "kreadconfig5 --file ~/.config/kwinrc --group org.kde.kdecoration2 --key theme",
        shell=True,
    )
    result = CD.clean_Shell_Result(str(x))
    text = "__aurorae__svg__"
    # removes the text from result,for easy display of options
    return CD.remove_text(result, text, pattern=f"{text}(.*)$")


def get_Gtk_Themes():

    # gtk theme
    x = subprocess.check_output(
        "kreadconfig5  --file ~/.config/gtk-3.0/settings.ini --group Settings --key gtk-theme-name",
        shell=True,
    )
    return CD.clean_Shell_Result(str(x))


def get_Color_Schemes():

    # color scheme
    x = subprocess.check_output(
        "kreadconfig5  --file ~/.config/kdeglobals --group General --key ColorScheme",
        shell=True,
    )
    return CD.clean_Shell_Result(str(x))


def get_Icons():

    # icons
    x = subprocess.check_output(
        "kreadconfig5 --file ~/.config/kdeglobals --group Icons --key Theme", shell=True
    )
    return CD.clean_Shell_Result(str(x))


def get_Kvantums():

    # kvantumtheme
    x = subprocess.check_output(
        "kreadconfig5 --file ~/.config/Kvantum/kvantum.kvconfig --group General --key theme",
        shell=True,
    )
    result = CD.clean_Shell_Result(str(x))
    text = "#"
    # removes the text from result,for easy display of options
    return CD.remove_text(result, text, pattern=f"(.*){text}$")


# print(get_Look_And_Feel())
# print(get_Plasma_Themes())
# print(get_Application_Styles())
# print(get_Window_Decorations())
# print(get_Gtk_Themes())
# print(get_Color_Schemes())
# print(get_Icons())
# print(get_Kvantums())
