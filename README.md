# Positive News Finder Neural Network

This site displays news articles gathered from all over Canada, with the less gloomy ones being displayed at the top. It does this by first gathering articles from various news outlets, then feeding the articles into a neural network that will read them and generate a "positivity" score based on their contents.

The less depressing the news article is, the higher its score will be :D

### How to run

1. run `npm run dev` to start the run the front-end
2. `cd` into the `python/web_scraper` directory. This is the directory where all the news articles are scraped and gathered
3. Run `python main.py` to run the main script
4. `cd` into the `python/neural_network` directory. This is the directory where the news article are taken and fed into a model, which will dictate the overall "positivity" score of the article
5. Run `python main.py` to run the main script
6. The news on the screen should be up-to-date!

### Technologies

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
