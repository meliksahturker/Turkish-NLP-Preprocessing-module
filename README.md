# Turkish-NLP-Preprocessing-module
Preprocessing tool for Turkish NLP that contains
- tokenizer
- normalizer
- stop-word eliminator
- stemmer.

Developed by Melikşah Türker and Büşra Oğuzoğlu for CMPE561 NLP class project.

https://github.com/meliksahturker

https://github.com/busraoguzoglu

### Sentence Splitter and Tokenizer 
modules have 2 versions, 
- Rule-based: uses RegEx rules.
- Machine learning based: uses handcrafted features.
  - Machine Learning part contains Naive Bayes Classifier and Logistic Regression Classifier. We developed the Naive Bayes algorithm from scratch, but used sklearn implementation for Logistic Regression.

### Stop-Word eliminator 
has 2 versions, 
- Static: requires pre-defined stopwords
- Dynamic: detects the stop-words choosing a threshold according to word frequency distribution, using second derivative(elbow rule) automatically. <strong>Works for any language!</strong>.

### Normalizer 
works using 
- Normalization lexicon
- Levenshtein distance: calculating for:
  - whole word
  - consonant letters only, facilitating the both.

Data folder contains lots of lexicons for multi-word-expressions, normalization, prefixes, abbreviations(non-breaking prefixes), stop-words, etc.
