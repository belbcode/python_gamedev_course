
# Day 1 Contents
1. What is a computer?
2. What is a programming language?
    * What is Python?
    * How to set up Python.
        * How Python works on the computer
    * Windows/Unix Terminals
        * Using Python in the terminal (sucks)
3. What is an IDE
    * Setting up visual studio code
4. Creating your first Python File
    * print("Hello world")
5. Python Datatypes
    * Numbers
    * Strings
    * Lists
6. Variables
	* assignment
7. Logical Operators
	* Boolean
	* Comparison Operators
  	* if
  	* else if
  	* else
8. Guessing Game
    
## What is a computer?
A computer is a machine that can read a set of instructions and modify those instructions. In modern computing these instructions are written in binary, the 0s and 1s most commonly seen in movies when somebody is 'hacking into the mainframe'. Binary is the only language a computer understands, this is because a computer (CPU) is comprised of millions to billions of microscopic electrical devices called 'transistors'. When a transistor has an electrical current going through it, the computer registers that as a 1, if there is no electrical current, it registers as a 0. The 2 possible options is why its called "binary". The transistor serves as the basis for modern computing. A binary gate or transistors that outputs either a 1 or a 0 is called a bit. 8 of these bits make up a byte. The "byte" from kilobyte, megabyte, and gigabyte. You can argue that all a computer really does is manipulate data. The words you read on an online article or the movie you watch on your phone or even video games are just a human legible side-effects of a computer serving 1s and 0s.
There are many components that make up a computer. Some important components are: The CPU (central processing unit) which reads and executes (processes) instructions, its the brain of the computer. RAM stands for (Random Access Memory). RAM is where the computer stores information that is currently being used. RAM is very fast and easy for the CPU to access. On the contrary, the Hard Drive is where the computer stores data in the long term. Data from the Hard Drive is significanlty slower to access than RAM memory. Think of RAM as short-term memory, the information that's relevant to what your doing right now. How to use a computer, listening comprehension, etc. The Hard Drive is more long-term memory, what you had for breakfast today, how to ride a bike. When hard drive data needs to be accessed it gets loaded into the RAM for the CPU to use.

## What is a programming language?
As I mentioned before, a computer can only read 0s and 1s. This makes it very complicated for a human to interface with a computer. Humans can learn to speak in binary, but the process is clumsy and unintuitive. Due to this major bottleneck to working on computers, early computer scientists devised a way to simplify the act of producing binary instructions. The first programming languages: COBOL, FORTRAN, Assembly- -were born of this endevor. They would package a set of binary instructions that had a function (let's say adding one value to another value) and linked it to a human legible syntax (let's say "+"), and voila! You now have an addition operator! Of course this is a gross simplification, the designers had to also handle the messy logic of how human legible input environments would be implemented and a bunch more stuff I probably haven't thought about. I think you could see how this creates a positive feedback loop of functionality. The first programming languages were made by the process of modulating functions in binary instruction into a human readable format and used the new modular (context) (functionality) to create more refined functions. A toolmaker using his tools to make better tools. Or to make a modern (Minecraft) analogy: Mining stone with a wooden pickaxe so you can build a stone pickaxe. The process of encapsulating logic and repackaging it to be more ledgible and easier to access is the most fundamental principle in computer programming. And you will do it to.

## What is Python?
Python is one of those 'refined' tools I just talked about. Python is a programming language that was released in 1991. Old by some standards but it has been continually modified and updated till today. The current stable version is Python 3.10.5. Python is known as a "interpretted" programming language, this means it doesn't actually interface with the hardware of the computer **THERE ARE EXCEPTIONS TO THIS**. Instead Python code is executed in a virtual environment known as the python interpretter. The virtual environment does communicate with hardware but the endpoint of a python script is ultimately software and so that one step of seperation from the hardware is what deems it as "interpretted". As opposed to compiled, but I won't get into that at the moment.

