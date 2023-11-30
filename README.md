# Python Spell Checker

The **spell checker** is a python package that can check your spelling. It supports **_5_** languages!

It contains the following languages:

- English
- German
- Spanish
- French
- Italian

All valid words of a language are stored in a text file in the `languages` folder. The words are sorted alphabetically and are in lowercase. You can add your own words to the text file.

# Installation

If not already [install pip](https://pip.pypa.io/en/stable/installing/)

Install the package with `pip` or `pip3`:

```bash
pip install python-spell-checker
```

# Usage

### Example:

```Python
from checker import Checker
text = "The... ! quick browmn fox jumps-over the lazi doug"
checker = Checker(text, "english")

# This returns a dictionary object
check_text = checker.check()
print(check_text)

# This returns a list of misspelt words
misspelt_words = checker.misspelt()
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

Misspelt words are ['browmn', 'lazi']
```

# Credits

Credits to [Harvard90873](https://github.com/Harvard90873/) for creating [spell-checker](https://pypi.org/project/spell-checker/) which is the base of this package.
