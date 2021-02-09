import NounSuffixes
import VerbSuffixes
import sys
import Utility


class Stemmer:


    # Get last 3 character
    # last_chars = sample_str[-3:]

    # Stem function gets a token and returns the
    # possible stem of that token

    def __init__(self):
        self.reserved_stems_list = Utility.load_words('./DATA/reserved_word_list.txt')
        self.small_stems_list = Utility.load_words('./DATA/small_words_list.txt')

    def stemmer_helper(self, token, recursion_count, suffix_list, avg_length):

        # Check if the word is a reserved word (long)
        # Or if the word is too shor

        if token not in self.reserved_stems_list and len(token) > 3:

            for suffix in suffix_list:

                types = suffix.get_types()
                length = len(types[0])
                delete = True

                # If We need to check previous part, first do that
                if suffix.check_before:
                    delete = False
                    irregularities = suffix.get_irregularities()
                    ir_length = len(irregularities[0])

                    for irregularity in irregularities:
                        token_previous = token[:-length]
                        if token_previous[-ir_length:] == irregularity:
                            delete = True

                # Delete if we do not need to check previous part
                # Or delete if we had to check previous part and it matched.
                if delete:
                    for type in types:
                        if token[-length:] == type:
                            # If the word is not in reserved words list:
                            if token not in self.reserved_stems_list and len(token[:-length]) > 2:
                                token = token[:-length]
                                print(token)
                            # Also check if it is a very small stem possibly
                            elif token[:-length] in self.small_stems_list:
                                token = token[:-length]

                # Now check for deletion of previous part irregularity
                if not suffix.delete_before:
                    continue

                # We have to remove some irregularity
                else:
                    irregularities = suffix.get_irregularities()
                    for irregularity in irregularities:
                        if token[-1:] == irregularity:
                            # If the word is not in reserved words list, and remaining
                            # word should be longer than two characters
                            if token not in self.reserved_stems_list and len(token[:-1]) > 2:
                                token = token[:-1]


            # Stem cannot be too long (ex: longer than 8 characters)
            # If so, run stemmer one more time.
            if len(token) <= avg_length or recursion_count > 3:  # lenghti azaltıp bazı korunan wordler listesi olmalı
                return token
            else:
                recursion_count += 1
                # Check bigger stems from a list and return them directly:
                # 'Ayakkabı' gibi
                return Stemmer.stemmer_helper(self, token, recursion_count, suffix_list, avg_length)

        else:
            return token

    def stemmer(self, token):

        noun_stem = token
        verb_stem = token
        nominal_verb_stem = token
        derivational_noun_stem = token

        noun_stem = Stemmer.stemmer_helper(self, noun_stem, 1, NounSuffixes.noun_suffix_list, 7)
        # Also, Check if the stem of this noun is actually a verb
        noun_stem = Stemmer.stemmer_helper(self, noun_stem, 1, VerbSuffixes.verb_to_noun_suffix_list, 5)

        verb_stem = Stemmer.stemmer_helper(self, verb_stem, 1, VerbSuffixes.verb_suffix_list, 5)
        nominal_verb_stem = Stemmer.stemmer_helper(self, nominal_verb_stem, 1, VerbSuffixes.nominal_verb_suffix_list, 7)
        derivational_noun_stem = Stemmer.stemmer_helper(self, derivational_noun_stem, 1, NounSuffixes.noun_derivational_suffix_list, 6)


        len1 = len(noun_stem)
        len2 = len(verb_stem)
        len3 = len(nominal_verb_stem)
        len4 = len(derivational_noun_stem)

        #print(derivational_noun_stem)

        if len1 < len2:
            stem = noun_stem
            print(noun_stem)
            print('is noun')

            # Check if the stem of this noun is actually a verb
            stem = Stemmer.stemmer_helper(self, stem, 1, VerbSuffixes.verb_to_noun_suffix_list, 5)

        else:
            stem = verb_stem
            print('is verb')
            # We said verbs cannot be longer than around 5 characters
            # If so, assign to noun again and go on.
            #if len(stem) > 5:
                #stem = noun_stem

        if len3 < len(stem):
            stem = nominal_verb_stem
            print('no its nominal')
            # Now treat it as verb once more
            stem = Stemmer.stemmer_helper(self, stem, 1, VerbSuffixes.verb_suffix_list, 5)

        if len4 < len(stem):
            print('no is noun')
            stem = derivational_noun_stem

        return stem

