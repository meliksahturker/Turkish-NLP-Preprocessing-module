import re
from TokenizationRules import *
import Utility
from nltk.tokenize import MWETokenizer

class RuleBasedTokenizer:

    def __init__(self):
        self.mwe_lexicon = Utility.load_words('./DATA/MWE_lexicon.txt')
        self.abbrevations = Utility.load_words('./DATA/abbrevations.txt')

    def tokenize(self, input_sentence, rules=rules, split_characters=split, split_token='<*>'):
        sentence = input_sentence

        # Check regular expressions for matches and add split:
        for rule in rules:
            sentence = re.sub(rule, " \g<0> ", sentence)   #The backreference \g<0> substitutes in the entire substring matched by the RE.

        # Split from all splitted characters
        working_sentence = re.sub(split_characters, split_token, sentence)
        list_of_token_strings = [x.strip() for x in working_sentence.split(split_token) if x.strip() !=""]

        original_list_of_token_strings = list(list_of_token_strings)

        # Normalization:
        index = 0
        inserted_dots = 0
        for token in original_list_of_token_strings:
            index += 1
            if token[-1] == '.':
                abbrevation = False
                # Check if abbrevation:
                if token in self.abbrevations:
                    abbrevation = True
                if not abbrevation:
                    new_token = token[:-1]
                    list_of_token_strings.insert(index + inserted_dots, '.')
                    list_of_token_strings[index + inserted_dots-1] = new_token
                    inserted_dots += 1

        # Multi Word Expressions
        # Known bug:
        # If MWE appears at the end of the sentence,
        # Bug appears.

        original_length = len(original_list_of_token_strings)
        original_list_of_token_strings = list(list_of_token_strings)
        index = 0

        while index < original_length:

            token = original_list_of_token_strings[index]

            for expression in self.mwe_lexicon:
                expression_length = expression.count(' ') + 1
                check_index = index
                is_multiword = True

                for i in range(expression_length):
                    if index+i >= original_length:
                        continue
                    else:
                        if original_list_of_token_strings[index+i] not in expression:
                            is_multiword = False

                if is_multiword:
                    # Pass if already multiword:
                    if token.count(' ') == 0:
                        list_of_token_strings.insert(index, expression)

                        for deleter in range(expression_length):
                            if index+1 < original_length:
                                list_of_token_strings.pop(index + 1)

                        index += expression_length

            index += 1


        return list_of_token_strings





def main():

    # Testing purposes

    test_sentence1 = "merhaba, name@gmail.com <html>!! www.abc.com #hello selam# nasılsınız:  Milli Eğitim Bakanlığı 2.01.1997'de 20:02'de aradı"
    test_sentence2 = "www.assignment.com.tr adresine gir. name@gmail.com a Dr. hanıma mail at."
    test_sentence3 = "bizi new jersey bekler"

    # Multiword expressions
    # Test for including multiword expressions:
    mwe = MWETokenizer([('Milli', 'Eğitim', 'Bakanlığı'), ('Bilkent', 'Üniversitesi')], separator='_')

    tokenizer = RuleBasedTokenizer()

    list_of_tokens = tokenizer.tokenize(test_sentence2)
    mwe_list_of_tokens = mwe.tokenize(list_of_tokens)

    print(list_of_tokens)


if __name__ == '__main__':
    main()