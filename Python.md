Python is a easy to use language created for faster development time,while sacrificing computation time,python is about 1000X slower compared to C,C++,java.
Since interpreted languge.



## Data structures
### lists
list is a ordered collection of items,similar to array.can change items of list,mutable(editable)
syntax:     
`listname = ["items","items"]`      
we access the item with index number,starting from 0     
`listname[0]`     
we access the item from last using negative values,from -1.here -1 is the last element in the list,-2 is the last second element in the list.            
`listname[-2]`    
can access items in a range      
`listname[2:5]`      
end of index is exculded.     
so items from 2,3,4 are returned.      

**clear()**    
clears list items.      

### tuples
a tuple is a unmutable list,we can add once but can't edit items after wards.
to change tuples we copy the tuple to a list,then edit on that list,then copy the output to a tuple.  
syntax:
`tuplename = ("itemd","items","itesms")`
`tuplename[1]`
### set
a set is a unordered,unindexed data.
Syntax:
`setname={"item","item","item"}`    
we cannont access an item by index,we can just check if the data exists or not using **in**.
item1 in setname,
**mutable** 
once a set is created we can add new items,but can't change old items.
we use set with following and some more methods/functions.
**add()**      
**update()**      
**remove()**
### dictionary
dictionary is a collection unordered,changable,indexed.  dictionaries are key,value pairs.   
syntax:
dictionaryname = {
   "key":"value","key":"value"}
dictionaryname["key"]         
we can modify exisiting key,value pairs,add new ones.
we work with key of an item to identify it.     
some useful functions
**get()**
**values()**      
**keys()**
**items()**

## Conditional Statements
in python indentation,tab space is really important to create a block of code.
### If
syntax:     
>If condition:    
>tab code   
>elif condition:
>tab code
>else:   
>tab code   
we can use a shorthand if 
>If condition: code
>code If condition else code
>code if condition else code if condition else code
logical operators in python
**and**
**or**
**not**
### while
syntax:
>while condition:
>tab code
control statements
**break** will exit the immediate loop
**continue** will skip the code below it and loops next condition
### for
syntax:
> for condition:
> tab code
we use for loops to iterate through a list of items,or range of numbers.
Ex:
>for x in range(10):---->list of numbers
>tab print (x)
>for x in fruitslist:---->list of items
>tab print(x)

## Functions:
block of code to use as needed.              
syntax:           

`def functionname(parameters):tabspace code`    

parameter is the variable
argument is the value.
### optional parameters
we can specify default arguments in the function/method declaration
ex:
>add(x=0,y=0): return x+y     
>add()--->works      
>add(1)--->works     
>add(2,3)---->works     

we can give arguments if want to or the default values are taken into calculations.    
can only set individual argument from the beginning.

## lambda 
lambda is an anonymous function,that is used one time,can only have one expression
syntax:
`lambda arguments:expression`
ex:
x = lambda a : a+10
x(5)
a lambda function can be inside another function.a normal function has to be encapsulated for this to work.

## error handling
when an error is expected to raise while programming is running,we create a try and except block to crete a contingency code.    
the code to test will go inside the try block,the error is specified at except block,and relavent code to handle it is given inside it,their can be many except blocks for a single try block,but order matters,
sytax:
try:
tab code
except:errorname
tab code


## Class
syntax:
class classname:
   code

### functions
function inside a class should a one argument **self**,after that we give our needed arguments.

## object
syntax:
objectname=classname()

### __init__()
this is an object constructor,
when ever an object is being created this is used to assign values.     
it is created by default even if we don't create one.

### self
we use self parameter to reference to current object being used.
doesn't have to be self,can name it whatever we want but should be the firstparameter


## inheritance
we define a class that can inherite from another class.
we have single inheritance,multiple inheritance,multi level inheritance.
base class is parent class,sub class is child class.

syntax:
>class childclass(parentclass):
>   code

when we have a __init__() method inside a child class,the properties of parent class will not be inherited,same goes to any function that is overriden in child class.

to call a method inside a class
syntax:
`classname.methodname.`
ex:animal.eat(),inside dog class.

### super()
while the classname.methodname can be used to call any method in any class,we use super to call the parent methods only.
syntax:  
`super().method()`

### global 
to make a variable accessible in other functions,we can use keyword **global**   


### reading files 
**read-only(r)**
**write-only(w)**
**read and write(r+)**
**write and read(w+)**
**append-only(a)**
**append and read(a+)**

syntax:
file_object = open(r"filename","access")
r---> tell to ignore any special character that python may take as code.
Ex:/temp will be taken as /t for tab,with **r**,it will be taken as string.   


file_object.close()
to remove file lock,so other programs can access this.
useful functions
**write(string)**
**writelines(L) for l = [items,items,items]**
**read()**
**readline(linenumber)**
