{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Dictionaries\n",
    "===\n",
    "Dictionaries allow us to store connected bits of information. For example, you might store a person's name and age together."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[Previous: Basic Terminal Apps](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/terminal_apps.ipynb) | \n",
    "[Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) |\n",
    "[Next: More Functions](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/more_functions.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Contents\n",
    "===\n",
    "- [What are dictionaries?](#What-are-dictionaries?)\n",
    "    - [General Syntax](#General-Syntax)\n",
    "    - [Example](#Example)\n",
    "    - [Exercises](#Exercises-what)\n",
    "- [Common operations with dictionaries](#Common-operations-with-dictionaries)\n",
    "    - [Adding new key-value pairs](#Adding-new-key-value-pairs)\n",
    "    - [Modifying values in a dictionary](#Modifying-values-in-a-dictionary)\n",
    "    - [Removing key-value pairs](#Removing-key-value-pairs)\n",
    "    - [Modifying keys in a dictionary](#Modifying-keys-in-a-dictionary)\n",
    "    - [Exercises](#Exercises-operations)\n",
    "- [Looping through a dictionary](#Looping-through-a-dictionary)\n",
    "    - [Looping through all key-value pairs](#Looping-through-all-key-value-pairs)\n",
    "    - [Looping through all keys in a dictionary](#Looping-through-all-keys-in-a-dictionary)\n",
    "    - [Looping through all values in a dictionary](#Looping-through-all-values-in-a-dictionary)\n",
    "    - [Looping through a dictionary in order](#Looping-through-a-dictionary-in-order)\n",
    "    - [Exercises](#Exercises-looping)\n",
    "- [Nesting](#Nesting)\n",
    "    - [Lists in a dictionary](#Lists-in-a-dictionary)\n",
    "    - [Dictionaries in a dictionary](#Dictionaries-in-a-dictionary)\n",
    "    - [An important note about nesting](#An-important-note-about-nesting)\n",
    "    - [Exercises](#Exercises-nesting)\n",
    "- [Overall Challenges](#Overall-Challenges)"
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
    "What are dictionaries?\n",
    "===\n",
    "Dictionaries are a way to store information that is connected in some way. Dictionaries store information in *key-value* pairs, so that any one piece of information in a dictionary is connected to at least one other piece of information.\n",
    "\n",
    "Dictionaries do not store their information in any particular order, so you may not get your information back in the same order you entered it."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "General Syntax\n",
    "---\n",
    "A general dictionary in Python looks something like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "dictionary_name = {key_1: value_1, key_2: value_2, key_3: value_3}"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since the keys and values in dictionaries can be long, we often write just one key-value pair on a line. You might see dictionaries that look more like this:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "dictionary_name = {key_1: value_1,\n",
    "                   key_2: value_2,\n",
    "                   key_3: value_3,\n",
    "                   }"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is a bit easier to read, especially if the values are long."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Example\n",
    "---\n",
    "A simple example involves modeling an actual dictionary."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can get individual items out of the dictionary, by giving the dictionary's name, and the key in square brackets:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Word: list\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n",
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "print(\"\\nWord: %s\" % 'list')\n",
    "print(\"Meaning: %s\" % python_words['list'])\n",
    "      \n",
    "print(\"\\nWord: %s\" % 'dictionary')\n",
    "print(\"Meaning: %s\" % python_words['dictionary'])\n",
    "\n",
    "print(\"\\nWord: %s\" % 'function')\n",
    "print(\"Meaning: %s\" % python_words['function'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This code looks pretty repetitive, and it is. Dictionaries have their own for-loop syntax, but since there are two kinds of information in dictionaries, the structure is a bit more complicated than it is for lists. Here is how to use a for loop with a dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "Word: list\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Print out the items in the dictionary.\n",
    "for word, meaning in python_words.items():\n",
    "    print(\"\\nWord: %s\" % word)\n",
    "    print(\"Meaning: %s\" % meaning)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The output is identical, but we did it in 3 lines instead of 6. If we had 100 terms in our dictionary, we would still be able to print them out with just 3 lines.\n",
    "\n",
    "The only tricky part about using for loops with dictionaries is figuring out what to call those first two variables. The general syntax for this for loop is:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "for key_name, value_name in dictionary_name.items():\n",
    "    print(key_name) # The key is stored in whatever you called the first variable.\n",
    "    print(value_name) # The value associated with that key is stored in your second variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Exercises-what\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Pet Names\n",
    "- Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.\n",
    "    - For example, 'ziggy': 'canary'\n",
    "- Put at least 3 key-value pairs in your dictionary.\n",
    "- Use a for loop to print out a series of statements such as \"Willie is a dog.\"\n",
    "\n",
    "#### Polling Friends\n",
    "- Think of a question you could ask your friends. Create a dictionary where each key is a person's name, and each value is that person's response to your question.\n",
    "- Store at least three responses in your dictionary.\n",
    "- Use a for loop to print out a series of statements listing each person's name, and their response."
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
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Parmi les animaux on a les : chien \n",
      "En voici un, le : Doberman\n",
      "\n",
      "Parmi les animaux on a les : oiseau \n",
      "En voici un, le : Canari\n",
      "\n",
      "Parmi les animaux on a les : reptile \n",
      "En voici un, le : Boa\n",
      "\n",
      "Bonjour Anas\n",
      "Quel est ton sport préféré ? le foot est mon sport préféré.\n",
      "Bonjour Jordan\n",
      "Quel est ton sport préféré ? le basket-ball est mon sport préféré.\n",
      "Bonjour Lorraine\n",
      "Quel est ton sport préféré ? le tennis est mon sport préféré.\n"
     ]
    }
   ],
   "source": [
    "animaux_de_compagnie = {\"chien\": \"doberman\",\n",
    "                        \"oiseau\": \"canari\",\n",
    "                        \"reptile\": \"boa\"\n",
    "                        }\n",
    "for key , value, in animaux_de_compagnie.items():\n",
    "    print(\"Parmi les animaux on a les : %s \" % key)\n",
    "    print(\"En voici un, le : %s\\n\" % value.title())\n",
    "\n",
    "\n",
    "question_reponse = {\"anas\": \"le foot est mon sport préféré.\",\n",
    "                    \"jordan\": \"le basket-ball est mon sport préféré.\",\n",
    "                    \"lorraine\": \"le tennis est mon sport préféré.\"\n",
    "                    }\n",
    "for key, value, in question_reponse.items():\n",
    "    print(\"Bonjour %s\" % key.title())\n",
    "    print(\"Quel est ton sport préféré ? %s\" % value) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Common operations with dictionaries\n",
    "===\n",
    "There are a few common things you will want to do with dictionaries. These include adding new key-value pairs, modifying information in the dictionary, and removing items from dictionaries."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Adding new key-value pairs\n",
    "---\n",
    "To add a new key-value pair, you give the dictionary name followed by the new key in square brackets, and set that equal to the new value. We will show this by starting with an empty dictionary, and re-creating the dictionary from the example above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Word: list\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n",
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n"
     ]
    }
   ],
   "source": [
    "# Create an empty dictionary.\n",
    "python_words = {}\n",
    "\n",
    "# Fill the dictionary, pair by pair.\n",
    "python_words['list'] ='A collection of values that are not connected, but have an order.'\n",
    "python_words['dictionary'] = 'A collection of key-value pairs.'\n",
    "python_words['function'] = 'A named set of instructions that defines a set of actions in Python.'\n",
    "\n",
    "# Print out the items in the dictionary.\n",
    "for word, meaning in python_words.items():\n",
    "    print(\"\\nWord: %s\" % word)\n",
    "    print(\"Meaning: %s\" % meaning)"
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
    "Modifying values in a dictionary\n",
    "---\n",
    "At some point you may want to modify one of the values in your dictionary. Modifying a value in a dictionary is pretty similar to modifying an element in a list. You give the name of the dictionary and then the key in square brackets, and set that equal to the new value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dictionary: A collection of key-value pairs.\n",
      "\n",
      "dictionary: A collection of key-value pairs. Each key can be used to access its corresponding value.\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "print('dictionary: ' + python_words['dictionary'])\n",
    "    \n",
    "# Clarify one of the meanings.\n",
    "python_words['dictionary'] = 'A collection of key-value pairs. Each key can be used to access its corresponding value.'\n",
    "\n",
    "print('\\ndictionary: ' + python_words['dictionary'])"
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
    "Removing key-value pairs\n",
    "---\n",
    "You may want to remove some key-value pairs from one of your dictionaries at some point. You can do this using the same `del` command you learned to use with lists. To remove a key-value pair, you give the `del` command, followed by the name of the dictionary, with the key that you want to delete. This removes the key and the value as a pair."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "These are the Python words I know:\n",
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "Word: list\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n",
      "\n",
      "\n",
      "These are the Python words I know:\n",
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Show the current set of words and meanings.\n",
    "print(\"\\n\\nThese are the Python words I know:\")\n",
    "for word, meaning in python_words.items():\n",
    "    print(\"\\nWord: %s\" % word)\n",
    "    print(\"Meaning: %s\" % meaning)\n",
    "    \n",
    "# Remove the word 'list' and its meaning.\n",
    "del python_words['list']\n",
    "\n",
    "# Show the current set of words and meanings.\n",
    "print(\"\\n\\nThese are the Python words I know:\")\n",
    "for word, meaning in python_words.items():\n",
    "    print(\"\\nWord: %s\" % word)\n",
    "    print(\"Meaning: %s\" % meaning)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you were going to work with this code, you would certainly want to put the code for displaying the dictionary into a function. Let's see what this looks like:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "These are the Python words I know:\n",
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "Word: list\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n",
      "\n",
      "\n",
      "These are the Python words I know:\n",
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[2,3,4,5,6,7,8,16,21]\n",
    "def show_words_meanings(python_words):\n",
    "    # This function takes in a dictionary of python words and meanings,\n",
    "    #  and prints out each word with its meaning.\n",
    "    print(\"\\n\\nThese are the Python words I know:\")\n",
    "    for word, meaning in python_words.items():\n",
    "        print(\"\\nWord: %s\" % word)\n",
    "        print(\"Meaning: %s\" % meaning)\n",
    "        \n",
    "\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "show_words_meanings(python_words)\n",
    "    \n",
    "# Remove the word 'list' and its meaning.\n",
    "del python_words['list']\n",
    "\n",
    "show_words_meanings(python_words)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As long as we have a nice clean function to work with, let's clean up our output a little:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "These are the Python words I know:\n",
      "\n",
      "function: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "list: A collection of values that are not connected, but have an order.\n",
      "\n",
      "dictionary: A collection of key-value pairs.\n",
      "\n",
      "\n",
      "These are the Python words I know:\n",
      "\n",
      "function: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "dictionary: A collection of key-value pairs.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[7]\n",
    "def show_words_meanings(python_words):\n",
    "    # This function takes in a dictionary of python words and meanings,\n",
    "    #  and prints out each word with its meaning.\n",
    "    print(\"\\n\\nThese are the Python words I know:\")\n",
    "    for word, meaning in python_words.items():\n",
    "        print(\"\\n%s: %s\" % (word, meaning))\n",
    "        \n",
    "\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "show_words_meanings(python_words)\n",
    "    \n",
    "# Remove the word 'list' and its meaning.\n",
    "del python_words['list']\n",
    "\n",
    "show_words_meanings(python_words)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is much more realistic code."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Modifying keys in a dictionary\n",
    "---\n",
    "Modifying a value in a dictionary was straightforward, because nothing else depends on the value. Modifying a key is a little harder, because each key is used to unlock a value. We can change a key in two steps:\n",
    "\n",
    "- Make a new key, and copy the value to the new key.\n",
    "- Delete the old key, which also deletes the old value.\n",
    "\n",
    "Here's what this looks like. We will use a dictionary with just one key-value pair, to keep things simple."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'list': 'A collection of values that are not connected, but have an order.'}\n"
     ]
    }
   ],
   "source": [
    "# We have a spelling mistake!\n",
    "python_words = {'lisst': 'A collection of values that are not connected, but have an order.'}\n",
    "\n",
    "# Create a new, correct key, and connect it to the old value.\n",
    "#  Then delete the old key.\n",
    "python_words['list'] = python_words['lisst']\n",
    "del python_words['lisst']\n",
    "\n",
    "# Print the dictionary, to show that the key has changed.\n",
    "print(python_words)"
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
    "<a id=\"Exercises-operations\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Pet Names 2\n",
    "- Make a copy of your program from [Pet Names](#exercises_what).\n",
    "    - Use a for loop to print out a series of statements such as \"Willie is a dog.\"\n",
    "    - Modify one of the values in your dictionary. You could clarify to name a breed, or you could change an animal from a cat to a dog.\n",
    "        - Use a for loop to print out a series of statements such as \"Willie is a dog.\"\n",
    "    - Add a new key-value pair to your dictionary.\n",
    "        - Use a for loop to print out a series of statements such as \"Willie is a dog.\"\n",
    "    - Remove one of the key-value pairs from your dictionary.\n",
    "        - Use a for loop to print out a series of statements such as \"Willie is a dog.\"\n",
    "- Bonus: Use a function to do all of the looping and printing in this problem.\n",
    "\n",
    "#### Weight Lifting\n",
    "- Make a dictionary where the keys are the names of weight lifting exercises, and the values are the number of times you did that exercise.\n",
    "    - Use a for loop to print out a series of statements such as \"I did 10 bench presses\".\n",
    "    - Modify one of the values in your dictionary, to represent doing more of that exercise.\n",
    "        - Use a for loop to print out a series of statements such as \"I did 10 bench presses\".\n",
    "    - Add a new key-value pair to your dictionary.\n",
    "        - - Use a for loop to print out a series of statements such as \"I did 10 bench presses\".\n",
    "    - Remove one of the key-value pairs from your dictionary.\n",
    "        - - Use a for loop to print out a series of statements such as \"I did 10 bench presses\".\n",
    "- Bonus: Use a function to do all of the looping and printing in this problem."
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
    "Looping through a dictionary\n",
    "===\n",
    "Since dictionaries are really about connecting bits of information, you will often use them in the ways described above, where you add key-value pairs whenever you receive some new information, and then you retrieve the key-value pairs that you care about. Sometimes, however, you will want to loop through the entire dictionary. There are several ways to do this:\n",
    "\n",
    "- You can loop through all key-value pairs;\n",
    "- You can loop through the keys, and pull out the values for any keys that you care about;\n",
    "- You can loop through the values."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Looping through all key-value pairs\n",
    "---\n",
    "This is the kind of loop that was shown in the first example. Here's what this loop looks like, in a general format:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Key: key_1\n",
      "Value: value_1\n",
      "\n",
      "Key: key_3\n",
      "Value: value_3\n",
      "\n",
      "Key: key_2\n",
      "Value: value_2\n"
     ]
    }
   ],
   "source": [
    "my_dict = {'key_1': 'value_1',\n",
    "    'key_2': 'value_2',\n",
    "    'key_3': 'value_3',\n",
    "    }\n",
    "\n",
    "for key, value in my_dict.items():\n",
    "    print('\\nKey: %s' % key)\n",
    "    print('Value: %s' % value)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This works because the method `.items()` pulls all key-value pairs from a dictionary into a list of tuples:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('key_1', 'value_1'), ('key_3', 'value_3'), ('key_2', 'value_2')]\n"
     ]
    }
   ],
   "source": [
    "my_dict = {'key_1': 'value_1',\n",
    "    'key_2': 'value_2',\n",
    "    'key_3': 'value_3',\n",
    "    }\n",
    "\n",
    "print(my_dict.items())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The syntax `for key, value in my_dict.items():` does the work of looping through this list of tuples, and pulling the first and second item from each tuple for us.\n",
    "\n",
    "There is nothing special about any of these variable names, so Python code that uses this syntax becomes really readable. Rather than create a new example of this loop, let's just look at the original example again to see this in a meaningful context:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Word: function\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "Word: list\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "Word: dictionary\n",
      "Meaning: A collection of key-value pairs.\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "for word, meaning in python_words.items():\n",
    "    print(\"\\nWord: %s\" % word)\n",
    "    print(\"Meaning: %s\" % meaning)"
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
    "Looping through all keys in a dictionary\n",
    "---\n",
    "Python provides a clear syntax for looping through just the keys in a dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key: key_1\n",
      "Key: key_3\n",
      "Key: key_2\n"
     ]
    }
   ],
   "source": [
    "my_dict = {'key_1': 'value_1',\n",
    "    'key_2': 'value_2',\n",
    "    'key_3': 'value_3',\n",
    "    }\n",
    "\n",
    "for key in my_dict.keys():\n",
    "    print('Key: %s' % key)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is actually the default behavior of looping through the dictionary itself. So you can leave out the `.keys()` part, and get the exact same behavior:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key: key_1\n",
      "Key: key_3\n",
      "Key: key_2\n"
     ]
    }
   ],
   "source": [
    "###highlight=[7]\n",
    "my_dict = {'key_1': 'value_1',\n",
    "    'key_2': 'value_2',\n",
    "    'key_3': 'value_3',\n",
    "    }\n",
    "\n",
    "for key in my_dict:\n",
    "    print('Key: %s' % key)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The only advantage of using the `.keys()` in the code is a little bit of clarity. But anyone who knows Python reasonably well is going to recognize what the second version does. In the rest of our code, we will leave out the `.keys()` when we want this behavior.\n",
    "\n",
    "You can pull out the value of any key that you are interested in within your loop, using the standard notation for accessing a dictionary value from a key:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Key: key_1\n",
      "Key: key_3\n",
      "Key: key_2\n",
      "  The value for key_2 is value_2.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[9,10]\n",
    "my_dict = {'key_1': 'value_1',\n",
    "    'key_2': 'value_2',\n",
    "    'key_3': 'value_3',\n",
    "    }\n",
    "\n",
    "for key in my_dict:\n",
    "    print('Key: %s' % key)\n",
    "    if key == 'key_2':\n",
    "        print(\"  The value for key_2 is %s.\" % my_dict[key])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's show how we might use this in our Python words program. This kind of loop provides a straightforward way to show only the words in the dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The following Python words have been defined:\n",
      "- function\n",
      "- list\n",
      "- dictionary\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Show the words that are currently in the dictionary.\n",
    "print(\"The following Python words have been defined:\")\n",
    "for word in python_words:\n",
    "    print(\"- %s\" % word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can extend this slightly to make a program that lets you look up words. We first let the user choose a word. When the user has chosen a word, we get the meaning for that word, and display it:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The following Python words have been defined:\n",
      "- function\n",
      "- list\n",
      "- dictionary\n",
      "\n",
      "What word would you like to learn about? list\n",
      "\n",
      "list: A collection of values that are not connected, but have an order.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[12,13,14]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Show the words that are currently in the dictionary.\n",
    "print(\"The following Python words have been defined:\")\n",
    "for word in python_words:\n",
    "    print(\"- %s\" % word)\n",
    "    \n",
    "# Allow the user to choose a word, and then display the meaning for that word.\n",
    "requested_word = raw_input(\"\\nWhat word would you like to learn about? \")\n",
    "print(\"\\n%s: %s\" % (requested_word, python_words[requested_word]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This allows the user to select one word that has been defined. If we enclose the input part of the program in a while loop, the user can see as many definitions as they'd like:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The following Python words have been defined:\n",
      "- function\n",
      "- list\n",
      "- dictionary\n",
      "\n",
      "What word would you like to learn about? (or 'quit') list\n",
      "\n",
      "  list: A collection of values that are not connected, but have an order.\n",
      "\n",
      "What word would you like to learn about? (or 'quit') dictionary\n",
      "\n",
      "  dictionary: A collection of key-value pairs.\n",
      "\n",
      "What word would you like to learn about? (or 'quit') quit\n",
      "\n",
      "  Sorry, I don't know that word.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[12,13,14,15,16,17,18,19,20]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Show the words that are currently in the dictionary.\n",
    "print(\"The following Python words have been defined:\")\n",
    "for word in python_words:\n",
    "    print(\"- %s\" % word)\n",
    "\n",
    "requested_word = ''\n",
    "while requested_word != 'quit':\n",
    "    # Allow the user to choose a word, and then display the meaning for that word.\n",
    "    requested_word = raw_input(\"\\nWhat word would you like to learn about? (or 'quit') \")\n",
    "    if requested_word in python_words.keys():\n",
    "        print(\"\\n  %s: %s\" % (requested_word, python_words[requested_word]))\n",
    "    else:\n",
    "        # Handle misspellings, and words not yet stored.\n",
    "        print(\"\\n  Sorry, I don't know that word.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This allows the user to ask for as many meanings as they want, but it takes the word \"quit\" as a requested word. Let's add an `elif` clause to clean up this behavior:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The following Python words have been defined:\n",
      "- function\n",
      "- list\n",
      "- dictionary\n",
      "\n",
      "What word would you like to learn about? (or 'quit') function\n",
      "\n",
      "  function: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "What word would you like to learn about? (or 'quit') dictionary\n",
      "\n",
      "  dictionary: A collection of key-value pairs.\n",
      "\n",
      "What word would you like to learn about? (or 'quit') list\n",
      "\n",
      "  list: A collection of values that are not connected, but have an order.\n",
      "\n",
      "What word would you like to learn about? (or 'quit') class\n",
      "\n",
      "  Sorry, I don't know that word.\n",
      "\n",
      "What word would you like to learn about? (or 'quit') quit\n",
      "\n",
      "  Bye!\n"
     ]
    }
   ],
   "source": [
    "###highlight=[16,17,18,19,20,21,22,23,24]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Show the words that are currently in the dictionary.\n",
    "print(\"The following Python words have been defined:\")\n",
    "for word in python_words:\n",
    "    print(\"- %s\" % word)\n",
    "\n",
    "requested_word = ''\n",
    "while requested_word != 'quit':\n",
    "    # Allow the user to choose a word, and then display the meaning for that word.\n",
    "    requested_word = raw_input(\"\\nWhat word would you like to learn about? (or 'quit') \")\n",
    "    if requested_word in python_words.keys():\n",
    "        # This is a word we know, so show the meaning.\n",
    "        print(\"\\n  %s: %s\" % (requested_word, python_words[requested_word]))\n",
    "    elif requested_word != 'quit':\n",
    "        # This is not in python_words, and it's not 'quit'.\n",
    "        print(\"\\n  Sorry, I don't know that word.\")\n",
    "    else:\n",
    "        # The word is quit.\n",
    "        print \"\\n  Bye!\""
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
    "Looping through all values in a dictionary\n",
    "---\n",
    "Python provides a straightforward syntax for looping through all the values in a dictionary, as well:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Value: value_1\n",
      "Value: value_3\n",
      "Value: value_2\n"
     ]
    }
   ],
   "source": [
    "my_dict = {'key_1': 'value_1',\n",
    "    'key_2': 'value_2',\n",
    "    'key_3': 'value_3',\n",
    "    }\n",
    "\n",
    "for value in my_dict.values():\n",
    "    print('Value: %s' % value)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can use this loop syntax to have a little fun with the dictionary example, by making a little quiz program. The program will display a meaning, and ask the user to guess the word that matches that meaning. Let's start out by showing all the meanings in the dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "Meaning: A collection of key-value pairs.\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "for meaning in python_words.values():\n",
    "    print(\"Meaning: %s\" % meaning)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we can add a prompt after each meaning, asking the user to guess the word:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "What word do you think this is? function\n",
      "You got it!\n",
      "\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "What word do you think this is? function\n",
      "Sorry, that's just not the right word.\n",
      "\n",
      "Meaning: A collection of key-value pairs.\n",
      "What word do you think this is? dictionary\n",
      "You got it!\n"
     ]
    }
   ],
   "source": [
    "###highlight=[12,13,14,15,16,17,18]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Print each meaning, one at a time, and ask the user\n",
    "#  what word they think it is.\n",
    "for meaning in python_words.values():\n",
    "    print(\"\\nMeaning: %s\" % meaning)\n",
    "    \n",
    "    guessed_word = raw_input(\"What word do you think this is? \")\n",
    "    \n",
    "    # The guess is correct if the guessed word's meaning matches the current meaning.\n",
    "    if python_words[guessed_word] == meaning:\n",
    "        print(\"You got it!\")\n",
    "    else:\n",
    "        print(\"Sorry, that's just not the right word.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is starting to work, but we can see from the output that the user does not get the chance to take a second guess if they guess wrong for any meaning. We can use a while loop around the guessing code, to let the user guess until they get it right:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Meaning: A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "What word do you think this is? function\n",
      "You got it!\n",
      "\n",
      "Meaning: A collection of values that are not connected, but have an order.\n",
      "\n",
      "What word do you think this is? dictionary\n",
      "Sorry, that's just not the right word.\n",
      "\n",
      "What word do you think this is? list\n",
      "You got it!\n",
      "\n",
      "Meaning: A collection of key-value pairs.\n",
      "\n",
      "What word do you think this is? dictionary\n",
      "You got it!\n"
     ]
    }
   ],
   "source": [
    "###highlight=[12,13,14,15,16,17,18,19,20,21,22]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "# Print each meaning, one at a time, and ask the user\n",
    "#  what word they think it is.\n",
    "for meaning in python_words.values():\n",
    "    print(\"\\nMeaning: %s\" % meaning)\n",
    "    \n",
    "    # Assume the guess is not correct; keep guessing until correct.\n",
    "    correct = False\n",
    "    while not correct:\n",
    "        guessed_word = input(\"\\nWhat word do you think this is? \")\n",
    "    \n",
    "        # The guess is correct if the guessed word's meaning matches the current meaning.\n",
    "        if python_words[guessed_word] == meaning:\n",
    "            print(\"You got it!\")\n",
    "            correct = True\n",
    "        else:\n",
    "            print(\"Sorry, that's just not the right word.\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This is better. Now, if the guess is incorrect, the user is caught in a loop that they can only exit by guessing correctly. The final revision to this code is to show the user a list of words to choose from when they are asked to guess:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "A named set of instructions that defines a set of actions in Python.\n",
      "\n",
      "What word do you think this is?\n",
      "function  list  dictionary  \n",
      "- function\n",
      "You got it!\n",
      "\n",
      "A collection of values that are not connected, but have an order.\n",
      "\n",
      "What word do you think this is?\n",
      "function  list  dictionary  \n",
      "- dictionary\n",
      "Sorry, that's just not the right word.\n",
      "\n",
      "What word do you think this is?\n",
      "function  list  dictionary  \n",
      "- list\n",
      "You got it!\n",
      "\n",
      "A collection of key-value pairs.\n",
      "\n",
      "What word do you think this is?\n",
      "function  list  dictionary  \n",
      "- dictionary\n",
      "You got it!\n"
     ]
    }
   ],
   "source": [
    "###highlight=[7,8,9,10,11,12,23,24,25]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "def show_words(python_words):\n",
    "    # A simple function to show the words in the dictionary.\n",
    "    display_message = \"\"\n",
    "    for word in python_words.keys():\n",
    "        display_message += word + '  '\n",
    "    print display_message\n",
    "\n",
    "# Print each meaning, one at a time, and ask the user\n",
    "#  what word they think it is.\n",
    "for meaning in python_words.values():\n",
    "    print(\"\\n%s\" % meaning)\n",
    "\n",
    "    # Assume the guess is not correct; keep guessing until correct.\n",
    "    correct = False\n",
    "    while not correct:\n",
    "        \n",
    "        print(\"\\nWhat word do you think this is?\")\n",
    "        show_words(python_words)\n",
    "        guessed_word = raw_input(\"- \")    \n",
    "        \n",
    "        # The guess is correct if the guessed word's meaning matches the current meaning.\n",
    "        if python_words[guessed_word] == meaning:\n",
    "            print(\"You got it!\")\n",
    "            correct = True\n",
    "        else:\n",
    "            print(\"Sorry, that's just not the right word.\")"
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
    "Looping through a dictionary in order\n",
    "===\n",
    "Dictionaries are quite useful because they allow bits of information to be connected. One of the problems with dictionaries, however, is that they are not stored in any particular order. When you retrieve all of the keys or values in your dictionary, you can't be sure what order you will get them back. There is a quick and easy way to do this, however, when you want them in a particular order.\n",
    "\n",
    "Let's take a look at the order that results from a simple call to *dictionary.keys()*:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "function\n",
      "list\n",
      "dictionary\n"
     ]
    }
   ],
   "source": [
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "for word in python_words.keys():\n",
    "    print(word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The resulting list is not in order. The list of keys can be put in order by passing the list into the *sorted()* function, in the line that initiates the for loop:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dictionary\n",
      "function\n",
      "list\n"
     ]
    }
   ],
   "source": [
    "###highlight=[7]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "for word in sorted(python_words.keys()):\n",
    "    print(word)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This approach can be used to work with the keys and values in order. For example, the words and meanings can be printed in alphabetical order by word:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dictionary: A collection of key-value pairs.\n",
      "Function: A named set of instructions that defines a set of actions in Python.\n",
      "List: A collection of values that are not connected, but have an order.\n"
     ]
    }
   ],
   "source": [
    "###highlight=[8]\n",
    "python_words = {'list': 'A collection of values that are not connected, but have an order.',\n",
    "                'dictionary': 'A collection of key-value pairs.',\n",
    "                'function': 'A named set of instructions that defines a set of actions in Python.',\n",
    "                }\n",
    "\n",
    "for word in sorted(python_words.keys()):\n",
    "    print(\"%s: %s\" % (word.title(), python_words[word]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this example, the keys have been put into alphabetical order in the for loop only; Python has not changed the way the dictionary is stored at all. So the next time the dictionary is accessed, the keys could be returned in any order. There is no way to permanently specify an order for the items in an ordinary dictionary, but if you want to do this you can use the [OrderedDict](http://docs.python.org/3.3/library/collections.html#ordereddict-objects) structure."
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
    "<a id=\"Exercises-looping\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Mountain Heights\n",
    "- Wikipedia has a list of the [tallest mountains in the world](http://en.wikipedia.org/wiki/List_of_mountains_by_elevation), with each mountain's elevation. Pick five mountains from this list.\n",
    "    - Create a dictionary with the mountain names as keys, and the elevations as values.\n",
    "    - Print out just the mountains' names, by looping through the keys of your dictionary.\n",
    "    - Print out just the mountains' elevations, by looping through the values of your dictionary.\n",
    "    - Print out a series of statements telling how tall each mountain is: \"Everest is 8848 meters tall.\"\n",
    "- Revise your output, if necessary.\n",
    "    - Make sure there is an introductory sentence describing the output for each loop you write.\n",
    "    - Make sure there is a blank line between each group of statements.\n",
    "\n",
    "#### Mountain Heights 2\n",
    "- Revise your final output from Mountain Heights, so that the information is listed in alphabetical order by each mountain's name.\n",
    "    - That is, print out a series of statements telling how tall each mountain is: \"Everest is 8848 meters tall.\"\n",
    "    - Make sure your output is in alphabetical order."
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
    "Nesting\n",
    "===\n",
    "Nesting is one of the most powerful concepts we have come to so far. Nesting involves putting a list or dictionary inside another list or dictionary. We will look at two examples here, lists inside of a dictionary and dictionaries inside of a dictionary. With nesting, the kind of information we can model in our programs is expanded greatly."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lists in a dictionary\n",
    "---\n",
    "A dictionary connects two pieces of information. Those two pieces of information can be any kind of data structure in Python. Let's keep using strings for our keys, but let's try giving a list as a value.\n",
    "\n",
    "The first example will involve storing a number of people's favorite numbers. The keys consist of people's names, and the values are lists of each person's favorite numbers. In this first example, we will access each person's list one at a time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Eric's favorite numbers are:\n",
      "[3, 11, 19, 23, 42]\n",
      "\n",
      "Ever's favorite numbers are:\n",
      "[2, 4, 5]\n",
      "\n",
      "Willie's favorite numbers are:\n",
      "[5, 35, 120]\n"
     ]
    }
   ],
   "source": [
    "# This program stores people's favorite numbers, and displays them.\n",
    "favorite_numbers = {'eric': [3, 11, 19, 23, 42],\n",
    "                    'ever': [2, 4, 5],\n",
    "                    'willie': [5, 35, 120],\n",
    "                    }\n",
    "\n",
    "# Display each person's favorite numbers.\n",
    "print(\"Eric's favorite numbers are:\")\n",
    "print(favorite_numbers['eric'])\n",
    "\n",
    "print(\"\\nEver's favorite numbers are:\")\n",
    "print(favorite_numbers['ever'])\n",
    "\n",
    "print(\"\\nWillie's favorite numbers are:\")\n",
    "print(favorite_numbers['willie'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We are really just working our way through each key in the dictionary, so let's use a for loop to go through the keys in the dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Willie's favorite numbers are:\n",
      "[5, 35, 120]\n",
      "\n",
      "Ever's favorite numbers are:\n",
      "[2, 4, 5]\n",
      "\n",
      "Eric's favorite numbers are:\n",
      "[3, 11, 19, 23, 42]\n"
     ]
    }
   ],
   "source": [
    "###highlight=[8,9,10,11]\n",
    "# This program stores people's favorite numbers, and displays them.\n",
    "favorite_numbers = {'eric': [3, 11, 19, 23, 42],\n",
    "                    'ever': [2, 4, 5],\n",
    "                    'willie': [5, 35, 120],\n",
    "                    }\n",
    "\n",
    "# Display each person's favorite numbers.\n",
    "for name in favorite_numbers:\n",
    "    print(\"\\n%s's favorite numbers are:\" % name.title())\n",
    "    print(favorite_numbers[name])      "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This structure is fairly complex, so don't worry if it takes a while for things to sink in. The dictionary itself probably makes sense; each person is connected to a list of their favorite numbers.\n",
    "\n",
    "This works, but we'd rather not print raw Python in our output. Let's use a for loop to print the favorite numbers individually, rather than in a Python list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Willie's favorite numbers are:\n",
      "5\n",
      "35\n",
      "120\n",
      "\n",
      "Ever's favorite numbers are:\n",
      "2\n",
      "4\n",
      "5\n",
      "\n",
      "Eric's favorite numbers are:\n",
      "3\n",
      "11\n",
      "19\n",
      "23\n",
      "42\n"
     ]
    }
   ],
   "source": [
    "###highlight=[11,12,13,14]\n",
    "# This program stores people's favorite numbers, and displays them.\n",
    "favorite_numbers = {'eric': [3, 11, 19, 23, 42],\n",
    "                    'ever': [2, 4, 5],\n",
    "                    'willie': [5, 35, 120],\n",
    "                    }\n",
    "\n",
    "# Display each person's favorite numbers.\n",
    "for name in favorite_numbers:\n",
    "    print(\"\\n%s's favorite numbers are:\" % name.title())\n",
    "    # Each value is itself a list, so we need another for loop\n",
    "    #  to work with the list.\n",
    "    for favorite_number in favorite_numbers[name]:\n",
    "        print(favorite_number)        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Things get a little more complicated inside the for loop. The value is a list of favorite numbers, so the for loop pulls each *favorite\\_number* out of the list one at a time. If it makes more sense to you, you are free to store the list in a new variable, and use that to define your for loop:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Willie's favorite numbers are:\n",
      "5\n",
      "35\n",
      "120\n",
      "\n",
      "Ever's favorite numbers are:\n",
      "2\n",
      "4\n",
      "5\n",
      "\n",
      "Eric's favorite numbers are:\n",
      "3\n",
      "11\n",
      "19\n",
      "23\n",
      "42\n"
     ]
    }
   ],
   "source": [
    "###highlight=[12,13,14,15]\n",
    "# This program stores people's favorite numbers, and displays them.\n",
    "favorite_numbers = {'eric': [3, 11, 19, 23, 42],\n",
    "                    'ever': [2, 4, 5],\n",
    "                    'willie': [5, 35, 120],\n",
    "                    }\n",
    "\n",
    "# Display each person's favorite numbers.\n",
    "for name in favorite_numbers:\n",
    "    print(\"\\n%s's favorite numbers are:\" % name.title())\n",
    "    \n",
    "    # Each value is itself a list, so let's put that list in a variable.\n",
    "    current_favorite_numbers = favorite_numbers[name]\n",
    "    for favorite_number in current_favorite_numbers:\n",
    "        print(favorite_number)        "
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
    "Dictionaries in a dictionary\n",
    "---\n",
    "The most powerful nesting concept we will cover right now is nesting a dictionary inside of a dictionary.\n",
    "\n",
    "To demonstrate this, let's make a dictionary of pets, with some information about each pet. The keys for this dictionary will consist of the pet's name. The values will include information such as the kind of animal, the owner, and whether the pet has been vaccinated."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is what I know about Willie:\n",
      "kind: dog\n",
      "owner: eric\n",
      "vaccinated: True\n",
      "\n",
      "Here is what I know about Walter:\n",
      "kind: cockroach\n",
      "owner: eric\n",
      "vaccinated: False\n",
      "\n",
      "Here is what I know about Peso:\n",
      "kind: dog\n",
      "owner: chloe\n",
      "vaccinated: True\n"
     ]
    }
   ],
   "source": [
    "# This program stores information about pets. For each pet,\n",
    "#   we store the kind of animal, the owner's name, and\n",
    "#   the breed.\n",
    "pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},\n",
    "        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},\n",
    "        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},\n",
    "        }\n",
    "\n",
    "# Let's show all the information for each pet.\n",
    "print(\"Here is what I know about Willie:\")\n",
    "print(\"kind: \" + pets['willie']['kind'])\n",
    "print(\"owner: \" + pets['willie']['owner'])\n",
    "print(\"vaccinated: \" + str(pets['willie']['vaccinated']))\n",
    "\n",
    "print(\"\\nHere is what I know about Walter:\")\n",
    "print(\"kind: \" + pets['walter']['kind'])\n",
    "print(\"owner: \" + pets['walter']['owner'])\n",
    "print(\"vaccinated: \" + str(pets['walter']['vaccinated']))\n",
    "\n",
    "print(\"\\nHere is what I know about Peso:\")\n",
    "print(\"kind: \" + pets['peso']['kind'])\n",
    "print(\"owner: \" + pets['peso']['owner'])\n",
    "print(\"vaccinated: \" + str(pets['peso']['vaccinated']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Clearly this is some repetitive code, but it shows exactly how we access information in a nested dictionary. In the first set of `print` statements, we use the name 'willie' to unlock the 'kind' of animal he is, the 'owner' he has, and whether or not he is 'vaccinated'. We have to wrap the vaccination value in the `str` function so that Python knows we want the words 'True' and 'False', not the values `True` and `False`. We then do the same thing for each animal.\n",
    "\n",
    "Let's rewrite this program, using a for loop to go through the dictionary's keys:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Here is what I know about Peso:\n",
      "kind: dog\n",
      "owner: chloe\n",
      "vaccinated: True\n",
      "\n",
      "Here is what I know about Willie:\n",
      "kind: dog\n",
      "owner: eric\n",
      "vaccinated: True\n",
      "\n",
      "Here is what I know about Walter:\n",
      "kind: cockroach\n",
      "owner: eric\n",
      "vaccinated: False\n"
     ]
    }
   ],
   "source": [
    "###highlight=[10,11,12,13,14,15]\n",
    "# This program stores information about pets. For each pet,\n",
    "#   we store the kind of animal, the owner's name, and\n",
    "#   the breed.\n",
    "pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},\n",
    "        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},\n",
    "        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},\n",
    "        }\n",
    "\n",
    "# Let's show all the information for each pet.\n",
    "for pet_name, pet_information in pets.items():\n",
    "    print(\"\\nHere is what I know about %s:\" % pet_name.title())\n",
    "    print(\"kind: \" + pet_information['kind'])\n",
    "    print(\"owner: \" + pet_information['owner'])\n",
    "    print(\"vaccinated: \" + str(pet_information['vaccinated']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This code is much shorter and easier to maintain. But even this code will not keep up with our dictionary. If we add more information to the dictionary later, we will have to update our print statements. Let's put a second for loop inside the first loop in order to run through all the information about each pet:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Here is what I know about Peso:\n",
      "owner: chloe\n",
      "kind: dog\n",
      "vaccinated: True\n",
      "\n",
      "Here is what I know about Willie:\n",
      "owner: eric\n",
      "kind: dog\n",
      "vaccinated: True\n",
      "\n",
      "Here is what I know about Walter:\n",
      "owner: eric\n",
      "kind: cockroach\n",
      "vaccinated: False\n"
     ]
    }
   ],
   "source": [
    "###highlight=[14,15]\n",
    "# This program stores information about pets. For each pet,\n",
    "#   we store the kind of animal, the owner's name, and\n",
    "#   the breed.\n",
    "pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},\n",
    "        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},\n",
    "        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},\n",
    "        }\n",
    "\n",
    "# Let's show all the information for each pet.\n",
    "for pet_name, pet_information in pets.items():\n",
    "    print(\"\\nHere is what I know about %s:\" % pet_name.title())\n",
    "    # Each animal's dictionary is in 'information'\n",
    "    for key in pet_information:\n",
    "        print(key + \": \" + str(pet_information[key]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This nested loop can look pretty complicated, so again, don't worry if it doesn't make sense for a while.\n",
    "\n",
    "- The first loop gives us all the keys in the main dictionary, which consist of the name of each pet.\n",
    "- Each of these names can be used to 'unlock' the dictionary of each pet.\n",
    "- The inner loop goes through the dictionary for that individual pet, and pulls out all of the keys in that individual pet's dictionary.\n",
    "- We print the key, which tells us the kind of information we are about to see, and the value for that key.\n",
    "- You can see that we could improve the formatting in the output.\n",
    "    - We could capitalize the owner's name.\n",
    "    - We could print 'yes' or 'no', instead of True and False.\n",
    "    \n",
    "Let's show one last version that uses some if statements to clean up our data for printing:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Here is what I know about Peso:\n",
      "owner: Chloe\n",
      "kind: dog\n",
      "vaccinated: yes\n",
      "\n",
      "Here is what I know about Willie:\n",
      "owner: Eric\n",
      "kind: dog\n",
      "vaccinated: yes\n",
      "\n",
      "Here is what I know about Walter:\n",
      "owner: Eric\n",
      "kind: cockroach\n",
      "vaccinated: no\n"
     ]
    }
   ],
   "source": [
    "###highlight=[15,16,17,18,19,20,21,22,23,24,25,26,27]\n",
    "# This program stores information about pets. For each pet,\n",
    "#   we store the kind of animal, the owner's name, and\n",
    "#   the breed.\n",
    "pets = {'willie': {'kind': 'dog', 'owner': 'eric', 'vaccinated': True},\n",
    "        'walter': {'kind': 'cockroach', 'owner': 'eric', 'vaccinated': False},\n",
    "        'peso': {'kind': 'dog', 'owner': 'chloe', 'vaccinated': True},\n",
    "        }\n",
    "\n",
    "# Let's show all the information for each pet.\n",
    "for pet_name, pet_information in pets.items():\n",
    "    print(\"\\nHere is what I know about %s:\" % pet_name.title())\n",
    "    # Each animal's dictionary is in pet_information\n",
    "    for key in pet_information:\n",
    "        if key == 'owner':\n",
    "            # Capitalize the owner's name.\n",
    "            print(key + \": \" + pet_information[key].title())\n",
    "        elif key == 'vaccinated':\n",
    "            # Print 'yes' for True, and 'no' for False.\n",
    "            vaccinated = pet_information['vaccinated']\n",
    "            if vaccinated:\n",
    "                print 'vaccinated: yes'\n",
    "            else:\n",
    "                print 'vaccinated: no'\n",
    "        else:\n",
    "            # No special formatting needed for this key.\n",
    "            print(key + \": \" + pet_information[key])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This code is a lot longer, and now we have nested if statements as well as nested for loops. But keep in mind, this structure would work if there were 1000 pets in our dictionary, and it would work if we were storing 1000 pieces of information about each pet. One level of nesting lets us model an incredible array of information."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An important note about nesting\n",
    "---\n",
    "While one level of nesting is really useful, nesting much deeper than that gets really complicated, really quickly. There are other structures such as classes which can be even more useful for modeling information. In addition to this, we can use Python to store information in a database, which is the proper tool for storing deeply nested information.\n",
    "\n",
    "Often times when you are storing information in a database you will pull a small set of that information out and put it into a dictionary, or a slightly nested structure, and then work with it. But you will rarely, if ever, work with Python data structures nested more than one level deep."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a id=\"Exercises-nesting\"></a>\n",
    "Exercises\n",
    "---\n",
    "#### Mountain Heights 3\n",
    "- This is an extension of [Mountain Heights](#exercise_mountain_heights). Make sure you save this program under a different filename, such as *mountain\\_heights_3.py*, so that you can go back to your original program if you need to.\n",
    "    - The list of [tallest mountains in the world](http://en.wikipedia.org/wiki/List_of_mountains_by_elevation) provided all elevations in meters. Convert each of these elevations to feet, given that a meter is approximately 3.28 feet. You can do these calculations by hand at this point.\n",
    "    - Create a new dictionary, where the keys of the dictionary are still the mountains' names. This time however, the values of the dictionary should be a list of each mountain's elevation in meters, and then in feet: {'everest': [8848, 29029]}\n",
    "    - Print out just the mountains' names, by looping through the keys of your dictionary.\n",
    "    - Print out just the mountains' elevations in meters, by looping through the values of your dictionary and pulling out the first number from each list.\n",
    "    - Print out just the mountains' elevations in feet, by looping through the values of your dictionary and pulling out the second number from each list.\n",
    "    - Print out a series of statements telling how tall each mountain is: \"Everest is 8848 meters tall, or 29029 feet.\"\n",
    "- Bonus:\n",
    "    - Start with your original program from [Mountain Heights](#exercise_mountain_heights). Write a function that reads through the elevations in meters, and returns a list of elevations in feet. Use this list to create the nested dictionary described above.\n",
    "\n",
    "#### Mountain Heights 4\n",
    "- This is one more extension of Mountain Heights.\n",
    "    - Create a new dictionary, where the keys of the dictionary are once again the mountains' names. This time, the values of the dictionary are another dictionary. This dictionary should contain the elevation in either meters or feet, and the range that contains the mountain. For example: {'everest': {'elevation': 8848, 'range': 'himalaya'}}.\n",
    "    - Print out just the mountains' names.\n",
    "    - Print out just the mountains' elevations.\n",
    "    - Print out just the range for each mountain.\n",
    "    - Print out a series of statements that say everything you know about each mountain: \"Everest is an 8848-meter tall mountain in the Himalaya range.\""
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
    "#### Word Wall\n",
    "- A word wall is a place on your wall where you keep track of the new words and meanings you are learning. Write a terminal app that lets you enter new words, and a meaning for each word.\n",
    "    - Your app should have a title bar that says the name of your program.\n",
    "    - Your program should give users the option to see all words and meanings that have been entered so far.\n",
    "    - Your program should give users the option to enter a new word and meaning.\n",
    "        - Your program must not allow duplicate entries.\n",
    "    - Your program should store existing words and meanings, even after the program closes.\n",
    "    - Your program should give users the option to modify an existing meaning.\n",
    "- Bonus Features\n",
    "    - Allow users to modify the spelling of words.\n",
    "    - Allow users to categorize words.\n",
    "    - Turn the program into a game that quizzes users on words and meanings.\n",
    "    - (later on) Turn your program into a website that only you can use.\n",
    "    - (later on) Turn your program into a website that anyone can register for, and use.\n",
    "    - Add a visualization feature that reports on some statistics about the words and meanings that have been entered.\n",
    "\n",
    "#### Periodic Table App\n",
    "- The [Periodic Table](http://www.ptable.com/) of the Elements was developed to organize information about the elements that make up the Universe. Write a terminal app that lets you enter information about each element in the periodic table.\n",
    "    - Make sure you include the following information:\n",
    "        - symbol, name, atomic number, row, and column\n",
    "    - Choose at least one other piece of information to include in your app.\n",
    "    - Provide a menu of options for users to:\n",
    "        - See all the information that is stored about any element, by entering that element's symbol.\n",
    "        - Choose a property, and see that property for each element in the table.\n",
    "- Bonus Features\n",
    "    - Provide an option to view the symbols arranged like the periodic table. ([hint](#hints_periodic_table))"
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
    "[Previous: Basic Terminal Apps](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/terminal_apps.ipynb) | \n",
    "[Home](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/index.ipynb) |\n",
    "[Next: More Functions](http://nbviewer.ipython.org/urls/raw.github.com/ehmatthes/intro_programming/master/notebooks/more_functions.ipynb)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Hints\n",
    "===\n",
    "#### Periodic Table App\n",
    "- You can use a for loop to loop through each element. Pick out the elements' row numbers and column numbers.\n",
    "- Use two nested for loops to print either an element's symbol or a series of spaces, depending on how full that row is."
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
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
