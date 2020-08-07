import os, re

""" homeDir: current User home directory """
homeDir = os.path.expanduser("~")


def filter_List_Values(*regexValues, listOfThemes, deleteWord=False):
    """
    filter_List_Values removes specified lines or words in a list

    Args:
        regexValues (list): list of regex's
        listOfThemes (list): a list of text values
        deleteWord (bool, optional):
            True: deletes entire value with regex match
                Ex: test.py.so will be ""
            False(default): deletes only the regex value
                Ex: test.py.so will be "test.py"

    Returns:
        list: string list with no suffixes and empty values
    """
    # Keyword arguments should be after positional arguments,so took all the positions at the beginning,making all other as keyword arguments
    tempList = []
    # themesList=[]
    for theme in listOfThemes:
        if deleteWord == True:
            # substituting the theme value with an empty string
            for regex in regexValues:
                theme = re.sub(f".*{regex}$", "", theme)

        if deleteWord == False:
            # removing the specified regex string from theme value
            for regex in regexValues:
                theme = re.sub(f"{regex}$", "", theme)
        tempList.append(theme)

    # removing empty string from tempList
    return list(filter(None, tempList))


def combine_Lists(userData, systemData):
    """
    combine_Lists combines multiple lists

    Args:
        userData (list): user themes in a list
        systemData (list): system themes in a list

    Returns:
        (list): sorted list of theme names
    """
    # sorts list case insenstively
    return sorted(userData + systemData, key=str.lower)


def files_In_Path(dirPath):
    """
    dir_Files gets all the folders in a given path

    Parameters:
        dirPath:(string): path of a directory/folder containing themes

    Returns:
        (list) : list of all folder names in given path
    """
    # gets folders in user path
    if "/." in dirPath:
        x = os.listdir(f"{homeDir}{dirPath}")
    else:
        # gets folders in system path
        x = os.listdir(f"{dirPath}")
    return x


def clean_Shell_Result(text):
    """
    clean_Shell_Result removes starting and trailing patterns

    Args:
        text (str): text to remove pattern

    Returns:
        str: cleaned text
    """
    # pattern between () group can be extracted
    return re.search("b'(.*)\\\\n'", text).group(1)


def remove_text(result, text, pattern):
    """
    remove_text removes pattern from text

    Args:
        result (str): string to apply pattern
        text (str): string used in pattern 
        pattern (regex): regex pattern

    Returns:
        str: cleaned result using pattern
    """
    if text in result:
        return re.search(pattern, result).group(1)
    else:
        return result
