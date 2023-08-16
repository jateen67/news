export default function About() {
  return (
    <div className="about-container">
      <p>
        This site displays news articles gathered from all over Canada, with the
        less gloomy ones being displayed at the top. It does this by first
        gathering articles from various news outlets, then feeding the articles
        into a neural network that will read them and generate a "positivity"
        score based on their contents.
      </p>
      <p>
        Built with: React.js, TypeScript, Python, BeautifulSoup, scikit-learn,
        NLTK, TensorFlow, Keras, Matplotlib
      </p>
    </div>
  );
}
