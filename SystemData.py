import os,re

homeDir=os.path.expanduser("~")
testfile=open("test.txt","a+")
def userDirFiles(userPath):
   x = os.listdir(f'{homeDir}{userPath}')
   x.sort()
   return x

def systemDirFiles(systemPath):
   x = os.listdir(f'{systemPath}')
   x.sort()
   return x

def append(alist):
   for i in alist:
      testfile.write(f"{i}\n")

      
# gtktheme,kvantum,cursor,gtkcursor,taskswitcher
# directory location starting and ending with / is needed.
# lookAndFeel
# userThemes
lookUserThemes=userDirFiles("/.local/share/plasma/look-and-feel/")
# print(lookUserThemes)
# systemThemes
lookSystemThemes=systemDirFiles("/usr/share/plasma/look-and-feel/")
# print(lookSystemThemes)

# plasmaTheme
# userThemes
plasmaUserThemes=userDirFiles("/.local/share/plasma/desktoptheme/")
# print(plasmaUserThemes)
# systemThemes
plasmaSystemThemes=systemDirFiles("/usr/share/plasma/desktoptheme/")
# print(plasmaSystemThemes)

# applicationStyles
# systemThemes
applicationSystemThemes=systemDirFiles("/usr/lib/x86_64-linux-gnu/qt5/plugins/styles/")
# print(applicationSystemThemes)

# windowdecoratios
# userThemes
windowUserThemes=userDirFiles("/.local/share/aurorae/themes/")
# print(windowUserThemes)
# systemThemes
windowSystemThemes=systemDirFiles("/usr/share/kwin/decorations/")
# print(windowSystemThemes)

# colorScheme
# userThemes
colorUserThemes = userDirFiles("/.local/share/color-schemes/color-schemes/")
# print(colorUserThemes)
# systemThemes
colorSystemThemes = systemDirFiles("/usr/share/color-schemes/")
# print(colorSystemThemes)

# icons
# userThemes
iconsUserThemes = userDirFiles("/.local/share/icons/")
# print(iconsUserThemes)
# systemThemes
iconsSystemThemes = systemDirFiles("/usr/share/icons/")
# print(iconsSystemThemes)

# splashScreen
# userThemes
splashUserThemes = userDirFiles("/.local/share/plasma/look-and-feel/")
# print(splashUserThemes)
# systemThemes
splashSystemThemes = systemDirFiles("/usr/share/plasma/look-and-feel/")
# print(splashSystemThemes)

# TestData
# testlist=[
#  'abcd.colors',
#  'abcd.colors.something',
#  'abcd.so',
#  'abcd.so.something',
#  'abcd.png',
#  'abcd.png.something',
#  'abcd.json',
#  'abcd.json.something',
#  'abcd.desktop',
#  'abcd.desktop.something'
# ]
# testlist.sort()

# here a list of values are passed,
# on deleteLine true entire line is deleted,
# on deleteLine false only word in line is deleted.
def editListValues(alist,deleteLine=False,*regexValue):
   tempList = []
   # single item of a list is taken
   for i in alist:
      if(deleteLine==True):
         for reg in regexValue:
            # substitutin the single item(i) with a regular expression and removing entire line,cannot make a blank line like in bash. 
            i=(re.sub(f".*{reg}$",'',i))
      if(deleteLine==False):
         for reg in regexValue:
            # substing the single item(i) with a regular expression and removing only matched pattern data.
            i=(re.sub(f"{reg}$",'',i))
      # temporary list to return,indentation is important, i element is only present in outer for loop,make sure the variable is inside it's scope.
      tempList.append(i)
   tempList.sort()
   # print(tempList)
   return tempList

# calling the method with list,and regex
x = editListValues(lookUserThemes,True,'.json')
for i in x:
   print(i)

# editListValues(lookUserThemes)
# append(lookSystemThemes)
# append(plasmaUserThemes)
# append(plasmaSystemThemes)
# append(applicationSystemThemes)
# append(windowUserThemes)
# append(windowSystemThemes)