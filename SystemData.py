import os,re

homeDir=os.path.expanduser("~")

# def main():

   # gtktheme,kvantum,cursor,gtkcursor,taskswitcher
   # directory location starting and ending with / is needed.
   # print("hello")

# takes absolute userpath,needs userPath value to inclue backslash,ex: /userpath/
def userDirFiles(userPath):
   x = os.listdir(f'{homeDir}{userPath}')
   x.sort()
   return x

# takes absolute system path
def systemDirFiles(systemPath):
   x = os.listdir(f'{systemPath}')
   x.sort()
   return x

# writes output to a file given above,one item per line
def append(alist):
   testfile=open("test.txt","a+")
   for i in alist:
      testfile.write(f"{i}\n")

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

def organizeData(userData,SystemData):
   tempList = []

   tempList.append('==========')
   tempList.append('User Theme')
   tempList.append('==========')
   for x in userData:
      tempList.append(x)

   tempList.append('==========')
   tempList.append('System Theme')
   tempList.append('==========')
   for x in SystemData:
      tempList.append(x)
   
   return tempList

def lookAndFeel():
   # lookAndFeel
   # userThemes
   UserThemes = userDirFiles("/.local/share/plasma/look-and-feel/")
   # print(lookUserThemes)
   # systemThemes
   SystemThemes = systemDirFiles("/usr/share/plasma/look-and-feel/")
   # print(lookSystemThemes)
   editedUserList=editListValues(UserThemes,True,'.json')
   editedSystemList=editListValues(SystemThemes,False,'.desktop')
   return organizeData(editedUserList,editedSystemList)

def plasmaTheme():
   # plasmaTheme
   # userThemes
   UserThemes=userDirFiles("/.local/share/plasma/desktoptheme/")
   # print(plasmaUserThemes)
   # systemThemes
   SystemThemes=systemDirFiles("/usr/share/plasma/desktoptheme/")
   # print(plasmaSystemThemes)
   editedUserList=editListValues(UserThemes,True,'.json')
   editedSystemList=editListValues(SystemThemes)
   return organizeData(editedUserList,editedSystemList)

def applicationStyles():
   # applicationStyles
   # systemThemes
   SystemThemes=systemDirFiles("/usr/lib/x86_64-linux-gnu/qt5/plugins/styles/")
   # print(applicationSystemThemes)
   editedSystemList=editListValues(SystemThemes,False,'.so')
   return organizeData([],editedSystemList)

def windowDecorations():
   # windowdecoratios
   # userThemes
   UserThemes=userDirFiles("/.local/share/aurorae/themes/")
   # print(windowUserThemes)
   # systemThemes
   SystemThemes=systemDirFiles("/usr/share/kwin/decorations/")
   # print(windowSystemThemes)
   editedUserList=editListValues(UserThemes)
   editedSystemList=editListValues(SystemThemes)
   return organizeData(editedUserList,editedSystemList)

def gtkTheme():
   pass
def colorScheme():
   # colorScheme
   # userThemes
   UserThemes = userDirFiles("/.local/share/color-schemes/color-schemes/")
   # print(colorUserThemes)
   # systemThemes
   SystemThemes = systemDirFiles("/usr/share/color-schemes/")
   # print(colorSystemThemes)
   editedUserList=editListValues(UserThemes,False,'.colors')
   editedSystemList=editListValues(SystemThemes,False,'.colors')
   return organizeData(editedUserList,editedSystemList)

def icons():
   # icons
   # userThemes
   UserThemes = userDirFiles("/.local/share/icons/")
   # print(iconsUserThemes)
   # systemThemes
   SystemThemes = systemDirFiles("/usr/share/icons/")
   # print(iconsSystemThemes)
   editedUserList=editListValues(UserThemes,True,'.png')
   editedSystemList=editListValues(SystemThemes,True,'.png')
   return organizeData(editedUserList,editedSystemList)

def kvantum():
   pass
