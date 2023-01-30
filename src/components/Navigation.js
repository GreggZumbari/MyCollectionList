import React from 'react';
import {Link} from 'react-router-dom';

function NavigationBar() {
  return (
    <nav>
       <Link to="/">Home</Link>
       <br></br>
       <Link to="/login">Login</Link>
       <br></br>
    </nav>
  );
}

export default NavigationBar;