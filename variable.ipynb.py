{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Variables, Strings, and Numbers\n",
    "===\n",
    "In this section, you will learn to store information in variables. You will learn about two types of data: strings, which are sets of characters, and numerical data types."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Previous: Hello World](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/hello_world.ipynb) | \n",
    "[Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) | \n",
    "[Next: Lists and Tuples](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/lists_tuples.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Contents\n",
    "---\n",
    "- [Variables](#Variables)\n",
    "    - [Example](#Example)\n",
    "    - [Naming rules](#Naming-rules)\n",
    "    - [NameError](#NameError)\n",
    "    - [Exercises](#Exercises-variables)\n",
    "- [Strings](#Strings)\n",
    "    - [Single and double quotes](#Single-and-double-quotes)\n",
    "    - [Changing case](#Changing-case)\n",
    "    - [Combining strings (concatenation)](#Combining-strings-(concatenation))\n",
    "    - [Whitespace](#Whitespace)\n",
    "    - [Exercises](#Exercises-strings)\n",
    "- [Numbers](#Numbers)\n",
    "    - [Integer operations](#Integer-operations)\n",
    "    - [Floating-point numbers](#Floating-point-numbers)\n",
    "    - [Integers in Python 2.7](#Integers-in-Python-2.7)\n",
    "    - [Exercises](#Exercises-numbers)\n",
    "    - [Challenges](#Challenges-numbers)\n",
    "- [Comments](#Comments)\n",
    "    - [What makes a good comment?](#What-makes-a-good-comment?)\n",
    "    - [When should you write comments?](#When-should-you-write-comments?)\n",
    "    - [Exercises](#Exercises-comments)\n",
    "- [Zen of Python](#Zen-of-Python)\n",
    "- [Overall Challenges](#Overall-Challenges)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Variables\n",
    "===\n",
    "A variable holds a value."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Example\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Pythn world!\n"
     ]
    }
   ],
   "source": [
    "message = \"Hello Pythn world!\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A variable holds a value. You can change the value of a variable at any point."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello Python world!\n",
      "Python is my favorite language!\n"
     ]
    }
   ],
   "source": [
    "###highlight=[5,6]\n",
    "message = \"Hello Python world!\"\n",
    "print(message)\n",
    "\n",
    "message = \"Python is my favorite language!\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Naming rules\n",
    "---\n",
    "- Variables can only contain letters, numbers, and underscores. Variable names can start with a letter or an underscore, but can not start with a number.\n",
    "- Spaces are not allowed in variable names, so we use underscores instead of spaces. For example, use student_name instead of \"student name\".\n",
    "- You cannot use [Python keywords](http://docs.python.org/3/reference/lexical_analysis.html#keywords) as variable names.\n",
    "- Variable names should be descriptive, without being too long. For example mc_wheels is better than just \"wheels\", and number_of_wheels_on_a_motorycle.\n",
    "- Be careful about using the lowercase letter l and the uppercase letter O in places where they could be confused with the numbers 1 and 0."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "NameError\n",
    "---\n",
    "There is one common error when using variables, that you will almost certainly encounter at some point. Take a look at this code, and see if you can figure out why it causes an error."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 320,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for sharing Python with the world, Guido!\n"
     ]
    }
   ],
   "source": [
    "message = \"Thank you for sharing Python with the world, Guido!\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's look through this error message. First, we see it is a NameError. Then we see the file that caused the error, and a green arrow shows us what line in that file caused the error. Then we get some more specific feedback, that \"name 'mesage' is not defined\".\n",
    "\n",
    "You may have already spotted the source of the error. We spelled message two different ways. Python does not care whether we use the variable name \"message\" or \"mesage\". Python only cares that the spellings of our variable names match every time we use them.\n",
    "\n",
    "This is pretty important, because it allows us to have a variable \"name\" with a single name in it, and then another variable \"names\" with a bunch of names in it.\n",
    "\n",
    "We can fix NameErrors by making sure all of our variable names are spelled consistently."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 321,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Thank you for sharing Python with the world, Guido!\n"
     ]
    }
   ],
   "source": [
    "###highlight=[3]\n",
    "message = \"Thank you for sharing Python with the world, Guido!\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In case you didn't know [Guido](http://en.wikipedia.org/wiki/Guido_van_Rossum) [van Rossum](http://www.python.org/~guido/) created the Python language over 20 years ago, and he is considered Python's [Benevolent Dictator for Life](http://en.wikipedia.org/wiki/Benevolent_Dictator_for_Life). Guido still signs off on all major changes to the core Python language."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Exercises-variables\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Hello World - variable\n",
    "\n",
    "- Store your own version of the message \"Hello World\" in a variable, and print it.\n",
    "\n",
    "#### One Variable, Two Messages:\n",
    "- Store a message in a variable, and then print that message.\n",
    "- Store a new message in the same variable, and then print that new message."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[top](#)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 322,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "a = \"Hello World\"\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Strings\n",
    "===\n",
    "Strings are sets of characters. Strings are easier to understand by looking at some examples."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Single and double quotes\n",
    "---\n",
    "Strings are contained by either single or double quotes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 323,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "my_string = \"This is a double-quoted string.\"\n",
    "my_string = 'This is a single-quoted string.'"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This lets us make strings that contain quotations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "quote = \"Linus Torvalds once said, 'Any program is only as good as it is useful.'\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Changing case\n",
    "---\n",
    "You can easily change the case of a string, to present it the way you want it to look."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eric\n",
      "Eric\n"
     ]
    }
   ],
   "source": [
    "first_name = 'eric'\n",
    "\n",
    "print(first_name)\n",
    "print(first_name.title())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It is often good to store data in lower case, and then change the case as you want to for presentation. This catches some TYpos. It also makes sure that 'eric', 'Eric', and 'ERIC' are not considered three different people.\n",
    "\n",
    "Some of the most common cases are lower, title, and upper."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 326,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eric\n",
      "Eric\n",
      "ERIC\n",
      "eric\n"
     ]
    }
   ],
   "source": [
    "###highlight=[6,8,9]\n",
    "first_name = 'eric'\n",
    "\n",
    "print(first_name)\n",
    "print(first_name.title())\n",
    "print(first_name.upper())\n",
    "\n",
    "first_name = 'Eric'\n",
    "print(first_name.lower())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You will see this syntax quite often, where a variable name is followed by a dot and then the name of an action, followed by a set of parentheses. The parentheses may be empty, or they may contain some values.\n",
    "\n",
    "variable_name.action()\n",
    "\n",
    "In this example, the word \"action\" is the name of a method. A method is something that can be done to a variable. The methods 'lower', 'title', and 'upper' are all functions that have been written into the Python language, which do something to strings. Later on, you will learn to write your own methods."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Combining strings (concatenation)\n",
    "---\n",
    "It is often very useful to be able to combine strings into a message or page element that we want to display. Again, this is easier to understand through an example."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 327,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ada Lovelace\n"
     ]
    }
   ],
   "source": [
    "first_name = 'ada'\n",
    "last_name = 'lovelace'\n",
    "\n",
    "full_name = first_name + ' ' + last_name\n",
    "\n",
    "print(full_name.title())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The plus sign combines two strings into one, which is called \"concatenation\". You can use as many plus signs as you want in composing messages. In fact, many web pages are written as giant strings which are put together through a long series of string concatenations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 328,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ada Lovelace was considered the world's first computer programmer.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[6,7,8]\n",
    "first_name = 'ada'\n",
    "last_name = 'lovelace'\n",
    "full_name = first_name + ' ' + last_name\n",
    "\n",
    "message = full_name.title() + ' ' + \"was considered the world's first computer programmer.\"\n",
    "\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you don't know who Ada Lovelace is, you might want to go read what [Wikipedia](http://en.wikipedia.org/wiki/Ada_Lovelace) or the [Computer History Museum](http://www.computerhistory.org/babbage/adalovelace/) have to say about her. Her life and her work are also the inspiration for the [Ada Initiative](http://adainitiative.org/faq/about-ada-lovelace/), which supports women who are involved in technical fields."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Whitespace\n",
    "---\n",
    "The term \"whitespace\" refers to characters that the computer is aware of, but are invisible to readers. The most common whitespace characters are spaces, tabs, and newlines.\n",
    "\n",
    "Spaces are easy to create, because you have been using them as long as you have been using computers. Tabs and newlines are represented by special character combinations.\n",
    "\n",
    "The two-character combination \"\\t\" makes a tab appear in a string. Tabs can be used anywhere you like in a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello everyone!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello everyone!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\tHello everyone!\n"
     ]
    }
   ],
   "source": [
    "print(\"\\tHello everyone!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \teveryone!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\teveryone!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The combination \"\\n\" makes a newline appear in a string. You can use newlines anywhere you like in a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 332,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello everyone!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello everyone!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 333,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Hello everyone!\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nHello everyone!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 334,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello \n",
      "everyone!\n"
     ]
    }
   ],
   "source": [
    "print(\"Hello \\neveryone!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\n",
      "Hello everyone!\n"
     ]
    }
   ],
   "source": [
    "print(\"\\n\\n\\nHello everyone!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###Stripping whitespace\n",
    "\n",
    "Many times you will allow users to enter text into a box, and then you will read that text and use it. It is really easy for people to include extra whitespace at the beginning or end of their text. Whitespace includes spaces, tabs, and newlines.\n",
    "\n",
    "It is often a good idea to strip this whitespace from strings before you start working with them. For example, you might want to let people log in, and you probably want to treat 'eric ' as 'eric' when you are trying to see if I exist on your system.\n",
    "\n",
    "You can strip whitespace from the left side, the right side, or both sides of a string."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 336,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "eric \n",
      " eric\n",
      "eric\n"
     ]
    }
   ],
   "source": [
    "name = ' eric '\n",
    "\n",
    "print(name.lstrip())\n",
    "print(name.rstrip())\n",
    "print(name.strip())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's hard to see exactly what is happening, so maybe the following will make it a little more clear:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 337,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-eric -\n",
      "- eric-\n",
      "-eric-\n"
     ]
    }
   ],
   "source": [
    "name = ' eric '\n",
    "\n",
    "print('-' + name.lstrip() + '-')\n",
    "print('-' + name.rstrip() + '-')\n",
    "print('-' + name.strip() + '-')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Exercises-strings\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Someone Said\n",
    "- Find a quote that you like. Store the quote in a variable, with an appropriate introduction such as \"Ken Thompson once said, 'One of my most productive days was throwing away 1000 lines of code'\". Print the quote.\n",
    "\n",
    "#### First Name Cases\n",
    "- Store your first name, in lowercase, in a variable.\n",
    "- Using that one variable, print your name in lowercase, Titlecase, and UPPERCASE.\n",
    "\n",
    "#### Full Name\n",
    "- Store your first name and last name in separate variables, and then combine them to print out your full name.\n",
    "\n",
    "#### About This Person\n",
    "- Choose a person you look up to. Store their first and last names in separate variables.\n",
    "- Use concatenation to make a sentence about this person, and store that sentence in a variable.-\n",
    "- Print the sentence.\n",
    "\n",
    "#### Name Strip\n",
    "- Store your first name in a variable, but include at least two kinds of whitespace on each side of your name.\n",
    "- Print your name as it is stored.\n",
    "- Print your name with whitespace stripped from the left side, then from the right side, then from both sides."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[top](#)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 338,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n",
      "Martin Luther King a dit : \"L'obscurité ne peut pas chasser l'obscurité, seule la lumière le peut. La haine ne peut pas chasser la haine, seul l'amour le peut.\n",
      "Aissa\n",
      "AISSA\n",
      "aissa\n",
      "aissa moustaine\n",
      "Martin Luther King est un homme politique\n",
      " aissa  \n",
      "aissa  \n",
      " aissa\n",
      "aissa\n"
     ]
    }
   ],
   "source": [
    "a = \"Hello World\"\n",
    "print(a)\n",
    "\n",
    "citation = \"Martin Luther King a dit : \\\"L'obscurité ne peut pas chasser l'obscurité, seule la lumière le peut. La haine ne peut pas chasser la haine, seul l'amour le peut.\"\n",
    "print(citation)\n",
    "\n",
    "x = \"aissa\"\n",
    "print(x.title())\n",
    "print(x.upper())\n",
    "print(x.lower())\n",
    "\n",
    "\n",
    "y = \"aissa\"\n",
    "h = \"moustaine\"\n",
    "full_name = y + \" \" + h\n",
    "print(full_name)\n",
    "\n",
    "a = \"Martin\"\n",
    "b = \"Luther King\"\n",
    "h = a + \" \" + b + \" \" + \"est un homme politique\"\n",
    "print(h)\n",
    "\n",
    "\n",
    "a = \" aissa  \"\n",
    "print(a)\n",
    "print(a.lstrip())\n",
    "print(a.rstrip())\n",
    "print(a.strip())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Numbers\n",
    "===\n",
    "Dealing with simple numerical data is fairly straightforward in Python, but there are a few things you should know about."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Integers\n",
    "---\n",
    "You can do all of the basic operations with integers, and everything should behave as you expect. Addition and subtraction use the standard plus and minus symbols. Multiplication uses the asterisk, and division uses a forward slash. Exponents use two asterisks."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 339,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "print(3+2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 340,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "print(3-2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 341,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "print(3*2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 342,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.5\n"
     ]
    }
   ],
   "source": [
    "print(3/2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 343,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "print(3**2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can use parenthesis to modify the standard order of operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 344,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14\n"
     ]
    }
   ],
   "source": [
    "standard_order = 2+3*4\n",
    "print(standard_order)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 345,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "my_order = (2+3)*4\n",
    "print(my_order)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Floating-Point numbers\n",
    "---\n",
    "Floating-point numbers refer to any number with a decimal point. Most of the time, you can think of floating point numbers as decimals, and they will behave as you expect them to."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 346,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.2\n"
     ]
    }
   ],
   "source": [
    "print(0.1+0.1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "However, sometimes you will get an answer with an unexpectly long decimal part:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 347,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.30000000000000004\n"
     ]
    }
   ],
   "source": [
    "print(0.1+0.2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This happens because of the way computers represent numbers internally; this has nothing to do with Python itself. Basically, we are used to working in powers of ten, where one tenth plus two tenths is just three tenths. But computers work in powers of two. So your computer has to represent 0.1 in a power of two, and then 0.2 as a power of two, and express their sum as a power of two. There is no exact representation for 0.3 in powers of two, and we see that in the answer to 0.1+0.2.\n",
    "\n",
    "Python tries to hide this kind of stuff when possible. Don't worry about it much for now; just don't be surprised by it, and know that we will learn to clean up our results a little later on.\n",
    "\n",
    "You can also get the same kind of result with other operations."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 348,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.30000000000000004\n"
     ]
    }
   ],
   "source": [
    "print(3*0.1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Integers in Python 2.7\n",
    "---\n",
    "There are a couple differences in the way Python 2 and Python 3 handle numbers. In Python 2, dividing two integers always results in an integer, while Python 3 always returns a float. This is fine when the result of your integer division is an integer, but it leads to quite different results when the answer is a decimal."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Division in Python 2.7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.0\n"
     ]
    }
   ],
   "source": [
    "# Python 2.7\n",
    "print(4/2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 350,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.5\n"
     ]
    }
   ],
   "source": [
    "# Python 2.7\n",
    "print(3/2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Division in Python 3.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 351,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.0\n"
     ]
    }
   ],
   "source": [
    "# Python 3.3\n",
    "print(4/2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 352,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.5\n"
     ]
    }
   ],
   "source": [
    "# Python 3.3\n",
    "print(3/2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you are getting numerical results that you don't expect, or that don't make sense, check if the version of Python you are using is treating integers differently than you expect."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Exercises-numbers\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Arithmetic\n",
    "- Write a program that prints out the results of at least one calculation for each of the basic operations: addition, subtraction, multiplication, division, and exponents.\n",
    "\n",
    "#### Order of Operations\n",
    "- Find a calculation whose result depends on the order of operations.\n",
    "- Print the result of this calculation using the standard order of operations.\n",
    "- Use parentheses to force a nonstandard order of operations. Print the result of this calculation.\n",
    "\n",
    "#### Long Decimals\n",
    "- On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004.\n",
    "- Find at least one other calculation that results in a long decimal like this.\n",
    "\n",
    "#### Python 2 or Python 3?\n",
    "- Use integer division to show whether your Python interpeter is using Python 2 or Python 3."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 389,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "-2\n",
      "28\n",
      "2.0\n",
      "8\n",
      "17\n",
      "25\n",
      "0.30000000000000004\n"
     ]
    }
   ],
   "source": [
    "print(2+2)\n",
    "print(5-7)\n",
    "print(7*4)\n",
    "print(6/3)\n",
    "print(2**3)\n",
    "\n",
    "print(2+3*5)\n",
    "print((2+3)*5)\n",
    "\n",
    "print(0.10+0.20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Challenges-numbers\">\n",
    "Challenges\n",
    "---\n",
    "#### Neat Arithmetic\n",
    "\n",
    "- Store the results of at least 5 different calculations in separate variables. Make sure you use each operation at least once.\n",
    "- Print a series of informative statements, such as \"The result of the calculation 5+7 is 12.\"\n",
    "\n",
    "#### Neat Order of Operations\n",
    "- Take your work for \"Order of Operations\" above.\n",
    "- Instead of just printing the results, print an informative summary of the results. Show each calculation that is being done and the result of that calculation. Explain how you modified the result using parentheses.\n",
    "\n",
    "#### Long Decimals - Pattern\n",
    "- On paper, 0.1+0.2=0.3. But you have seen that in Python, 0.1+0.2=0.30000000000000004.\n",
    "- Find a number of other calculations that result in a long decimal like this. Try to find a pattern in what kinds of numbers will result in long decimals.\n",
    "\n",
    "#### Python 2 and Python 3\n",
    "- Find a way to make your computer interpret 3/2 once in Python 2, and once in Python 3.\n",
    "- (HINT) Don't spend too much time on this, unless you like reading on forums about installing from packages and what not.\n",
    "\n",
    "    If you just want to play around with Python 2 and Python 3, you can easily do so on [pythontutor.com](http://pythontutor.com/). Click \"Start using Online Python Tutor now\", and then delete the sample code in the text box so you can enter your own code. On that page, there is a drop-down list just below the text box that lets you select different versions of Python. Click \"Visualize Execution\" to run your code. On the next page, you can either click \"Forward\" to step through your code one line at a time, or click \"Last\" to run your entire program."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 421,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "le résultat de 3+2 est égale à 5\n",
      "le résultat de 5*3 est égale à 15\n",
      "le résultat de 9-6 est égale à 3\n",
      "le résultat de 4/2 est égale à 2.0\n",
      "le résultat de 2**4 est égale à 16\n",
      "C'est la multiplication qui est prioritaire ensuite le reste\n",
      "On ajoute des parenthèses a 5+2 car l'addtion n'est prioritaire\n"
     ]
    }
   ],
   "source": [
    "a = 3+2\n",
    "b = 5*3\n",
    "c = 9-6\n",
    "d = 4/2\n",
    "e = 2**4\n",
    "\n",
    "print(f\"le résultat de 3+2 est égale à {a}\")\n",
    "print(f\"le résultat de 5*3 est égale à {b}\")\n",
    "print(f\"le résultat de 9-6 est égale à {c}\")\n",
    "print(f\"le résultat de 4/2 est égale à {d}\")\n",
    "print(f\"le résultat de 2**4 est égale à {e}\")\n",
    "\n",
    "x = 5+2*2\n",
    "print(\"C'est la multiplication qui est prioritaire ensuite le reste\")\n",
    "x = (5+2)*2\n",
    "print(\"On ajoute des parenthèses a 5+2 car l'addtion n'est pas prioritaire\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[top](#)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Comments\n",
    "===\n",
    "As you begin to write more complicated code, you will have to spend more time thinking about how to code solutions to the problems you want to solve. Once you come up with an idea, you will spend a fair amount of time troubleshooting your code, and revising your overall approach.\n",
    "\n",
    "Comments allow you to write in English, within your program. In Python, any line that starts with a pound (#) symbol is ignored by the Python interpreter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 422,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This line is not a comment, it is code.\n"
     ]
    }
   ],
   "source": [
    "# This line is a comment.\n",
    "print(\"This line is not a comment, it is code.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What makes a good comment?\n",
    "---\n",
    "- It is short and to the point, but a complete thought. Most comments should be written in complete sentences.\n",
    "- It explains your thinking, so that when you return to the code later you will understand how you were approaching the problem.\n",
    "- It explains your thinking, so that others who work with your code will understand your overall approach to a problem.\n",
    "- It explains particularly difficult sections of code in detail.\n",
    "\n",
    "When should you write comments?\n",
    "---\n",
    "- When you have to think about code before writing it.\n",
    "- When you are likely to forget later exactly how you were approaching a problem.\n",
    "- When there is more than one way to solve a problem.\n",
    "- When others are unlikely to anticipate your way of thinking about a problem.\n",
    "\n",
    "Writing good comments is one of the clear signs of a good programmer. If you have any real interest in taking programming seriously, start using comments now. You will see them throughout the examples in these notebooks."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Exercises-comments\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### First Comments\n",
    "- Choose the longest, most difficult, or most interesting program you have written so far. Write at least one comment in your program.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[top](#)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Zen of Python\n",
    "===\n",
    "The Python community is incredibly large and diverse. People are using Python in science, in medicine, in robotics, on the internet, and in any other field you can imagine. This diverse group of thinkers has developed a collective mindset about how programs should be written. If you want to understand Python and the community of Python programmers, it is a good idea to learn the ways Python programmers think.\n",
    "\n",
    "You can easily see a set of guiding principles that is written right into the language:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 423,
   "metadata": {},
   "outputs": [],
   "source": [
    "import this"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "There is a lot here. Let's just take a few lines, and see what they mean for you as a new programmer.\n",
    "\n",
    "    Beautiful is better than ugly.\n",
    "\n",
    "Python programmers recognize that good code can actually be beautiful. If you come up with a particularly elegant or efficient way to solve a problem, especially a difficult problem, other Python programmers will respect your work and may even call it beautiful. There is beauty in high-level technical work.\n",
    "\n",
    "    Explicit is better than implicit.\n",
    "\n",
    "It is better to be clear about what you are doing, than come up with some shorter way to do something that is difficult to understand.\n",
    "\n",
    "    Simple is better than complex.\n",
    "    Complex is better than complicated.\n",
    "\n",
    "Keep your code simple whenever possible, but recognize that we sometimes take on really difficult problems for which there are no easy solutions. In those cases, accept the complexity but avoid complication.\n",
    "\n",
    "    Readability counts.\n",
    "\n",
    "There are very few interesting and useful programs these days that are written and maintained entirely by one person. Write your code in a way that others can read it as easily as possible, and in a way that you will be able to read and understand it 6 months from now. This includes writing good comments in your code.\n",
    "\n",
    "    There should be one-- and preferably only one --obvious way to do it.\n",
    "\n",
    "There are many ways to solve most problems that come up in programming. However, most problems have a standard, well-established approach. Save complexity for when it is needed, and solve problems in the most straightforward way possible.\n",
    "\n",
    "    Now is better than never.\n",
    "\n",
    "No one ever writes perfect code. If you have an idea you want to implement it, write some code that works. Release it, let it be used by others, and then steadily improve it."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[top](#)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Overall Challenges\n",
    "===\n",
    "We have learned quite a bit so far about programming, but we haven't learned enough yet for you to go create something. In the next notebook, things will get much more interesting, and there will be a longer list of overall challenges.\n",
    "\n",
    "<blank>\n",
    "\n",
    "#### What I've Learned\n",
    "- Write a program that uses everything you have learned in this notebook at least once.\n",
    "- Write comments that label each section of your program.\n",
    "- For each thing your program does, write at least one line of output that explains what your program did.\n",
    "- For example, you might have one line that stores your name with some whitespace in a variable, and a second line that strips that whitespace from your name:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 424,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I can strip tabs from my name: eric\n"
     ]
    }
   ],
   "source": [
    "# I learned how to strip whitespace from strings.\n",
    "name = '\\t\\teric'\n",
    "print(\"I can strip tabs from my name: \" + name.strip())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    \n",
    "#### Exploring the Python Community\n",
    "\n",
    "As I have said earlier, the Python community is incredibly rich and diverse. Here are a couple resources to look at, if you want to do some exploring.\n",
    "\n",
    "- [The Python website](http://python.org/)\n",
    "\n",
    "    The main Python website is probably not of too much interest to you at this point, but it is a great resource to know about as you start to learn more.\n",
    "    \n",
    "<!-- -->\n",
    "\n",
    "- [PyCon](https://us.pycon.org/)\n",
    "\n",
    "    The Python Conference (PyCon) is an incredible event, and the community is entirely welcoming to new programmers. They happen all over the world, throughout the year. If you can make your way to one of these conferences, you will learn a great deal and meet some really interesting people.\n",
    "\n",
    "<!-- -->\n",
    "    \n",
    "- [PyLadies](http://www.pyladies.com/)\n",
    "\n",
    "    Women and minorities are still under-represented in most technology fields, and the programming world is no different in this regard. That said, the Python community may well be the most welcoming and supportive programming community for women and minorities. There are a number of groups dedicated to bringing women and minorities together around programming in Python, and there are a number of explicit Codes of Conduct for Python-related events.\n",
    "\n",
    "    PyLadies is one of the most visible of these organizations. They are a great resource, so go see what they do and what they have to offer.\n",
    "\n",
    "<!-- -->\n",
    "    \n",
    "- [Python User Groups](https://wiki.python.org/moin/LocalUserGroups)\n",
    "\n",
    "    Wherever there are a number of Python programmers, they will find a way to get together. Python user groups are regular meetings of Python users from a local area. Go take a look at the list of user groups, and see if there is one near you."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[top](#)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- - -\n",
    "[Previous: Hello World](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/hello_world.ipynb) | \n",
    "[Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) | \n",
    "[Next: Lists and Tuples](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/lists_tuples.ipynb)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "position": {
    "height": "144.85px",
    "left": "1537px",
    "right": "20px",
    "top": "19px",
    "width": "350px"
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": true
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