#### How to set up Python:
(This is bare bones because it will just be demonstrated live)
You can install Python by going to their website https://www.python.org/downloads/ and pressing the big yellow button that says "Download Python 3.10.5" it should recognize which OS (Operating System, we didn't even get into that) you are using but if not there should be an option on the page to download the version supported by your OS. After it downloads open the installer and begin the process of installing Python. Make sure that when it prompts you, you check the "Add Python to PATH" option on the installer. This makes it so that you can access Python from your window terminal segueing us into.

#### How Python works on the computer:
What we've just downloaded is the python executable. The python executable is an environment which allows us to check and execute python scripts. By adding Python to our PATH folder we also enabled ourselves to access python from the terminal of our computer. Which begs the question, what's a terminal. The Windows terminal or "command prompt" is a program that let's humans interface with their operating system. It's called a Shell because it encapsulates and abstracts the features of an OS for the common user. Ironic considering how antiquated the program might seem today. The CLI counterpart in Mac and Linux is called BASH, it's been in use since the 70s. Good program. There are different types of Shells, Graphical-User-Interface or GUI which just that you can interact with the OS with more than text commands, like the one your using now. Windows still includes their command-line-interface CLI because there are some tasks on computers that are very slow to access through sole graphical interfacing, not stuff you need to worry about for the time being. The point is, for the time being we'll be creating programs that will have simple text inputs and will lack graphical output so until then we'll need a text interface to see what our programs are doing.

#### Using Python in the Python Executable or Shell:
So now we can access the Python Executable in two ways. First let's just open up the application. Go to your Windows search bar, type in Python and open it up.
(Live demonstration)
Okay let's now do the same thing but in the windows shell. What's cool about the windows shell is that I can navigate through the Windows fileSystem and use the native OS features in order to create and save files. Let's create a python file and then run it!
(Live demonstration)

## What is an IDE?
As you can see the process of coding in python from its own CL executable or the Command Prompt is extraordinarily janky. That's because it was never meant to be done that way. Remember how we wrote a python script, saved it as a .py and then executed the file? Well that file was essentially a bunch of text formatted in a way so that the python interpreter would understand it. Technically you could write that in google docs if you wanted to. But Google docs has certain qualities and lacks certain features that make it convenient to write code. What we want is a text editing application that provides an environment for running and testing the programs we make. Enter IDEs, Integrated Development environments. IDEs allow us to write, test, and refactor code all in one place. They usually provide intellisense, sort of like autocomplete for coding.

##### Installing Visual Studio Code
"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

