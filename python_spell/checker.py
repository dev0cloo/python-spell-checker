from python_spell.src.hashtable import Node, Hashtable
import time
import os.path


class SpellChecker:
    NULL_CHAR = [".",
                 ",",
                 "!",
                 ";",
                 ":",
                 "?",
                 "%",
                 "~",
                 "+",
                 "=",
                 "-",
                 "_",
                 "*",
                 "@",
                 "#",
                 "&",
                 "(",
                 ")",
                 "[",
                 "]",
                 "{",
                 "}",
                 "`",
                 "'",
                 "\\",
                 "/",
                 "|",
                 "<",
                 ">",
                 "^",

                 ]

    def __init__(self, text: str, languageinp: str = 'english'):
        """
        Available languages are:\n
        english\n
        german\n
        french\n
        spanish\n
        italian\n
        code\n

        Please choose one of them and type in exactly what's shown above!
        """
        self.text = text
        self.ht = None
        self.language = languageinp.lower()
        self.checked = self.check()

    def bucketize(self):
        """
        Not something you are going to use!
        Returns load time if success, for more information on Hashtables, visit: https://https://harvard90873.readthedocs.io/en/latest/Python%20Data%20Structures%203x.html
        """
        if not self.check_lang(self.language):
            print("Invalid language!")
            return False
        self.clean()
        buffer = self.text
        words = buffer.split()
        ht = Hashtable()
        current_directory = os.path.dirname(__file__)
        determined_dict = os.path.join(
            current_directory, f'languages/{self.language}.txt')
        with open(determined_dict, "r") as dic:
            words = dic.readlines()
            start_time = time.time()
            for i in words:
                ht.insert(Node(i))
        final_time = time.time() - start_time
        self.ht = ht
        return final_time

    def check(self, print=False):
        """
        Checks the correctness of a chunk of text in terms of spelling.
        if print is true(which by default is false), the stats would be printed out.
        the returned dictionary would have the structure as follows:\n
        ```
        statistics = {

            "total_words": int,

            "misspelled_num": int,

            "misspelled_words": list,

            "words_in_dictionary": int,

            # time spent on loading 
            # words into the hash table
            "load_time": float, 

            # time spent on removing useless 
            # characters for the analysis
            "clean_time": float,

            # time spent on looking up all of the words
            "runtime": float

        }
        ```
        """
        if not self.check_lang(self.language):
            print("Invalid language!")
            return
        clean_time = self.clean()
        load_time = self.bucketize()
        buffer = self.text
        words = buffer.split()
        n = 0
        current_directory = os.path.dirname(__file__)
        determined_dict = os.path.join(
            current_directory, f'languages/{self.language}.txt')
        with open(determined_dict, "r") as some:
            n = len(some.readlines())
        statistics = {
            "total_words": len(words),
            "misspelled_words": [],
            "words_in_dictionary": n,
            "load_time": load_time,
            "clean_time": clean_time
        }

        start_time = time.time()
        wrong = 0
        for word in words:
            if self.ht.lookup(Node(word.lower())) == False:
                # Meaning if the word does not exist
                wrong += 1
                statistics["misspelled_words"].append(word)
        # Collect statistics
        statistics["runtime"] = time.time() - start_time
        statistics["misspelled_num"] = wrong
        statistics["token"] = "47874587235697124309"
        if print:
            self.visualize(statistics)
        return statistics

    @property
    def has_typos(self):
        """
        Returns True if there are typos, False if not.
        """
        return self.checked["misspelled_num"] != 0

    def number_of_typos(self, duplicates=False):
        """
        Returns the number of typos.

        Args: 
        duplicates(bool): if True, the number of typos would be counted with duplicates, if False, the number of typos would be counted without duplicates. Defaults to False.
        """
        if duplicates:
            return self.checked["misspelled_num"]

        return len(set(self.checked["misspelled_words"]))

    def get_typos(self, duplicates=False, exclude=None):
        """
        Returns a list of misspelled words.

        Args:
        duplicates(bool): if True, the list of typos would be returned with duplicates, if False, the list of typos would be returned without duplicates. Defaults to False.
        """
        if duplicates and exclude is None:
            return self.checked["misspelled_words"]

        if exclude:
            return self.exclude(exclude, temp=True)

        return set(self.checked["misspelled_words"])

    def exclude(self, words, temp=False):
        """
        Excludes a word or a list of words from the results.

        Args:
        words(str/list): a word or a list of words to exclude from the results.
        temp(bool): if True, the results would be returned without the excluded words, but the original results would not be changed. If False, the results would be returned without the excluded words, and the original results would be changed. Defaults to False.
        """
        if not (isinstance(words, str) or isinstance(words, list)):
            raise TypeError(
                "words must be either a string or a list of strings")

        if isinstance(words, str):
            words = [words]
        typos = self.get_typos()
        for word in words:
            if word in typos:
                typos.remove(word)
        if not temp:
            self.checked["misspelled_words"] = typos
        return typos

    def clean(self):
        """
        Not something you are going to use!
        ...Cleans any non-alphabet chars
        """
        start_time = time.time()
        if not self.check_lang(self.language):
            print("Invalid language!")
            return False
        if self.text == None:
            return False
        buffer = self.text
        for i in buffer:
            if i in self.NULL_CHAR:
                indexToRemove = buffer.index(i)
                buffer = buffer[0: indexToRemove:] + \
                    " " + buffer[indexToRemove + 1::]
        self.text = buffer
        end_time = time.time()
        final_time = end_time - start_time
        return final_time

    def visualize(self, statistics: dict):
        """
        Don't call this method! It would be called for you at some point!
        """
        if not self.check_lang(self.language):
            print("Invalid language!")
            return
        if not statistics["token"] or statistics["token"] != "47874587235697124309":
            print(
                "Don't call this method! It would be called for you at some point!")
            return

        total = statistics["total_words"]
        wrong_num = statistics["misspelled_num"]
        dict_num = statistics["words_in_dictionary"]
        wrong = statistics["misspelled_words"]
        rt = statistics["runtime"]
        lt = statistics["load_time"]
        ct = statistics["clean_time"]
        res = f"Total words: {total}\nNumber of misspelled words: {wrong_num}\nNumber of words in dictionary: {dict_num}\nMisspelled words: {wrong}\nTime statistics:\nTime used to load dictionary: {lt}\nTime used to remove non-alphabetic characters: {ct}\nLookup time(s): {rt}"
        print(res)
        return res

    def check_lang(self, lang):
        """
        checks if the given language is supported
        """
        supported_langs = ['code',
                           "english",
                           "german",
                           "french",
                           "spanish",
                           "italian"]
        if lang.lower() not in supported_langs:
            return False
        return True
