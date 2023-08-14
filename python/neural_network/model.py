import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import re
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.layers import LSTM, Embedding
from keras.models import Sequential
from keras.layers.core import Dense
import matplotlib.pyplot as plt

nltk.download("stopwords")

imdb_reviews = pd.read_csv("imdb_reviews.csv")
# safety check
imdb_reviews.shape

"""preprocessing"""


def preprocess(s):
    s = s.lower()

    s = re.compile(r"<[^>]+>").sub("", s)

    # remove punctuations/numbers
    s = re.sub("[^a-zA-Z]", " ", s)

    # remove single letters
    s = re.sub(r"\s+[a-zA-Z]\s+", " ", s)

    # remove places with more than one space
    s = re.sub(r"\s+", " ", s)

    # remove nltk stopwords (regex makes it go wayyy faster than the line below)
    # s = ' '.join([word for word in s.split() if word not in (stopwords.words('english'))])
    s = re.compile(r"\b(" + r"|".join(stopwords.words("english")) + r")\b\s*").sub(
        "", s
    )

    return s


print(preprocess("i use ` rust for BLLLLLAZINGLY fast code    ... its amazing"))

# preprocessing all reviews
preprocessed_text = []

for review in list(imdb_reviews["review"]):
    preprocessed_text.append(preprocess(review))

print(preprocessed_text[1])

# converting each review's "sentiment" column value to 1 and 0 instead of "positive" and "negative"
sentiments = []

for sentiment in imdb_reviews["sentiment"]:
    if sentiment == "positive":
        sentiments.append(1)
    else:
        sentiments.append(0)

sentiments = np.array(sentiments)

print(sentiments[1])

# spliting data into training and test set data for the model
X_train, X_test, y_train, y_test = train_test_split(
    preprocessed_text, sentiments, test_size=0.25, random_state=42
)

"""making embedded layer"""

# transform raw text into numerical representations suitable for feeding into the model
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

# our corpus has 90,094 words in it
# also adding one more to the mix for words that dont have a word embedding (90,095 total)
corpus_length = len(tokenizer.word_index) + 1
print(corpus_length)

# padding reviews to 100 tokens
X_train = pad_sequences(X_train, padding="post", maxlen=100)
X_test = pad_sequences(X_test, padding="post", maxlen=100)

# creating dict that will contain word embeddings for words found in the glove_word_embeddings.txt
word_embeddings_dict = {}
glove_word_embeddings = open("glove_word_embeddings.txt", encoding="utf8")

for line in glove_word_embeddings:
    values = line.split()
    word = values[0]
    embedding_vector = np.asarray(values[1:], dtype="float32")
    word_embeddings_dict[word] = embedding_vector
glove_word_embeddings.close()

# each row corresponds to the index of the word in the corpus
# the matrix has 100 columns, where each column contains the glove embeddings for the words in the corpus
# matrix can now be used as an initial embedding layer when training the neural network
embedding_matrix = np.zeros((corpus_length, 100))

for word, i in tokenizer.word_index.items():
    embedding_vector = word_embeddings_dict.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

print(embedding_matrix.shape)

"""training"""

# setup for a sequential model using our word embeddings and LSTM layer, followed by a final dense layer for binary classification output
model = Sequential()
model.add(
    Embedding(
        corpus_length,
        100,
        weights=[embedding_matrix],
        input_length=100,
        trainable=False,
    )
)
model.add(LSTM(128))
model.add(Dense(1, activation="sigmoid"))

# compile
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
print(model.summary())

# trainingggg
fit_model = model.fit(
    X_train, y_train, batch_size=512, epochs=6, verbose=1, validation_split=0.20
)

# final results
print(model.evaluate(X_test, y_test, verbose=1))

# plot training and validation loss values
plt.plot(fit_model.history["loss"])
plt.plot(fit_model.history["val_loss"])
plt.title("Model Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(["Train", "Validation"], loc="upper right")
plt.show()

# plot training and validation accuracy values
plt.plot(fit_model.history["accuracy"])
plt.plot(fit_model.history["val_accuracy"])
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend(["Train", "Validation"], loc="lower right")
plt.show()

# save
model.save("./model.h5", save_format="h5")

"""news analysis method"""


def analyze_news(path):
    test_reviews = pd.read_csv(path)

    test_preprocessed = []
    for review in test_reviews["Review Text"]:
        review = preprocess(review)
        test_preprocessed.append(review)

    # tokenising with tokenizer from before
    test_tokenized = tokenizer.texts_to_sequences(test_preprocessed)

    # padding to 100 tokens
    test_padded = pad_sequences(test_tokenized, padding="post", maxlen=100)

    # passing tokenized + padded reviews to the model
    test_sentiments = model.predict(test_padded)

    test_reviews["rating"] = np.round(test_sentiments * 10, 1)

    test_reviews = test_reviews.sort_values(by="rating", ascending=False)

    test_reviews.to_json("display.json", orient="records", indent=4, force_ascii=False)
