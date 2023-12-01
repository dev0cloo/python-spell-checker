# Python Spell Checker

The **spell checker** is a python package that can check your spelling. It supports **_6_** languages!

It contains the following languages:

- English
- German
- Spanish
- French
- Italian
- Code

**_Code_** is a special language that contains the english language along with syntaxes and keywords of programming languages. This is to prevent the spell checker from marking them as misspelt words when the checker is used on a codebase. The words are stored in `code.txt` in `languages` folder.

All valid words of a language are stored in a text file in the `languages` folder. The words are sorted alphabetically and are in lowercase. You can add your own words to it. You can also delete words from the text file to exclude them as valid words.

# Installation

The easiest way to install the package is to use `pip` or `pip3`:

```bash
pip install python-spell-checker
```

or you can clone the repository and use the files:

```bash
    git clone https://github.com/dev0cloo/python-spell-checker.git
    cd python-spell-checker
```

# Usage

The main file is `checker.py` in the `python_spell` folder.

The `SpellChecker` class is used to check the spelling of a text. It takes two arguments:

- `text`: The text to be checked
- `language`: The language of the text. It is set to `english` by default. The language must be one of the following:
  - `english`
  - `german`
  - `spanish`
  - `french`
  - `italian`
  - `code`

The `check()` method is used to check the spelling of the text. It returns a dictionary object with the following relevant keys:

- `total_words`: The total number of words in the text
- `misspelled_num`: The number of misspelled words in the text
- `words_in_dictionary`: The number of words in the dictionary of the language
- `misspelled_words`: A list of misspelled words

The `has_typos` attribute returns a boolean for if the text has typos or not.

The `number_of_typos()` method returns the number of typos in the text. It takes an optional argument `duplicates` which is set to `False` by default. If it is set to `True`, then each duplicate word is counted as a typo. If it is set to `False`, then each duplicate word is counted as a single typo.

The `get_typos()` method returns a list of misspelt words. It takes the optional arguments `duplicates` and `exclude`. `duplicates` is set to `False` by default and works the same as in `number_of_typos()`. `exclude` is a string or a list of strings that are excluded from the returned list of misspelt words. It is set to `None` by default.

`exclude` can be used to exclude words that are not in the dictionary but are valid words without changing the language file. It takes an optional argument `temp` which is set to `False` by default. If it is set to `True`, then the words are excluded only for the current method call and not the whole instance. If it is set to `False`, then the words are excluded for the whole instance. This is useful if you want to exclude words for a single method call but not for the whole instance.

#### Note

The SpellChecker class calls the `check()` method when it is initialized. So, you can directly use the `has_typos`, `number_of_typos()`, `get_typos()` and `exclude` methods without first calling the `check()` method. You can access the dictionary object returned by the `check()` method using the `checked` attribute.

### Example:

```Python
from python_spell.checker import SpellChecker
text = "The... ! quick browmn fox jumps-over the lazi dog"
checker = SpellChecker(text, "english")

# This returns a dictionary object with all information
check_text = checker.checked
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

# This returns a list of misspelt words excluding the words in the list
misspelt_words = checker.get_typos(exclude="lazi")
print("Misspelt words with exlusion are " , misspelt_words)

# This returns a list of misspelt words excluding the words in the list for the current instance
checker.exclude("browmn") # This excludes the word "browmn" for the whole instance
misspelt_words = checker.get_typos()
print("Misspelt words after using the exclude method first are " , misspelt_words)
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

Misspelt words with exlusion are ['browmn']

Misspelt words after using the exclude method first are ['lazi']

```

# Contributing

We welcome contributions to this project, especially those that help us fix bugs, add new words or improve the docs. If you would like to contribute, please fork the repo and submit a pull request.

# Credits

Credits to [Harvard90873](https://github.com/Harvard90873/) for creating [spell-checker](https://pypi.org/project/spell-checker/) which is the base of this package.
