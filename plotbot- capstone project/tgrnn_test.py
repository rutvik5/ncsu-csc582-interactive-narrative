from textgenrnn import textgenrnn

temp = 0.5

def generate_sentences(genre, prefix, n_sentences):
    tg = textgenrnn()
    tg.load('weights/' + genre + '.hdf5')
    text = tg.generate(return_as_list=True, prefix=prefix, temperature=temp, n_sentences=n_sentences)[0]
    return text


print (generate_sentences('crime', 'Alice attacked Bob', 3))
