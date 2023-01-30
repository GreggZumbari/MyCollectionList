import NavigationBar from './components/Navigation';
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import HomePage from './pages/HomePage'
import LoginPage from './pages/LoginPage'
import RegisterPage from './pages/RegisterPage'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Router>
            <NavigationBar/>
            <Routes>
                <Route path="/" element={<HomePage />}></Route>
                <Route path="/login" element={ <LoginPage />}></Route>
                <Route path="/register" element={ <RegisterPage />}></Route>
            </Routes>
        </Router>
      </header>
    </div>
  );
}

export default App;
