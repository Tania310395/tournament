import React, { Component } from 'react';
import { Route, NavLink, Switch, Redirect } from 'react-router-dom';
import Signup from '../Components/Signup/Signup';
import Login from '../Components/Login/Login';
import Tournament from '../Components/AddTournament/AddTournament';
import AddPlayer from '../Components/AddPlayer/AddPlayer';
import Match from '../Components/Match/MainMatch/Match';
import classes from './Blog.css';
import axios from 'axios';
import Home from '../Components/Home/Home';

class Blog extends Component{
  render (){

    return (
      <div> 
        <header className={classes.header}>
            <h1>Swiss Tournament</h1>
            <div>
        <button className={classes.tab}>Already a member? <NavLink to="/login/" exact activeClassName="my-active" activeStyle={{color: 'black',textDecoration: 'underline'}}>Login</NavLink></button>
        <button className={classes.tab}>Not a member? <NavLink to="/signup/" exact activeClassName="my-active" activeStyle={{color: 'black',textDecoration: 'underline'}}>Signup</NavLink></button>
        </div>
        </header>
        <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/signup" component={Signup} />
            <Route path='/tournament/:id' exact component={Match} />
            <Route path='/tournament' component={Tournament} />
            <Route path='/player/:id' exact component={AddPlayer} />
        </Switch>
      </div>
    );
  }

}
export default Blog;

