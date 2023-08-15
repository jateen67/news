import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link className="navbar-link" to={"/"}>
              Home
            </Link>
          </li>
          <li>
            <Link className="navbar-link" to={"/about"}>
              About
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}
