# Priprava razvojnega okolja

## Pregled integriranih razvojnih okolji

- [Python IDEs and Code Editors (Guide)](https://realpython.com/python-ides-code-editors-guide/)

An **IDE (or Integrated Development Environment)** is a program dedicated to software development. As the name implies, IDEs integrate several tools specifically designed for software development. These tools usually include:

- An editor designed to handle code (with, for example, syntax highlighting and auto-completion)
- Build, execution, and debugging tools
- Some form of source control

Most IDEs support many different programming languages and contain many more features. They can, therefore, be large and take time to download and install. You may also need advanced knowledge to use them properly.

In contrast, a dedicated **code editor** can be as simple as a text editor with syntax highlighting and code formatting capabilities. Most good code editors can execute code and control a debugger. The very best ones interact with source control systems as well. Compared to an IDE, a good dedicated code editor is usually smaller and quicker, but often less feature rich.

**Requirements for a Good Python Coding Environment**:

- **Save and reload code files**: If an IDE or editor won’t let you save your work and reopen everything later, in the same state it was in when you left, it’s not much of an IDE.
- **Run code from within the environment**: Similarly, if you have to drop out of the editor to run your Python code, then it’s not much more than a simple text editor.
- **Debugging support**: Being able to step through your code as it runs is a core feature of all IDEs and most good code editors.
- **Syntax highlighting**: Being able to quickly spot keywords, variables, and symbols in your code makes reading and understanding code much easier.
- **Automatic code formatting**: Any editor or IDE worth it’s salt will recognize the colon at the end of a while or for statement, and know the next line should be indented.

**General Editors and IDEs with Python Support**:

- [Visual Studio Code](https://code.visualstudio.com/): Not to be confused with full Visual Studio, Visual Studio Code (aka VS Code) is a full-featured code editor available for Linux, Mac OS X, and Windows platforms. Small and light-weight, but full-featured, VS Code is open-source, extensible, and configurable for almost any task.
- [PyCharm](https://www.jetbrains.com/pycharm/): One of the best (and only) full-featured, dedicated IDEs for Python is PyCharm. Available in both paid (Professional) and free open-source (Community) editions, PyCharm installs quickly and easily on Windows, Mac OS X, and Linux platforms.
- [Sublime Text](http://www.sublimetext.com/): Written by a Google engineer with a dream for a better text editor, Sublime Text is an extremely popular code editor. Supported on all platforms, Sublime Text has built-in support for Python code editing and a rich set of extensions (called packages) that extend the syntax and editing features.
- [Atom](https://atom.io/): Available on all platforms, Atom is billed as the “hackable text editor for the 21st Century.” With a sleek interface, file system browser, and marketplace for extensions, open-source Atom is built using Electron, a framework for creating desktop applications using JavaScript, HTML, and CSS. Python language support is provided by an extension that can be installed when Atom is running.

## Namestitev VSCode in uporaba

- [Python Development in Visual Studio Code](https://realpython.com/python-development-visual-studio-code/)
- [Setting Up VS Code](https://realpython.com/python-coding-setup-windows/#setting-up-vs-code)
- [Advanced Visual Studio Code for Python Developers](https://realpython.com/advanced-visual-studio-code-python/)
- [Setting Up VSCode For Python: A Complete Guide](https://www.datacamp.com/tutorial/setting-up-vscode-python)
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages and runtimes (such as C++, C#, Java, Python, PHP, Go, .NET).

[Download Visual Studio Code](https://code.visualstudio.com/Download) and install it on your computer.

At its heart, Visual Studio Code is a code editor. Like many other code editors, VS Code adopts a common user interface and layout of an explorer on the left, showing all of the files and folders you have access to, and an editor on the right, showing the content of the files you have opened.

![VSCode User Interface](https://code.visualstudio.com/assets/docs/getstarted/userinterface/hero.png)

By starting VS Code in a folder, that folder becomes your "workspace".

Using a command prompt or terminal, create an empty folder called "hello", navigate into it, and open VS Code (`code`) in that folder (`.`) by entering the following commands:

```
mkdir python-osnovni
cd python-osnovni
code .
```

> Alternately, you can create a folder through the operating system UI, then use VS Code's File > Open Folder to open the project folder.

Install the **Python extension for Visual Studio Code** from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Open the Command Palette (`Ctrl+Shift+P`), start typing `Python: Select Interpreter` command from the Command Palette. Select the local Python interpreter installed previously (ex. `Python 3.13.0`).

From the File Explorer toolbar, select the New File button on the hello folder. Name the file `hello.py`, and VS Code will automatically open it in the editor.

Now that you have a code file in your Workspace, enter the following source code in `hello.py`:

```python
msg = "Roll a dice"
print(msg)
```

When you start typing print, notice how IntelliSense presents auto-completion options.

Click the **Run Python File in Terminal** play button in the top-right side of the editor.

> [Keyboard shortcuts for Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)


Open the integrated terminal in VS Code by selecting View > Terminal from the main menu. Check if you are in the correct folder by typing `pwd` and list the files with `ls`.

Install the dependencies: `pip install ruff`

Install the following extensions for VS Code:
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff)
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

Create a `.vscode` folder in the project root. In the new folder create a file `settings.json`:

```json
{
  "python.languageServer": "Pylance",
  "python.analysis.typeCheckingMode": "basic",
  "python.analysis.diagnosticMode": "workspace",
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.tabSize": 4,
  "editor.codeActionsOnSave": {
      "source.organizeImports.ruff": "explicit",
      "source.addMissingImports": "explicit",
      "source.formatDocument.ruff": "explicit",
      "source.fixAll.ruff": "explicit"
  },
  "ruff.importStrategy": "fromEnvironment",
  "ruff.lint.args": [
      "--select=ALL",
      "--line-length=180",
      "--ignore=N815,S105,D104",
      "--extend-exclude=**/tests/**",
  ],
  "ruff.format.args": [
      "--line-length=135"
  ],
  "python.testing.pytestArgs": [
      "tests"
  ],
  "python.testing.unittestEnabled": false,
  "python.testing.pytestEnabled": true,
}
```

Try to save the file `hello.py` and see what happens.


