Day 1 Contents
  What is a computer?
  What is a programming language?
  What is Python?
    How to set up Python.
    How Python works on the computer
      Windows/Unix Terminals
    Using Python in the terminal (sucks)
  What is an IDE
    Setting up visual studio code
  Creating your first Python File
    print("Hello world")
  Python Datatypes
    Numbers
    Strings
    Lists
  Logical Operators
  	if
  	if else
  	else
  Guessing Game
    
What is a computer?
A computer is a machine that can read a set of instructions and modify those instructions. In modern computing these instructions are written in binary, the zeros and ones most commonly seen in movies when somebody is 'hacking into the mainframe'. Binary is the only language a computer understands, this is because a computer (CPU) is comprised of millions to billions of microscopic electrical devices called 'transistors'. When a transistor has an electrical current going through it, the computer registers that as a 1, if there is no electrical current, it registers as a 0. The 2 possible options is why its called "binary". The transistor serves as the basis for modern computing. A binary gate or transistors that outputs either a 1 or a 0 is called a bit. 8 of these bits make up a byte. The one from kilobyte, megabyte, and gigabyte. You can argue that all a computer really does is manipulate data. The words you read on an online article or the movie you watch on your phone or even video games are just a human legible side-effects of the computer serving 1s and 0s.
There are many components that make up a computer. Some important components are: The CPU (central processing unit) which reads and executes (processes) instructions, its the brain of the computer. RAM stands for (Random Access Memory). RAM is where the computer stores information that is currently being used. RAM is very fast and easy for the CPU to access. On the contrary, the Hard Drive is where the computer stores data in the long term. Data from the Hard Drive is significanlty slower to access than RAM memory. Think of RAM as short-term memory, the information that's relevant to what your doing right now. How to use a computer, listening comprehension, etc. The Hard Drive is more long-term memory, what you had for breakfast today, how to ride a bike. When hard drive data needs to be accessed it gets loaded into the RAM for the CPU to use.

What is a programming language?
As I mentioned before, a computer can only read 0s and 1s. This makes it very complicated for a human to interface with a computer. Humans can learn to speak in binary, but the process is clumsy and unintuitive. Due to this major bottleneck to working on computers, early computer scientists devised a way to simplify the act of producing binary instructions. The first programming languages: COBOL, FORTRAN, Assembly- -were born of this endevor. They would package a set of binary instructions that had a function (let's say adding one value to another value) and linked it to a human legible syntax (let's say "+"), and voila! You now have an addition operator! Of course this is a gross simplification, the designers had to also handle the messy logic of how human legible input environments would be implemented and a bunch more stuff I probably haven't thought about. I think you could see how this creates a positive feedback loop of functionality. The first programming languages were made by the process of modulating functions in binary instruction into a human readable format and used the new modular (context) (functionality) to create more refined functions. A toolmaker using his tools to make better tools. Or to make a modern (Minecraft) analogy: Mining stone with a wooden pickaxe so you can build a stone pickaxe. The process of encapsulating logic and repackaging it to be more ledgible and easier to access is the most fundamental principle in computer programming. And you will do it to.

What is Python?
Python is one of those 'refined' tools I just talked about. Python is a programming language that was released in 1991. Old by some standards but it has been continually modified and updated till today. The current stable version is Python 3.10.5. Python is known as a "interpretted" programming language, this means it doesn't actually interface with the hardware of the computer **THERE ARE EXCEPTIONS TO THIS**. Instead Python code is executed in a virtual environment known as the python interpretter. The virtual environment does communicate with hardware but the endpoint of a python script is ultimately software and so that one step of seperation from the hardware is what deems it as "interpretted". As opposed to compiled, but I won't get into that at the moment.

How to set up Python:
(This is bare bones because it will just be demonstrated live)
You can install Python by going to their website https://www.python.org/downloads/ and pressing the big yellow button that says "Download Python 3.10.5" it should recognize which OS (Operating System, we didn't even get into that) you are using but if not there should be an option on the page to download the version supported by your OS. After it downloads open the installer and begin the process of installing Python. Make sure that when it prompts you, you check the "Add Python to PATH" option on the installer. This makes it so that you can access Python from your window terminal segueing us into.

How Python works on the computer:
What we've just downloaded is the python executable. The python executable is an environment which allows us to check and execute python scripts. By adding Python to our PATH folder we also enabled ourselves to access python from the terminal of our computer. Which begs the question, what's a terminal. The Windows terminal or "command prompt" is a program that let's humans interface with their operating system. It's called a Shell because it encapsulates and abstracts the features of an OS for the common user. Ironic considering how antiquated the program might seem today. The CLI counterpart in Mac and Linux is called BASH, it's been in use since the 70s. Good program. There are different types of Shells, Graphical-User-Interface or GUI which just that you can interact with the OS with more than text commands, like the one your using now. Windows still includes their command-line-interface CLI because there are some tasks on computers that are very slow to access through sole graphical interfacing, not stuff you need to worry about for the time being. The point is, for the time being we'll be creating programs that will have simple text inputs and will lack graphical output so until then we'll need a text interface to see what our programs are doing.

Using Python in the Python Executable or Shell:
So now we can access the Python Executable in two ways. First let's just open up the application. Go to your Windows search bar, type in Python and open it up.
(Live demonstration)
Okay let's now do the same thing but in the windows shell. What's cool about the windows shell is that I can navigate through the Windows fileSystem and use the native OS features in order to create and save files. Let's create a python file and then run it!
(Live demonstration)

What is an IDE?
As you can see the process of coding in python from its own CL executable or the Command Prompt is extraordinarily janky. That's because it was never meant to be done that way. Remember how we wrote a python script, saved it as a .py and then executed the file? Well that file was essentially a bunch of text formatted in a way so that the python interpreter would understand it. Technically you could write that in google docs if you wanted to. But Google docs has certain qualities and lacks certain features that make it convenient to write code. What we want is a text editing application that provides an environment for running and testing the programs we make. Enter IDEs, Integrated Development environments. IDEs allow us to write, test, and refactor code all in one place. They usually provide intellisense, sort of like autocomplete for coding.

Installing Visual Studio Code

Creating a Python File
Okay now we're finally ready to start coding. First let's open up a directory in VS Code. Let's go to the desktop and make a new folder, call it "python_projects".
Now let's right click on the folder and open it in VS Code. (Demonstrate how you can access the folder from within VS Code as well.) Let's open up a new file. VS Code defaults to a text file until you provide an .extension but the python extension we installed will automatically give us the option to write a .py file. Okay let's write our first line of code: print("Hello world"). Save the file as hello.py. Now let's open up a terminal in VS Code. With the python extension, VS Code loads the python executable into the terminal. If we hadn't done this we would have defaulted to the command prompt instead and we would've had to launch Python manually. Okay enough dallying let's execute our code. In the terminal type "python hello.py". You just got the computer to say "hello". Isn't that neat? Here's what we just did. "print" is a command embedded into python that logs text into the python executable. You can see that the python executable is actually pointing to a specific folder. This is the immediate scope of the python executable. If we were to try to execute the "python" command to run the file from the desktop folder we would get an error. Now it is pretty tedious and daunting to make sure that you remember and type the filename correctly and make sure the path is correctly specified we can bypass that by simply clicking the play buttion on the topright corner of the screen. (demonstrate) I just want to show you what is actually happening when you do it.

Logical Operaters
