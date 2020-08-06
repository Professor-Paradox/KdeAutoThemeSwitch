import cleanedData as CD


def get_Look_And_Feel():
    """
    get_Look_And_Feel checks plasma directories for look and feel themes

    Returns:
        (list): list of look and feel themes
    """
    UserThemes = CD.files_In_Path("/.local/share/plasma/look-and-feel/")
    SystemThemes = CD.files_In_Path("/usr/share/plasma/look-and-feel/")
    editedUserList = CD.filter_List_Values(
        ".json", listOfThemes=UserThemes, deleteWord=True
    )
    editedSystemList = CD.filter_List_Values(".desktop", listOfThemes=SystemThemes)
    return CD.combine_Lists(editedUserList, editedSystemList)


def get_Plasma_Themes():
    """
    get_Plasma_Themes checks plasma directories for themes

    Returns:
        (list): list of plasma themes
    """
    UserThemes = CD.files_In_Path("/.local/share/plasma/desktoptheme/")
    SystemThemes = CD.files_In_Path("/usr/share/plasma/desktoptheme/")
    editedUserList = CD.filter_List_Values(
        ".json", listOfThemes=UserThemes, deleteWord=True
    )
    editedSystemList = CD.filter_List_Values(listOfThemes=SystemThemes)
    return CD.combine_Lists(editedUserList, editedSystemList)


def get_Application_Styles():
    """
    get_Application_Styles checks plugins directories for styles

    Returns:
        (list): list of application styles
    """
    # No user application styles are available
    SystemThemes = CD.files_In_Path("/usr/lib/x86_64-linux-gnu/qt5/plugins/styles/")
    editedSystemList = CD.filter_List_Values(".so", listOfThemes=SystemThemes)
    # kde converts libkvantum to kvantum when applied from settings.we are Changing manually here
    for i in editedSystemList:
        if i == "libkvantum":
            editedSystemList.remove(i)
            editedSystemList.append("kvantum")
    return CD.combine_Lists([], editedSystemList)


def get_Window_Decorations():
    """
    get_Window_Decorations checks aurorae directories for themes

    Returns:
        (list): list of window decorations
    """
    UserThemes = CD.files_In_Path("/.local/share/aurorae/themes/")
    SystemThemes = CD.files_In_Path("/usr/share/kwin/decorations/")
    editedUserList = CD.filter_List_Values(listOfThemes=UserThemes)
    editedSystemList = CD.filter_List_Values(listOfThemes=SystemThemes)
    return CD.combine_Lists(editedUserList, editedSystemList)


def get_Gtk_Themes():
    """
    get_Gtk_Themes checks theme directories for gtk themes

    Returns:
        (list): list of gtk themes
    """
    UserThemes = CD.files_In_Path("/.themes/")
    # /usr/share/themes will have plasma,gtk,kvantum themes
    # hard coding only system gtk themes
    SystemThemes = ["Breeze", "Breeze-Dark", "Emacs"]
    editedUserList = CD.filter_List_Values(listOfThemes=UserThemes)
    editedSystemList = CD.filter_List_Values(listOfThemes=SystemThemes)
    return CD.combine_Lists(editedUserList, editedSystemList)


def get_Color_Schemes():
    """
    get_Color_Schemes checks color scheme directories for color scheme

    Returns:
        (list): list of color schemes
    """
    UserThemes = CD.files_In_Path("/.local/share/color-schemes/color-schemes/")
    SystemThemes = CD.files_In_Path("/usr/share/color-schemes/")
    editedUserList = CD.filter_List_Values(".colors", listOfThemes=UserThemes)
    editedSystemList = CD.filter_List_Values(".colors", listOfThemes=SystemThemes)
    return CD.combine_Lists(editedUserList, editedSystemList)


def get_Icons():
    """
    get_Icons checks directories for icons

    Returns:
        (list): list of icons
    """
    UserThemes = CD.files_In_Path("/.local/share/icons/")
    SystemThemes = CD.files_In_Path("/usr/share/icons/")
    editedUserList = CD.filter_List_Values(
        ".png", listOfThemes=UserThemes, deleteWord=True
    )
    editedSystemList = CD.filter_List_Values(
        ".png", listOfThemes=SystemThemes, deleteWord=True
    )
    return CD.combine_Lists(editedUserList, editedSystemList)


def get_Kvantums():
    """
    get_Kvantums checks config directories for kvantum themes

    Returns:
        (list): list of kvantum themes
    """
    UserThemes = CD.files_In_Path("/.config/Kvantum/")
    SystemThemes = CD.files_In_Path("/usr/share/Kvantum")
    editedUserList = CD.filter_List_Values("#", ".kvconfig", listOfThemes=UserThemes)
    # some kvantum themes will have these extensions
    editedSystemList = CD.filter_List_Values(listOfThemes=SystemThemes)
    return CD.combine_Lists(editedUserList, editedSystemList)


# print(get_Look_And_Feel())
# print(get_Plasma_Themes())
# print(get_Application_Styles())
# print(get_Window_Decorations())
# print(get_Gtk_Themes())
# print(get_Color_Schemes())
# print(get_Icons())
# print(get_Kvantums())
