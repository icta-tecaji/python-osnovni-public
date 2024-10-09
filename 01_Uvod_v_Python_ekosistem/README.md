# Uvod v Python ekosistem

## Kako deluje program na računalniku?
A **program makes a computer usable.** Without a program, a computer, even the most powerful one, is nothing more than an object.

It can **execute only extremely simple operations.** For example, a computer cannot understand the value of a complicated mathematical function by itself, although this isn't beyond the realms of possibility in the near future.

### High-level and low-level languages

A **high-level language is one that is user-oriented** in that it has been designed to make it straightforward for a programmer to convert an algorithm into program code. A **low-level language is machine-oriented**. Low-level programs are expressed in terms of the machine operations that must be performed to carry out a task.

| **Differentiating factor** | **Low-level programming language**                                                                                            | **High-level programming language**                                                                                      |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| Definition                 | Language with less abstraction such that it is directly understandable and executable on the machine it is being written for. | Language with higher abstraction such that it is easy to interpret and understand for humans and is machine-independent. |
| Portability                | Not portable from one device to another.                                                                                      | Portable from one device to another.                                                                                     |
| Friendliness               | Machine-friendly language                                                                                                     | Programmer-friendly language                                                                                             |
| Understandability          | Difficult to understand, maintain and debug                                                                                   | Easy to understand, maintain and debug                                                                                   |
| Speed                      | High                                                                                                                          | Low                                                                                                                      |
| Memory efficient           | Comparatively high memory efficiency.                                                                                         | Comparatively low memory efficiency.                                                                                     |
| Translation process        | Usage of assembler whilst converting assembly language to machine language for consumption by CPU.                            | Usage of compiler/interpreter for translating into the machine-understandable format.                                    |
| Pre-requisite Knowledge    | Knowledge of computer architecture is necessary.                                                                              | Knowledge of computer hardware is not necessary.                                                                         |
| Instruction set            | Low-level instructions like a series of binary codes of 0s and 1s OR mnemonics like ADD, SUB, DIV, MUL, etc.                  | An interpreted or compiled programming language which has its own set of syntax and semantics.                           |
| Examples                   | Examples are: Assembly language and Machine language                                                                          | Examples are: Java, Python, COBOL                                                                                        |

