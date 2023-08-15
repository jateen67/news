import display from "../python/data/display.json";

export default function Feed() {
  return (
    <>
      <div className="top-stories-container">
        <div className="top-stories-label">
          <p>TOP STORIES</p>
        </div>
        <div className="top-stories">
          <div className="top-story">
            <p>title</p>
            <p>date</p>
            <p>score</p>
          </div>
        </div>
      </div>
      <div className="latest-stories-container">
        <div className="latest-stories-label">
          <p>LATEST STORIES</p>
        </div>
        <div className="latest-stories">
          <div className="latest-story">
            <p>title</p>
            <p>date</p>
            <p>score</p>
          </div>
        </div>
      </div>
      <div className="articles-container">
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
    </>
  );
}
