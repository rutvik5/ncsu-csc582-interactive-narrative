# PlotBot

An interactive web page through which a user can generate their own short stories in accordance with the desired genre. Based upon the user-provided information and pre-defined plot skeleton, the RNN would generate the text.

- Choose the genre and provide keywords 

- The web page would present appropriate text (story) with a soundtrack and gif

The application is based on a RNN- LSTM model which is trained on stories related to three genres- crime, romance and horror. Based on the option selected by the user, a text of the particular genre would be displayed on a new webpage. The model is built using a open source dependency- textgenrnn.

#### Textgenrnn- (https://github.com/minimaxir/textgenrnn)
It is a Python 3 module on top of Keras/TensorFlow for creating char-rnns, with many cool features:

- A modern neural network architecture which utilizes new techniques as attention-weighting and skip-embedding to accelerate training and improve model quality.
- Train on and generate text at either the character-level or word-level.
- Configure RNN size, the number of RNN layers, and whether to use bidirectional RNNs.
- Train on any generic input text file, including large files.
- Train models on a GPU and then use them to generate text with a CPU.
- Utilize a powerful CuDNN implementation of RNNs when trained on the GPU, which massively speeds up training time as opposed to typical LSTM implementations.
- Train the model using contextual labels, allowing it to learn faster and produce better results in some cases.