#### Creating a Python File
Okay now we're finally ready to start coding. First let's open up a directory in VS Code. Let's go to the desktop and make a new folder, call it "python_projects".
Now let's right click on the folder and open it in VS Code. (Demonstrate how you can access the folder from within VS Code as well.) Let's open up a new file. VS Code defaults to a text file until you provide an .extension but the python extension we installed will automatically give us the option to write a .py file. Okay let's write our first line of code: print("Hello world"). Save the file as hello.py. Now let's open up a terminal in VS Code. With the python extension, VS Code loads the python executable into the terminal. If we hadn't done this we would have defaulted to the command prompt instead and we would've had to launch Python manually. Okay enough dallying let's execute our code. In the terminal type "python hello.py". You just got the computer to say "hello". Isn't that neat? Here's what we just did. "print" is a command embedded into python that logs text into the python executable. You can see that the python executable is actually pointing to a specific folder. This is the immediate scope of the python executable. If we were to try to execute the "python" command to run the file from the desktop folder we would get an error. Now it is pretty tedious and daunting to make sure that you remember and type the filename correctly and make sure the path is correctly specified we can bypass that by simply clicking the play button on the top-right corner of the screen. (demonstrate) I just want to show you what is actually happening when you do it.
## Python Datatypes
Datatypes are the different ways a computer interprets values. Remember computers only know 1s and 0s so its important to tell the computer what its actually reading. Modern programming languages like Python can infer type just by assignment. You don't have to implicitly declare what type a given variable will be. Modern Programming languages also define what operations can be performed on a given type. If that doesn't make sense it will in a minute.
Let's go over some basic datatypes:
### Numbers
Numbers are just what you expect:
They can be integer values: **5, -12, 101**
They can be floats or decimal values: **2.1, 12.3421**
You can perform calculations on them: **2 + 21 = 23**
There are 5 main operands that you should know about: ( + , - , * , / , % )
The first four behave as you'd expect: addition, subtraction, multiplication and division.
Division is a little interesting as it always returns a float value. e.g.
**\>>>2 + 2
. . . 4
\>>> 16 / 4
. . . 4.0**
This has to do with how computers do math and will have implications later down the road but for now just know that you can mitigate this behavior with the "floor division" operand "//" e.g.
**\>>> 5 / 2
. . . 2.5
\>>> 5 // 2
. . . 2**
Its called the floor because it will always round down, to the floor of the possible value.
### Strings
This is probably the first time you're encountering this term. Strings are how the computer interprets plain text. Strings are typically denoted by their wrapper. Usually a set of quotes like such: "I am a string"
We place strings in quotes when referencing them in a program so that the computer can differentiate between plain text and commands that you want to pass to the interpreter. They are called "strings" because they are strings of characters like 'a', 'b' or '!'. Strings as a datatype come packaged with certain properties that you can access.
A string's length is the number of characters the string is composed of. For example the string "Hello World!" has a length of 11 characters. You can access any individual character in the string with the syntax:
**\>>> "Hello World!"[4]
. . . "o"**
What's happening is that Python is accessing position 4 in the string. You might notice that although we used position 4 we got the fifth letter in the string. This is because Computers start counting from the 0th position. So to get the first letter in the string you'd need to write
**\>>> "Hello World!"[0]
. . . "H"**
You don't need to count how many letters are in a string every time you want to know its bounds. There's a handy built-in length function that can handle that for you.
**\>>> len("Hello World!)
. . . 11**
We'll figure out how that **function** works soon. If you're really keen you might have already figured out that the space between "Hello" and "World" is also included in the count. In programming blank space will still be considered as a character.
So:
**\>>> "Hello World!"[5]
. . . " "**
and
**\>>> len("  ")
. . . 1**
### Lists
A list is technically not a data type, instead lists can be thought of more as a data structure. Lists are containers of multiple pieces of data that can be accessed and modified in a sequence. Here's what they look like:
**[112, 65, 85, 342 ]**
Like strings, lists have a length property that can be accessed by the length function:
**\>>>len([112, 65, 85, 342 ])**
**. . . 4**
Lists can also be accessed in the same way as a string with the position starting at 0.
**\>>>[112, 65, 85, 342 ][2]
. . . 85**
But here's where the similarities end. For one, you can store different datatypes within a list, even a list itself!
**[5, "Hi!", "2342", True, [1, 3, 75, 0, -1]]**
Lists can also be modified while strings cannot, this is part of a more complicated concept called Mutability. What you need to know now is that this:
["Hello", "my", "name", "is", "Joe"][4] = "Bob"
returns
["Hello", "my", "name", "is", "Bob"]
Whereas:
"Hello my name is Joe"[4] = "p"
returns
TypeError: 'str' object does not support item assignment.
You may have noticed that the Python interpreter referred to the string datatype as an 'object'. Almost all data in Python can is an Object. What that means more practically is that any given datatype like numbers, strings, or lists, are instances of some predefined object. That predefined object being known as a **class**. Again this is far ahead of where we are at the moment. I'll just let that brief description stew in your head for a bit. 
## Variables
Variables are the butter of programming. A variable is a keyword set or "assigned" by the programmer to reference a value in the computer's memory. In Python assigning variables is the easiest it can be.
**\>>>x = 1
\>>>print(x)
. . . 1**
Variables are useful because I don't want to write out some long string, number or array more than once. I also don't want to have to keep track of a bunch of values. What are computers for in the first place. Most operations in Python or any programming language are just impractical without using variables. This previous example:
**[112, 65, 85, 342 ]**
**\>>>len([112, 65, 85, 342 ])**
**. . . 4**
Is a lot easier like this:
**x = [112, 65, 85, 342 ]**
**\>>>len(x)**
**. . . 4**
All the same behaviors associated with the datatype will still work when attached to the variable.
**x = ["Hello", "my", "name", "is", "Joe"]
x[4] = "Bob"
print(x)
["Hello", "my", "name", "is", "Bob"]**
But be careful, your variable is just a reference to the actual value, datatype and all. If you try to execute an operation that is not compatible with the datatype it will still throw an error.
**x = "Brick"
x[0] = "T"
TypeError: 'str' object does not support item assignment.**
You can also print variables with the print() function. But be warned that print() only accepts strings as a value. Therefore if the variable you want to print isn't a string, you need to pass an additional function called str(). 
From this point forward I will be assigning almost all data that the program logic will handle with a variable. There will still be some unique cases where using raw data may be applicable. However, variables are a key foundation for the process of simplifying and refining complex logic. 
## Logical Operations
### Boolean
Booleans are the simplest datatype. It is either True or False.
**you_stink = True**
**you_have_girlfriend = False**
Every data type has a boolean attribute attached to it and it works as you'd intuitively expect. Data with meaningful content will return True. Empty or null values in any data type will return False. You can access a value's boolean attribute with the function bool().
Example:
**bool("Hello.") True
bool("") False
bool(21) True
bool(0) False
bool([1, 2, 3]) True
bool([]) False**
You can find an exhaustive list of False bool() returns here:
https://www.w3schools.com/python/python_booleans.asp
On their own, Boolean values don't have any attributes you can use to modify its value. The real magic with Boolean values is they can be used manipulate a program's logic. 
### Comparison Operators
Comparison Operators allow us to compare two values against each other and make a True or False assumption about the comparison. Comparisons are wrapped in parentheses and must include a comparison operator in order to execute as a comparison.
Most of the operators will be familiar mainstays of your math classes.
**(a < b) a is less than b
(a > b) a is greater than b
(a==b) a is equal to b
(a<=b) a is less than or equal to b
(a>=b) a is greater than or equal to b
(a!=b) a is not equal to b**
A comparison will return as a Boolean True or False depending on evaluation of the comparison statement.
Example:
**(7 < 6), Translation: 7 is less than 6, Evaluation: False**
**(91 != 16) Translation: 91 is not equal to 16, Evaluation: True**
You can even pass math operations into comparisons.
**(5 == (6-1)) . . .True**
You can even pass in strings as arguments in comparisons, the way strings are evaluated is tricky. Can you figure it out?
Hint: These are still number evaluations.
**("abcd"<"efgh") . . .True
("abde"<"abcde") . . .False**

### If Statements
We're really close now. 
The if Statement is a conditional statement that allows you to embed logic into your program. It works as you'd logically expect:
```
if (comparison):
|   code to be executed
```
Here's an example of an if statement that checks whether the name variable starts with the letter 'a'.
```
name = "aaron"
if(name[0]=="a"):
|   print("A is for" + name)
```
A note on how python's syntax expects you to structure conditional statements. Python uses indentation to denote the scope of a statement. Let's look at a set of nested  
If you don't pass a comparison operator into the if clause of an if-statement than the python interpreter will evaluate bool() attribute of the value that you have passed in. e.g.
### Else

### Nested Ifs
```
name = ""
if name:
|	print("Hello "+ name + "!")
else
|	name = input("What is your name: ")
```
This code checks if there is a value attached to the name variable and if there isn't requests the user to provide one.
