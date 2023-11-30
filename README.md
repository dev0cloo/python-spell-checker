# Python text spell checker for python -v 3+!

The **spell checker** is a python package that can check your spelling. It supports **_5_** languages!

It contains the following languages:

- English
- German
- Spanish
- French
- Italian

# Installation

If not already [install pip](https://pip.pypa.io/en/stable/installing/)

Install the package with `pip` or `pip3`:

```bash
pip install spell-checker
```

# Usage

### Example:

```Python
from speller3x.checker import Checker
text = "The... ! quick browmn fox jumps-over the lazi doug"
checker = Checker(text, "english")
checker.check()
```

Output:

```bash
Total words: 9
Number of misspelled words: 2
Number of words in dictionary: 194433
Misspelled words: ['browmn', 'lazi']
Lookup time(s): 0.0005731582641601562
```

# Credits

Created by [Harvard90873](https://github.com/Harvard90873/)
