from checker import Checker
from pprint import pprint

text = "The... ! quick browmn fox jumps-over the lazi doug"
checker = Checker(text, 'english')
pprint(checker.check_misspelt())
