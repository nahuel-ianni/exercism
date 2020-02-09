# Python
>Python is, as Wikipedia goes, a powerful general-purpose high-level programming language. It basically means that it can be used to write a wide variety of different kinds of software, from videogames to HTTP servers to command-line tools.
One of the main characteristics that differentiates Python from other programming languages is its strong emphasis on readability and code cleaness. In fact, differently from other languages like JavaScript or C++, in Python code indentation has a syntactical meaning and you are forced to chose and adhere to a writing style (e.g. don't mix tabs and spaces for identation; don't use two spaces where you should use four etc.). Yes, forced: the Python interpreter will raise SyntaxErrors if it recognize wrong indentation.
This might look like a limit at the beginning but, as you will advance in your learning path, you'll realize that enforcing this behaviour will make your code slim and more readable by default.
For its own nature, exercism assumes that you already have a grasp of the language syntax before starting doing exercises. At least at a point where you can write simple functions in Python. From there on, you can continue your learning as you will advance in the exercism track and gradually explore new constructs and concepts.
With this premise, a good, beginner friendly, starting point for those who don't have any experience in other languages might be the Python course on Sololearn.com. It will help you get an understanding of the Python syntax with which you will be able to start solving exercises here on exercism.

## Installing Python
If Python isn't already available on your system, follow the instructions found at the official [Python site](https://www.python.org/) to install it on your computer.

## Test management
Exercism recommends installing [pytest](https://pypi.org/project/pytest/) and [pytest-cache](https://pypi.org/project/pytest-cache/). Pytest is a testing tool that will give you more flexibility over running your unit tests.

To install pytest, run the following command:

```pip3 install --user pytest pytest-cache```

*The ``--user`` parameter might be skipped based on user needs.*

### Running the tests
Pytest can easily execute all tests in a file by executing the `pytest` command from the test file's directory.

If you want to execute all tests on a particular file, the command accepts a path as a parameter: `pytest <filename>.py`.

### Debugging in Python
Python introduces built in breakpoint functionalities via the [PEP-0553](https://www.python.org/dev/peps/pep-0553/) specification.

This PEP proposes adding a new built-in function called `breakpoint()` which enters a Python debugger at the point of the call and allows the user to pause execution and inspect elements or change values executing on the current session.

When your code hits one of the `breakpoint()` statements, you can interact with the script with several different [debugger commands](https://docs.python.org/2/library/pdb.html), such as:

- `c` continue execution
- `n` step to the next line within the same function
- `s` step to the next line in this function or a called function
- `q` quit the debugger/execution
- `locals()` shows all local variables in the environment
- `vars(object)` shows all relevant info on the inspected object
- `exit()` (or *CTRL + D*) sets and interrupt
- *CTRL + C* sends a cancelation command to the console 

---

## Helpful resources
- [The Python standard library](https://docs.python.org/3/library/index.html)
- [List comprehension](https://realpython.com/list-comprehension-python/)

  - `new_list = [expression for member in iterable]`
  - `new_list = [expression for member in iterable (if conditional)]`
  - `new_list = [expression (if conditional) for member in iterable]`
- [Equivalent Linq methods in Python](https://www.markheath.net/post/python-equivalents-of-linq-methods)