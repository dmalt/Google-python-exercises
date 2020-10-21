Google Python Exercises
=======================

These exercises are taken from the basic exercises section of
[Google's Python Class](https://developers.google.com/edu/python) and
adapted to Python3.



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

---

Contents
========

1. [Preparation steps](#preparation-steps)
2. [How to start a new problem](#how-to-start-a-new-problem)
3. [How to submit](#how-to-submit)
4. [How to edit submission](#how-to-edit-submission)
5. [How to install flake8 and check the style of your code](#how-to-install-flake8-and-check-the-style-of-your-code)
6. [How the submission is checked?](#how-the-submission-is-checked)

Preparation steps
-----------------
1. Create a [github](https://github.com/) account if you don't have it already
2. Fork this repository

    ![Fork 1](https://github.com/dmalt/Google-python-exercises/blob/main/pics/fork1.png "Fork 1")
    The new repository `Google-python-exercises` should appear on **your** profile page on github.
3. Install git.
    - Open jupyter notebook and create new Python3 notebook.
    - Then, in the created notebook execute the following:

        ```bash
        !conda install -c anaconda -y git
        ```

How to start a new problem:
---------------------------

1. In the notebook set your Github usename and the problem you want to work on. For example:
    ```python
    github_username = "dmalt"  # <-- change this to your Github username
    problem = "string1"  # problem from the List of exercises
    ```

2. Then, in the notebook execute the following:
    ```bash
    !git clone -b {problem} https://github.com/{github_usename}/Google-python-exercises.git {problem}
    ```

3. `<problem>` folder with a file `<problem>.py` will appear. To change directory to `<problem>` run

    ```bash
    %cd {problem}
    ```

4. Write your code in `<problem>.py` an submit the solution.


How to submit:
--------------

1. When submitting, make sure your solution passes all the tests at the bottom of the script and
conform to [PEP8 style conventions](https://www.python.org/dev/peps/pep-0008/).  
Style check of your code should be done with [flake8](#how-to-install-flake8-and-check-the-style-of-your-code).
2. Upload your changes to Github.

    For that you must do 3 things:
    - Add your changes to git
    - Commit the changes.
    - Push the changes to Github

    Perform all three steps running the following in jupyter notebook:
    ```bash
    !git add {problem}.py
    !git commit --message 'Submitting problem'
    !git push
    ```

    Note that `git commit` command requires a commit message. This message is a description of the changes you make.  
    You can write your own message or just use the one above.

3. Create a pull request (PR) from your version of repository on Github

    - Go to Google-python-exercises repository on **your** github page and lick `Compare & pull request`:
    ![PR 1](https://github.com/dmalt/Google-python-exercises/blob/main/pics/PR1.png)
    - On the next screen click `Create pull request`.
    ![PR 2](https://github.com/dmalt/Google-python-exercises/blob/main/pics/PR2.png)
    - You will be redirected to your PR page, where you'll see running code checks
    ![PR 3](https://github.com/dmalt/Google-python-exercises/blob/main/pics/PR3.png)
    - After some time the checks will complete. If the result is `All checks have passed`, the code is good to be reviewed.  
    Otherwise you should [edit](#how-to-edit-submission) your submission so all the tests are successful.


How to edit submission
----------------------

Chances are you'll have to make some edits to your submission after
some tests fail or after the code review. To edit your submission:

1. Make edits to your `<problem>.py`
2. Upload them the same way as in [How to submit](#how-to-submit) section
3. No action here :) Your PR will update automatically

---

How to install flake8 and check the style of your code
------------------------------------------------------
In jupyter notebook run:

```bash
!conda install -c anaconda -y flake8
!flake8 {problem} --count --max-complexity=10 --max-line-length=80 --statistics --show-source
```

**NOTE** that your `problem` variable must be set for your notebook!


How the submission is checked?
-----------------------------

Each submission undergoes automatic testing followed by the manual code review.

Automatic tests include:
- correctness check with automatic tests most of which are listed at the bottom of each `<problem>.py` file.
- style check performed with flake8

Manual code review focusses on:
- Discovering bugs which were not revaled with the automatic tests
- Correcting program structure and style drawbacks (bad variable naming, unnecessary nesting and so on)
- Pointing out potentially more optimal solutions