def splashScreen():
   # splashScreen
   # userThemes
   UserThemes = userDirFiles("/.local/share/plasma/look-and-feel/")
   # print(splashUserThemes)
   # systemThemes
   SystemThemes = systemDirFiles("/usr/share/plasma/look-and-feel/")
   # print(splashSystemThemes)
   editedUserList=editListValues(UserThemes,True,'.json')
   editedSystemList=editListValues(SystemThemes,False,'.desktop')
   return organizeData(editedUserList,editedSystemList)

  # calling the method with list,and regex
   # have to pass exact value example .so will remove .so,so will remove only so
   # x = editListValues(lookUserThemes,True,'.json')
   # for i in x:
   #    print(i)

   # editListValues(lookUserThemes)
   # append(lookSystemThemes)
   # append(plasmaUserThemes)
   # append(plasmaSystemThemes)
   # append(applicationSystemThemes)
   # append(windowUserThemes)
   # append(windowSystemThemes)

# TestData
# innerList=[
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
# innerList.sort()

# this method gets data from other methods easy to implement.
def getSystemData(themeName):
   return themeName()


# take data from a file line by line,then add it to a list,create list of lists,reset the innerList 
def listFromFile(fileName):
   outerList=[]
   # read data from a file
   with open(f'{homeDir}{fileName}') as f:
      innerList=[]
      # appending each line to innerList,then from innerList to outerList
      for i in f.readlines():
         if i == "\n":#empty line means a new group of data
            outerList.append(innerList)
            innerList=[] # reset list to keep new group of data
         else:
            innerList.append(i)
      # for loop breaks when EOF reached,then this will append the last list
      outerList.append(innerList)
   return outerList


# a function to extract data from lists.first value is dictionary name
def dictionaryFromList(inputList):
   dictionaryData=[]

   for i in inputList: # two dimensional lists,so two for loops
      tempDictionaryData=[]#inner list gets reset every time loop starts
      for j in i:
         # extracting the Dictionaryname i.e, group(KDE) name,to create a dictionary
         dictionaryName=(re.findall('\[.*]*',j))
         if not dictionaryName == []: # we append non-empty data into a list
            # to apply regex on a list, we need to convert it to string or use it's index
            temp=re.sub('\[','',dictionaryName[0])
            dictionaryName=re.sub(']','',temp)
            tempDictionaryData.append(dictionaryName)
       #########################################     
         # extracting dictionary Data
         temp=(re.sub('\n','',j))
         dicData= (re.findall('^\w.*',temp))#taking data,which usually starts with a word
         if not dicData == []:
            tempDictionaryData.append(dicData[0])
         else:
            #there is a line break for every group of data,when a line break is encountered we save data into actual dictionary
            dictionaryData.append(tempDictionaryData)
   
   return dictionaryData

# function that will output a dictionaries from a file.
def getDictionaryFromFile(inputFile):
   # calling other function to get data
   receivedList=dictionaryFromList(listFromFile(inputFile))
   listOfDictionaries=[]
   # we receive a list of lists,where each list is a group of data,that we convert to a dictionary
   for i in receivedList:
      # a dictionary to store in above list
      innerDict={}
      for j in i:#j is the value inside a list
         # not all elements have equalto symbol inthem,so had to take this approach of individual key,value pair
         key=j.split('=')[0]
         val=j.split('=')[-1]
         if key==val:
            # in this list we have one value,with no =,so we give it our own.
            pair={"dictionaryName":val}
            innerDict.update(pair)
         else:
            # adding other key-value pairs into the list
            pair={key:val}
            innerDict.update(pair)
      # creating a list of dictionaries
      listOfDictionaries.append(innerDict.copy())
   return listOfDictionaries      
# getDictionaryFromFile('/.config/kdeglobals')
# print(dictionaryFromList(listFromFile('/.config/kcminputrc')))

# returns the value for given theme file from a groupname
def getCurrentThemeInfo(inputFile,groupName,key):
   dictionary=getDictionaryFromFile(inputFile)
   for i in dictionary:
      if i.get('dictionaryName') == groupName:
         return i.get(key)






# if __name__ == "__main__":
#    main()
# currentThemeData()