[Source](https://unstop.com/blog/difference-between-high-level-and-low-level-languages)

<!-- Source: https://d8it4huxumps7.cloudfront.net/bites/wp-content/banners/2022/11/637afe7e1cacd_difference_between_high-level_and_low-level_languages.png?d=1200x800 -->

![High-level and low-level languages](https://d8it4huxumps7.cloudfront.net/bites/wp-content/banners/2022/11/637afe7e1cacd_difference_between_high-level_and_low-level_languages.png?d=1200x800)

## Uvod v programske jezike
A program written in a high-level programming language is called a **source code** (in contrast to the machine code executed by computers). Similarly, the file containing the source code is called the **source file**.

### Compilation vs. interpretation
There are two different ways of transforming a program **from a high-level programming language into machine language**:
- **COMPILATION**: The source program is translated once (however, this act must be repeated each time you modify the source code) by getting a file (e.g., an .exe file if the code is intended to be run under MS Windows) containing the machine code; now you can distribute the file worldwide; the program that performs this translation is called a compiler or translator.
- **INTERPRETATION**: You (or any user of the code) can translate the source program each time it has to be run; the program performing this kind of transformation is called an interpreter, as it *interprets the code every time it is intended to be executed*; it also means that you cannot just distribute the source code as-is, because the end-user also needs the interpreter to execute it.

[Source](https://edube.org/learn/python-essentials-1/programming-absolute-basics-compilation-vs-interpretation-5)

![Compilation vs. interpretation](./images/img01.png)

About Python:
- Python is an **interpreted language**. This means that it inherits all the described advantages and disadvantages.
- If you want to program in Python, you'll need the **Python interpreter**. You won't be able to run your code without it. Fortunately, Python is **free**. This is one of its most important advantages.


### What does the interpreter actually do?
A computer program is actually a piece of text, so the source code is usually placed in **text files**.

The interpreter **reads the source code from top to bottom** and from left to right.
1. First of all, the interpreter checks if all subsequent lines are correct.
2. If the interpreter **finds an error**, it finishes its work immediately. The only result in this case is an error message.
3. The interpreter will inform you where the error is located and what caused it. However, these messages may be misleading, as the interpreter isn't able to follow your exact intentions, and may detect errors at some distance from their real causes.
4. If the line looks good, the interpreter tries to execute it.
5. It is also possible that a significant part of the code may be executed successfully before the interpreter finds an error. This is normal behavior in this execution model.

## Pregled osnovnih pojmov
- Due to historical reasons, languages designed to be utilized in the interpretation manner are often called **scripting languages**, while the source programs encoded using them are called **scripts**.
- **Virtual machine - virtualka**: A Virtual Machine (VM) is a compute resource that uses software instead of a physical computer to run programs and deploy apps. One or more virtual “guest” machines run on a physical “host” machine.
- **Environment - okolje**: An environment is a space where you can install and run software. It is isolated from your system and other environments. You can have different versions of Python, Java, Node.js, Ruby, Go, etc. installed on your computer and switch between them with ease. You can also install different versions of the same language.
- **Server**: A server is a computer or system that provides resources, data, services, or programs to other computers, known as clients, over a network. In theory, whenever computers share resources with client machines they are considered servers. There are many types of servers, including web servers, mail servers, and virtual servers.
- **Library - knjižnica**: A library is a collection of functions / objects that serves one particular purpose. You could use a library in a variety of projects. (Various libraries are available for Python, Java, Node.js, Ruby, Go, etc.)
- **Framework**: A framework is a collection of libraries. The framework provides a foundation and a set of guidelines for building a system. It specifies the structure of your application. (Various frameworks are available for Python, Java, Node.js, Ruby, Go, etc.)
- **Package manager**: A package manager is a tool that automates the process of installing, updating, and removing packages. A package is a collection of code files that are bundled together. (Various package managers are available for Python, Java, Node.js, Ruby, Go, etc.)
- **Package**: A package is a collection of code files that are bundled together. (Various packages are available for Python, Java, Node.js, Ruby, Go, etc.)
- **IDE**: An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. An IDE normally consists of at least a source code editor, build automation tools, and a debugger. (Various IDEs are available for Python, Java, Node.js, Ruby, Go, etc.)
- **Syntax**: Syntax is the set of rules that defines the combinations of symbols that are considered to be correctly structured statements or expressions in that language. (Python syntax is very simple and easy to learn.)

## Uvod v Python
**Python is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming.**


### History
- [History and Philosophy of Python](https://python-course.eu/python-tutorial/history-and-philosophy-of-python.php)
- [A brief history of Python](https://exyte.com/blog/a-brief-history-of-python)

One of the amazing features of Python is the fact that it **is actually one person's work.** Usually, new programming languages are developed and published by large companies employing lots of professionals, and due to copyright rules, it is very hard to name any of the people involved in the project. Python is an exception.

And while you may know the python as a large snake, the name of the Python programming language comes from an old BBC television comedy sketch series called **Monty Python's Flying Circus**.

Python was created by **Guido van Rossum**, born in 1956 in Haarlem, the Netherlands. Of course, Guido van Rossum did not develop and evolve all the Python components himself.

The circumstances in which Python was created are a bit puzzling. According to Guido van Rossum:
> In December 1989, I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas. My office (...) would be closed, but I had a home computer, and not much else on my hands. I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus).

The speed with which Python has spread around the world is a result of the **continuous work of thousands (very often anonymous) programmers**, testers, users (many of them aren't IT specialists) and enthusiasts, but it must be said that the very first idea (the seed from which Python sprouted) came to one head - Guido's.

### Development Steps of Python

Guido Van Rossum published the **first version of Python code (version 0.9.0)** in **February 1991**. This release included already exception handling, functions, and the core data types of list, dict, str and others. It was also object oriented and had a module system.

**Python version 1.0 was released in January 1994**. The major new features included in this release were the functional programming tools lambda, map, filter and reduce, which Guido Van Rossum never liked.

Six and a half years later in **October 2000, Python 2.0** was introduced. This release included list comprehensions, a full garbage collector and it was supporting unicode.

Python flourished for another 8 years in the versions 2.x before the next major release as **Python 3.0** (also known as "Python 3000" and "Py3K") was released. Python 3 is not backwards compatible with Python 2.x.

A good example of **Python’s principles is the Zen of Python**, a set of aphorisms from the software engineer Tom Peters. In 20 lines such as “Beautiful is better than ugly.”, the [Zen contains the core philosophy of Python](https://peps.python.org/pep-0020/).

> Try to read the Zen of Python and think about what each line means. You can do this by typing `import this` in the Python interpreter.

```
>>> import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

### Why Python? Advantages/Disadvantages
- [Introduction to Python 3](https://realpython.com/python-introduction/)

**Advantages**:
- Python is Popular
- Python is Free
- Python is Portable
- It is beginner-friendly and simple (Easy to learn, Easy to read, Easy to write, Easy to debug).
- Python is open-source and has a large community.
- It is great for both startups as well as big organizations.
- It has great career opportunities.
- Python has many powerful frameworks. 
- Python’s readability and ease-of-use make developers more productive.
- Is a general-purpose language, but is used almost everywhere (web development, machine learning, data science, Scripting, biology,... etc.)

**Disadvantages**:
- Python is slow as compared to C or C++. It's not a speed demon - Python does not deliver exceptional performance;
- In some cases it may be resistant to some simpler testing techniques - this may mean that debugging Python's code can be more difficult than with other languages; fortunately, making mistakes is always harder in Python.
- Not for low-level programming (like microcontrollers, embedded systems, etc.). There are still some frameworks like MicroPython, CircuitPython, etc. to develop low-level applications in Python.
- Not for Mobile and Game development (although there are some frameworks like Kivy, Pygame, etc. to develop mobile and game applications in Python)

While Python was steadily growing basically its whole existence, from around 2010, it started on a growth trajectory that soon enabled it to rival other top programming languages, such as Java and JavaScript.
![Python growth](https://149351115.v2.pressablecdn.com/wp-content/uploads/2017/09/projections-1-1024x878.png)
[Source](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)

### How Python Interprets Your Program
- [A Technical Deep Dive into Python](https://www.appdynamics.com/blog/engineering/a-technical-deep-dive-into-python/)
- [Python Internals: An Introduction](https://blog.sourcerer.io/python-internals-an-introduction-d14f9f70e583)

Python is also a piece of software called an interpreter. The interpreter is the program you’ll need to run Python code and scripts. Technically, the interpreter is a layer of software that works between your program and your computer hardware to get your code running.

In this process the interpreter will:
1. **Process the statements of your script in a sequential fashion**
2. **Compile the source code to an intermediate format known as bytecode**
    - This bytecode is a translation of the code into a lower-level language that’s platform-independent. Its purpose is to optimize code execution. So, the next time the interpreter runs your code, it’ll bypass this compilation step.
    - Strictly speaking, this code optimization is only for modules (imported files), not for executable scripts.
    - The bytecode is stored in files with the `.pyc` extension. These files are binary files that contain the bytecode, which is then sent to the PVM for execution.
3. **Ship off the code for execution**:
    - At this point, something known as a Python Virtual Machine (PVM) comes into action. The PVM is the runtime engine of Python. It is a cycle that iterates over the instructions of your bytecode to run them one by one.
    - The PVM is not an isolated component of Python. It’s just part of the Python system you’ve installed on your machine. Technically, the PVM is the last step of what is called the Python interpreter.

The whole process to run Python scripts is known as the **Python Execution Model**.

[Source](https://www.c-sharpcorner.com/blogs/importance-of-python-programming1)

![Python Execution Model](./images/img03.png)

### Python Implementations Types
- [Best Python Interpreters: Choose the Best in 2023](https://hackr.io/blog/python-interpreters)

Depending on the Python implementation you use, the interpreter can be:
- **CPython**:
    - The most popular form of Python being implemented today, CPython is often thought of as the “default” Python implementation. Written in C, CPython compiles source code to bytecode. After that, it interprets the bytecode, executing it on the fly.
    - It is compiled to run on virtual machines, which are software that emulate specific computer hardware. That way, the bytecode does not have to be configured for a myriad of different computer systems.
- **Jython**:
    - Another implementation of Python is called Jython. Instead of C, it is written in Java and is interpreted for the Java Virtual Machine (JVM).
    - The reason there is a variety of Python implementations is each one is better-suited for a unique technology stack. For example, Jython is geared toward a Java stack. It:
        - Works naturally and effortlessly with Java programs.
        - Imports a variety of Java classes.
        - Uses Java classes directly from inside the Jython program.
- **IronPython**:
    - Written in C#, IronPython was created by Jim Hugunin in 2006 and is designed for the .NET stack. 
- **PyPY**:
    - PyPy is a Python implementation written in Python. It is a very fast implementation of Python, but it is not fully compatible with CPython.

### Python 2 vs. Python 3
- [How we rolled out one of the largest Python 3 migrations ever](https://dropbox.tech/application/how-we-rolled-out-one-of-the-largest-python-3-migrations-ever)
- [Difference Between Python 2 and 3](https://www.interviewbit.com/blog/difference-between-python-2-and-3/)
- [Python 2 vs 3: Everything You Need to Know](https://www.datacamp.com/blog/python-2-vs-3-everything-you-need-to-know)

Python 2 was launched in 2000; Python 3 was launched in 2008. The issue with Python 3 was that it wasn’t backward compatible with its predecessor. So many companies still rely on Python 2—fourteen years after the introduction of Python 3—because transferring codes between Python 2 vs. 3 is a lot of effort. It could take years. 

> It took DropBox three years to migrate, despite Guido Van Rossum working for them.

Python 2 is no longer supported by the Python Software Foundation. The last major version of Python 2, Python 2.7, was released in 2010 and was supported through 2020. After 2020, there was no new security updates, bug fixes, or other improvements. **Python 2 is legacy, Python 3 is the present and future of the language.**

**Difference Between Python 2 and 3**:
- Print is now a function
- Views and iterators instead of lists
- The rules for ordering comparisons have been simplified. E.g. a heterogeneous list cannot be sorted, because all the elements of a list must be comparable to each other.
- There is only one integer type left, i.e. int. long is int as well.
- The division of two integers returns a float instead of an integer. "//" can be used to have the "old" behavior.
- Text Vs. Data Instead Of Unicode Vs. 8-bit

### Python 3 versions
- [Development Cycle](https://devguide.python.org/developer-workflow/development-cycle/)
- [Status of Python Versions](https://devguide.python.org/versions/)

Python uses a `major.minor.micro` nomenclature for production-ready releases. So for Python 3.1.2 final, that is a major version of 3, a minor version of 1, and a micro version of 2.
- new **major versions** are exceptional; they only come when strongly incompatible changes are deemed necessary, and are planned very long in advance;
- new **minor versions** are feature releases; they get released annually, from the current in-development branch;
- new **micro versions** are bugfix releases; they get released roughly every 2 months; they are prepared in maintenance branches.

![Python 3 versions](./images/img02.png)

## Predstavitev Python dokumentacije in virov za lastno učenje

### Python Official Resources
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python Documentation](https://docs.python.org/3/)
- [The official home of the Python Programming Language.](https://www.python.org/)
- [Python Package Index](https://pypi.org/)
- [Python Enhancement Proposals](https://www.python.org/dev/peps/)
- [Python Developer’s Guide](https://devguide.python.org/)

### Tutorial Resources
- [Real Python](https://realpython.com/): Real Python is an online learning platform that teaches individuals and companies the skills they need to work with Python in the real world.
- [SuperFastPython](https://superfastpython.com/): Master Threading, Multiprocessing, and AsyncIO
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/)
- [Test-Driven](https://testdriven.io/): Test-Driven Development with Python, Flask, and Docker
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [Python Tutorial](https://github.com/data-flair/python-tutorial)
- [Python for Biologists](https://www.pythonforbiologists.org/)

### Online Python Interpreters
If you want to try out the examples in this tutorial without setting up Python on your machine, then there are several websites that offer an online Python interpreter:
- [Python.org Online Console](https://www.python.org/shell/)
- [Repl.it](https://replit.com/)
- [Python Fiddle](http://pythonfiddle.com/)
- [Trinket](https://trinket.io/)
- [Python Anywhere](https://www.pythonanywhere.com/)

These cloud-based Python interpreters may not be able to execute some of the more complex examples in this tutorial, but they’re adequate for running most of the code and may be a nice way to get started. 

### Exercise and Quiz Resources
- [Exercism](https://exercism.org/): Exercism is an online platform designed to help you improve your coding skills through practice and mentorship.

### Other Usefull Resources
- [very Programmer Should Know](https://github.com/mtdvio/every-programmer-should-know)
- [Awesome Python](https://github.com/vinta/awesome-python): A curated list of awesome Python frameworks, libraries, software and resources.
- [Awesome Python Books](https://github.com/Junnplus/awesome-python-books)
- https://pythontutor.com/
