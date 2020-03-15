from nltk.tag import pos_tag
import nltk
import json

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def extract(genre):
    proper_nouns = []
    with open('corpus/' + genre + '.txt', 'r') as c:
        for line in c:
            tagged_line = pos_tag(line.split())
            for word in tagged_line:
                if word[1] == 'NNP' and word[0] not in proper_nouns:
                    proper_nouns.append(word[0])
    proper_noun_tags = []
    for proper_noun in proper_nouns:
        proper_noun_tags.append({'noun': proper_noun, 'tag': ''})
    with open('corpus/' + genre + '_NNP.json', 'w') as f:
        json.dump(proper_noun_tags, f)


extract('crime')
