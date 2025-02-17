# learning-python
Sample code for learning Python 3

open a terminal
#Install virtual env
$ pip install virtualenv

#Open a terminal in project root directory and run this command
#This will Create virtual environment. This will create  env directory
#better way is to use python command itself to create virtual environment. see "Note on using PyCharm editor"
$ virtualenv env

#activate virtual environment
$ source env/bin/activate

#To deactivate a virtual environment 
(.venv) $ deactivate
$


You will get into env prompt. Now you are inside virtual environment
Now after this, anything that you install is contained within this env
and will not install globally on your system. Your system is shielded from this env

To verify that you are indeed inside the virtual environment,
run the command
which python
You should get output that points to env folder of your project directory
$ which python
/Users/adiyen/poc/python/learning-python/.venv/bin/python


Install the necessary dependencies in this virtual environment.
(env) is a prompt that indicates you are in virtual environment. It is
not part of the command
$ (env) pip install -r requirements.txt

To check what versions are installed in virtual environment run
$ pip list

You could also use pip freeze command to capture packages currently
installed in the environment and create requirements.txt
$ pip freeze > requirements.txt

Note on using PyCharm editor
-------------------
$mkdir -p ~/poc/python/PySpark-Tutorial
$ cd ~/poc/python/PySpark-Tutorial
$ python -m venv .venv
$ source .venv/bin/activate
prompt changes
(.venv) $ pip install pyspark
(.venv) $ pip install findspark
(.venv) $ pip install jupyterlab #This is not required

Launch jupyter notebook
(.venv) $ jupyter-lab

Dont use jupyterlab. Let us do normal python code itself and use PyCharm. This is best
After doing the above steps , open the project in PyCharm. open a terminal and type which python
It will show global installation. You will also see a link to choose the project specific
python interpreter. click on the link and choose it. close the terminal and open again
you will see virtual env got activated. Typing which python will now correctly display 
the project specific virtual environment

Sometimes IDE may not reflect the settings and you might see error "Invalid Interperter" 
close the editor and reopen it


12 Production-Grade Python Code Styles
----------------------------------
1)Tuple Unpacking

snacks = ["bonda","biscuit"]

#unpacking
(
    first_snack,
    second_snack
) = snacks

print(first_snack)
print(second_snack)



2)List Comprehension

#pick odd numbers from 0 to 9 and square them to create a list
ls = [number ** 2
      for number in range(10)
      if (number % 2 == 1)]
print(ls)

3)Combining strings using brackets

#You dont need + inside brackets
variable1="v1"
variable2="v2"
error="err"
RETRY_INTERVAL = 5

error_log_message = (
"ERROR. Failed to perform computation on " 
f"{variable1=} and {variable2=} "
f"due to the following error: {error}. " 
f"Retrying in {RETRY_INTERVAL} seconds"
)

4)Indexing nested dictionaries
d={
     "data": {
             "num": 1
     }
 }

x = d ["data"] ["num"]
print (x) # 1

5)Writing readable Functions
You should not be writing a function this way

def func(a, b, c, d, e):
# do stuff

A function should have parameter type clues and return type clues and
docString explaining what the function does

def descriptive_function_name ( list_of_names: list[str], 
    list_of_numbers: list[int],
    is_dryrun: bool = True,
) -> list[int]:

    """
    This is the Docstring, and it describes what the function does:
    Args:
    list_of_names (lististrl): list of names used in ... list_of_numbers (list[intl): list of nunbers used in ... is_dryrun (bool): if True, no write operations are performed
    Returns
    (list[int]) a list of numbers that ...
    """
    
    # do stuff
    return [1,2,3]


6)Protection against None
if dog.owner.name=="bob":
    print("This is bob's dog)

if dog is None we get an error
if dog.owner is None, we get an error
How to protect this?
if dog and dog.owner and dog.owner.name == "bob":
    print("This is bob's dog)

protecting a loop 
for item in mylist or []:
    do_stuff(item)

The expression mylist or [] will return mylist if it is truthy (i.e, non-empty)
will return [] if mylist is falsy (None or empty)

7)Decorators for common functionality
Here is a class with 3 functions. They do different things,
but there are similar steps like try-except block and logging
We can move it to a decorator

class def MyClass:
    def func1(self):
        try:
            """code for func1"""
            logger.info("'func1 success")
        except Exception as e:
            logger.error (str(e))

    def func2(self):
        try:
            """code for func2""
            logger.info("'func2 success")
        except Exception as e:
            logger.error (str(e))

    def func3(self):
        try:
            """code for func3"""
            logger. info("'func3 success")
        except Exception as e:
            logger.error (str(e))

We can write a decorator to avoid repeated code

def handle_exception_and_logging(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args,**kwargs)
            logger.info(f"{func.__name__} success")
            return res
        except Exception as e:
            logger.error (str(e))
    return wrapper

Now you can rewrite the class using the decorator

class def MyClass:
    @handle_exception_and_logging
    def func1(self):
        """code for func1"""

    @handle_exception_and_logging
    def func1(self):
        """code for func2"""

    @handle_exception_and_logging
    def func1(self):
        """code for func3"""

8)You can use na object as a method if the class of the object
has defined __call__ method

class Greeting:
    def __init__(self,name:str) -> None:
        self.name = name
    
    def __call__(self,greeting:str) -> str:
        return f"{greeting}, {self.name}"

message = Greeting("Krishna")
text=message("Jai Shri")
print(text)

9)Refer arguments_demo.py for different ways of passing 
arguments to a function