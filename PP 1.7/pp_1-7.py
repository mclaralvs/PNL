import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter

def word_count(file):
    # opening the file and get their content
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # splitting the content into words
    words = content.split()

    # count the words' recurrence
    count = Counter(words)

    return count

def txt_stopwords(textwords):
    # get all the stopwords in portuguese
    nltk.download('stopwords')
    stop = stopwords.words('portuguese')

    # get only the stopwords that show up in the text
    stopwords_in_text = [word for word in textwords if word in stop]

    return stopwords_in_text

def get_word_classes(words):
    # geting the Parts Of Speech and their classification
    word_classes = nltk.pos_tag(words)

    # getting their full classification instead of an abbreviation
    class_mapping = {
        'CC': 'Coordenating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun, singular or mass',
        'NNS': 'Noun, plural',
        'NNP': 'Proper noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'SYM': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb, base form',
        'VBD': 'Verb, past tense',
        'VBG': 'Verb, gerund or present participle',
        'VBN': 'Verb, past participle',
        'VBP': 'Verb, non-3rd person singular present',
        'VBZ': 'Verb, 3rd person singular present',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-adverb'
    }

    word_classes_verbose = [(word, class_mapping[pos_tag]) for word, pos_tag in word_classes]

    return word_classes_verbose

def graphic_generate(wordcount):
    # get words and their count
    words = list(wordcount.keys())
    occurences = list(wordcount.values())

    # generate graphic
    plt.figure(figsize=(10, 6))
    plt.bar(words, occurences, color='skyblue')
    plt.xlabel('words')
    plt.ylabel('occurences')
    plt.title('word count - general')
    plt.xticks(rotation=90)
    plt.show()

def graphic_generate_top20(wordcount):
    # ordering by words that had the most occurence
    sorted_wordcount = dict(sorted(wordcount.items(), key=lambda item: item[1], reverse=True))
    
    # getting the top20 words
    top_words = list(sorted_wordcount.keys())[:20]
    occurrences = [wordcount[word] for word in top_words]

    # generate graphic
    plt.figure(figsize=(10, 6))
    plt.bar(top_words, occurrences, color='skyblue')
    plt.xlabel('words')
    plt.ylabel('occurences')
    plt.title('word count - top20')
    plt.xticks(rotation=90)
    plt.show()

def graphic_generate_no_stopwords(wordcount):
    # get words and their count
    words = list(wordcount.keys())
    occurrences = list(wordcount.values())

    # get all the stopwords in portuguese
    nltk.download('stopwords')
    stop_words = stopwords.words('portuguese')

    # remove the stopwords that show up in the text
    filtered_words = [word for word in words if word not in stop_words]
    filtered_occurrences = [wordcount[word] for word in filtered_words]

    # generate graphic
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_words, filtered_occurrences, color='skyblue')
    plt.xlabel('words')
    plt.ylabel('occurences')
    plt.title('word count - general [no stopwords]')
    plt.xticks(rotation=90)
    plt.show()

def graphic_generate_top20_no_stopwords(wordcount):
    # get words and their count
    words = list(wordcount.keys())
    occurrences = list(wordcount.values())

    # get only the stopwords that show up in the text
    nltk.download('stopwords')
    stop_words = stopwords.words('portuguese')

    # remove the stopwords that show up in the text
    filtered_words = [word for word in words if word not in stop_words]
    filtered_occurrences = [wordcount[word] for word in filtered_words]

    # ordering by occurence
    sorted_wordcount = dict(sorted(zip(filtered_words, filtered_occurrences), key=lambda item: item[1], reverse=True))

    # getting the top20 words
    top_words = list(sorted_wordcount.keys())[:20]
    occurrences_no_stopwords = [sorted_wordcount[word] for word in top_words]

    # generate graphic
    plt.figure(figsize=(10, 6))
    plt.bar(top_words, occurrences_no_stopwords, color='skyblue')    
    plt.xlabel('words')
    plt.ylabel('occurences')
    plt.title('word count - top20 [no stopwords]')
    plt.xticks(rotation=90)
    plt.show()


print('Count per Words ✨')
wordcount = word_count('example.txt')
print(wordcount)

print('Stopwords ✨')
stopwords_list = txt_stopwords(wordcount.keys())
print(stopwords_list)

print('Stopwords - Gramatical Classes ✨')
word_classes = get_word_classes(stopwords_list)
print("Word\t\tGramatical Class")
for word, word_class in word_classes:
    print(f"{word}\t\t{word_class}")

print('Graphic - General ✨')
graphic_generate(wordcount)

print('Graphic - Top20 ✨')
graphic_generate_top20(wordcount)

print('Graphic - General [No Stopwords] ✨')
graphic_generate_no_stopwords(wordcount)

print('Graphic - Top20 [No Stopwords] ✨')
graphic_generate_top20_no_stopwords(wordcount)