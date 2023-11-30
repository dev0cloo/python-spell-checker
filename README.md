# Python Spell Checker

The **spell checker** is a python package that can check your spelling. It supports **_6_** languages!

It contains the following languages:

- English
- German
- Spanish
- French
- Italian
- Code

Code is a special language that contains the english language along with syntaxes and keywords of programming languages. This is to prevent the spell checker from marking them as misspelt words when the checker is used on a codebase. The words are stored in `code.txt` in `languages` folder.

All valid words of a language are stored in a text file in the `languages` folder. The words are sorted alphabetically and are in lowercase. You can add your own words to it. You can also delete words from the text file to exclude them as valid words.

# Installation

If not already [install pip](https://pip.pypa.io/en/stable/installing/)

Install the package with `pip` or `pip3`:

```bash
pip install python-spell-checker
```

# Usage

### Example:

```Python
from python_spell.checker import SpellChecker
text = "The... ! quick browmn fox jumps-over the lazi doug"
checker = SpellChecker(text, "english")

# This returns a dictionary object with all information
check_text = checker.check()
print(check_text)

# This returns a boolean for if the text has typos or not
is_valid = checker.has_typos
print("Does the text have typos? " , is_valid)

# This returns the number of typos (duplicate words are )
num_typos = checker.number_of_typos()
print("Number of typos are " , num_typos)

# This returns a list of misspelt words
misspelt_words = checker.get_typos()
print("Misspelt words are " , misspelt_words)
```

Output:

```bash
{
"Total words": 9
"Number of misspelled words": 2
"Number of words in dictionary": 194433
"Misspelled words": ['browmn', 'lazi']
"Lookup time(s)": 0.0005731582641601562
}

Does the text have typos? True

Number of typos are 2

Misspelt words are ['browmn', 'lazi']
```

#### Note

The SpellChecker class calls the `check()` method when it is initialized. So, you can directly use the `has_typos`, `number_of_typos()` and `get_typos()` methods without calling the `check()` method.

# Contributing

We welcome contributions to this project, especially those that help us fix bugs, add new words or improve the docs. If you would like to contribute, please fork the repo and submit a pull request.

# Credits

Credits to [Harvard90873](https://github.com/Harvard90873/) for creating [spell-checker](https://pypi.org/project/spell-checker/) which is the base of this package.
