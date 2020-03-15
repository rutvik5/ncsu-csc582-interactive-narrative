from textgenrnn import textgenrnn


def train_genre(genre, n_epochs):
    tg = textgenrnn()
    tg.train_from_file('corpus/' + genre + '.txt', num_epochs=n_epochs)
    tg.save('weights/' + genre + '.hdf5')


train_genre('crime', 5)
train_genre('horror', 1)
train_genre('romance', 1)
