# Positive News Finder Neural Network

This site displays news articles gathered from all over Canada, with the less gloomy ones being displayed at the top. It does this by first gathering articles from various news outlets, then feeding the articles into a neural network that will read them and generate a "positivity" score based on their contents.

The less depressing the news article is, the higher its score will be :D

## How it works

The first step is to gather news articles from news outlets, which can be done by accessing each outlet's RSS feed.
[explain more and add pictures for both the scraper and model]

## Data

### IMDb Reviews

The IMDb review data set used to train this model comes from:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

### GloVe

All data used to train this model comes from the `glove.6B.zip` folder found at:
https://nlp.stanford.edu/projects/glove/

**Note**: The data file was not copied to this repository, as it is too large :(

## Technologies

Built using:

- [React.js](https://react.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Python](https://www.python.org/)
- [BeautfulSoup](https://pypi.org/project/beautifulsoup4/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [NLTK](https://www.nltk.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [Keras](https://keras.io/)
- [Matplotlib](https://matplotlib.org/)
