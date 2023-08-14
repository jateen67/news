# Positive News Finder Neural Network

This site displays news articles gathered from all over Canada, with the less gloomy ones being displayed at the top. It does this by first gathering articles from various news outlets, then feeding the articles into a neural network that will read them and generate a "positivity" score based on their contents.

The less depressing the news article is, the higher its score will be :D

## How it works

### Gather news feeds

The first step is to gather Canadian news feeds from various outlets, which can be done by accessing each indivdual outlet's [RSS feed](https://en.wikipedia.org/wiki/RSS). This allows us to access the news outlet's updated feed from a single location, making it easy and convenient for us to get the most up-to-date information. In this project, the feeds being gathered are the [CTV News Canada Headlines RSS feed](https://www.ctvnews.ca/rss/ctvnews-ca-canada-public-rss-1.822284) and the [Global News Canada Headlines RSS feed](https://globalnews.ca/canada/feed/).

From the RSS feed, we obtain the news articles' `title`, `description`, `publish date`, and `link` to the full article.

### Scrape each article from the obtained feed

Once we obtain our feed of articles, we iterate through the list and use [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) to scrape the `text` of each article in full (using the link mentioned earlier). This is done so that we have more stuff to feed into the neural network, leading to a higher level of certainty as to whether or not a specific article is positive, as opposed to if we just fed the model the article's very short `title` and `description`.

### Clean up the scraped article text

Naturally, the `text` of each article will be filled with unwanted characters, like `\n`. Because of this, it gets cleaned so that we can pass it into the model later on without a hitch (and because it looks nicer, obviously).

All the web scraping code is centralized at `python/web_scraper/main.py`, meaning running this file will go through the entire process of obtaining the feed, scraping the articles, etc.

### Feed cleaned up news articles into model

Once the entire scraping process is done, the file that contains all the articles (`python/data/news.csv`) gets passed to the model, which will in turn evaluate each article's `title`, `description`, and `text` property and generate a score from 0-10. Naturally, since most news is negative, most of the articles are not being evaluated by how positive they are; they're being evaluated based on how much less negative they are compared to the others.

## The model

The model is a recurrent neural network (RNN), meaning...[TO BE CONTINUED]

Running all the cells in `python/neural_network/model.ipynb` will go through the process of training the neural network and then feeding it the articles to determine the scores for them.

After completing the entire web scraping process, then training and feeding the model, the frontend should be up-to-date and ready!

## Results

[include graphs, observations, etc.]

## Data

### IMDb Reviews

The IMDb review data set used to train this model comes can be found [here](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)

### GloVe Word Embeddings

The data used to create the embedding layer for the neural network comes from the `glove.6B.zip` folder found [here](https://nlp.stanford.edu/projects/glove/)

**Note**: The word embeddings data file was not copied to this repository, as it is too large :( It should normally be located at `python/neural_network`

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
