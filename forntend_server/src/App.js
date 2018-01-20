import React, { Component } from 'react';
import logo from './logo.svg';
import classes from './App.css';
import { BrowserRouter } from 'react-router-dom';
import Blog from './Containers/Blog';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div className={classes.App}>
          <Blog />
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
