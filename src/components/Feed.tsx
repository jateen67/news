import display from "../python/data/display.json";

export default function Feed() {
  return (
    <div>
      {display.map((article, idx) => {
        return (
          <div key={idx} className="article">
            <p>{article.title}</p>
            <p>{article.description}</p>
            <p>{article.published}</p>
            <p>{article.link}</p>
            <p>{article.rating.toFixed(1)}</p>
          </div>
        );
      })}
    </div>
  );
}
