Google Python Exercises
=======================

These exercises are taken from the basic exercises section of
[Google's Python Class](https://developers.google.com/edu/python) and
adapted to Python3.

How to install flake8 and check the style of your code
------------------------------------------------------

Pass

List of exercises:
------------------
| file name    | problem   | description                                             | used concepts                |
| :---------:  | :-------: | ------------------------------------------------------- | ---------------------------- |
| string1.py   | string1   | basic string exercises                                  | strings                      |
| string2.py   | string2   | additional string exercises                             | strings                      |
| list1.py     | list1     | basic list exercises                                    | lists                        |
| list2.py     | list2     | additional list exercises                               | lists                        |
| wordcount.py | wordcount | utility to count words in a text file                   | strings, lists, dicts, files |
| mimic.py     | mimic     | utility to mimic writing style based on some other text | strings, lists, dicts, files |

To get started:
---------------
0. Create a [github](https://github.com/) account if you don't have it already
1. Fork this repository

    ![Fork 1](https://github.com/dmalt/Google-python-exercises/blob/main/pics/fork1.png "Fork 1")
    The new repository `Google-python-exercises` should appear on **your** profile page on github.
2. Install git and download the repository code from your fork.

    - Open jupyter notebook and create new Python3 notebook.
    - In the notebook set your Github usename and the problem you want to work on. For example:
        ```python
        github_username = "dmalt"
        problem = "string1"  # problem from the List of exercises
        ```
    - Then, in the notebook execute the following:
        ```bash
        !conda install -c anaconda -y git
        !git clone https://github.com/$github_usename/Google-python-exercises.git
        %cd Google-python-exercises
        !git pull --all
        !git checkout $problem
        ```
    - `<problem>.py` should appear in the `Google-python-exercises` folder. Write your code an submit the solution.

How to submit:
--------------

When submitting, make sure your solution passes all the tests and doesn't have any stylistic errors.
Style check of your code can be done with [flake8](#how-to-install-flake8-and-check-the-style-of-your-code)

