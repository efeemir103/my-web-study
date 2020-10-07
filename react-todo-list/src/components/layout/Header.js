import React from 'react';
import { Link } from 'react-router-dom';

import './Header.css';

function Header({children}) {
    return (
        <header className="Header">
            <h1>{children}</h1>
            <Link className="Link" to="/">Home</Link> | <Link className="Link" to="/about">Home</Link>
        </header>
    );
}

export default Header;