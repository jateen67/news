import display from "../python/data/display.json";

export default function Feed() {
  return (
    <>
      <p className="description">
        The less depressing the news article is, the higher its score will be :D
      </p>
      <div className="articles-container">
        {display.map((article, idx) => {
          return (
            <div key={idx} className="article">
              <p style={{ fontWeight: "bold" }}>{article.title}</p>
              <p
                className="desc"
                style={{ color: "#c4c4c4", overflowY: "auto" }}
              >
                {article.description}
              </p>
              <div className="info-container">
                <p className="info-item">{article.rating.toFixed(1)}</p>
                <a
                  className="view-link info-item"
                  href={article.link}
                  target="_blank"
                  style={{ fontFamily: "Josefin Sans, Times, serif" }}
                >
                  View
                </a>
                <p className="info-item">
                  {new Date(article.published).toLocaleDateString("en-US", {
                    month: "short",
                    day: "numeric",
                    year: "numeric",
                  })}
                </p>
              </div>
            </div>
          );
        })}
      </div>
    </>
  );
}
