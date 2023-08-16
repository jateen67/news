import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <>
      <nav className="navbar">
        <div className="navbar-items-container">
          <ul className="navbar-items">
            <li className="navbar-item">
              <Link className="navbar-link" to={"/"}>
                Home
              </Link>
            </li>
            <li className="navbar-item">
              <Link className="navbar-link" to={"/about"}>
                About
              </Link>
            </li>
          </ul>
        </div>
      </nav>
    </>
  );
}
