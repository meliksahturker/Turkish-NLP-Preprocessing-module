import Utility
from RuleBasedTokenizer import RuleBasedTokenizer


# NOT ONEMLİ: Stopword listesi https://github.com/ahmetax/trstop adresinden alındı.
# Kaynak belirtmek gerekir. Onun dışında o adresten kod kullanılmadı.


class StaticStopwordRemover:

    def __init__(self):
        self.Tokenizer = RuleBasedTokenizer()
        self.stop_words_list = Utility.load_words('./DATA/turkce-stop-words.txt')

    def remove_stopwords(self, sentence):
        word_tokens = self.Tokenizer.tokenize(sentence)

        filtered_sentence = []

        for w in word_tokens:
            if w not in self.stop_words_list:
                filtered_sentence.append(w)

        return word_tokens, filtered_sentence


#def main():

#    stop_words = load_words('turkce-stop-words')  # Stop wordleri import et
#    example_sent = """Deneme deneme ama bu şu o bu bir cümle ve belki bu bir cümle"""

#    word_tokens, filtered_sentence = StopwordRemover.remove_stopwords(example_sent, stop_words)

#    print(word_tokens)
#    print(filtered_sentence)

#if __name__ == '__main__':
#    main()
