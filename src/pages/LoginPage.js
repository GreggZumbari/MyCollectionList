import React from 'react';
import {Link} from 'react-router-dom';

function LoginPage() {
    return (
        <div>
            <h2>
                Log in
            </h2>
            <p>
                Enter user name and password below.
            </p>
            <p>
                New user? <Link to="/register">Register here.</Link>
            </p>
        </div>
    );
}

export default LoginPage;