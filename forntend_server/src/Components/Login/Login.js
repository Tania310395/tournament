import React,{ Component } from 'react';
import axios from 'axios';
import { NavLink } from 'react-router-dom';
import classes from './Login.css'; 

class Login extends Component{
  state = {
         username: '',
         password: ''
  }

  postDataHandler = () => {
    const data = {
      username: this.state.username,
      password: this.state.password
    };
    axios.post( "/api/login", data)
      .then(response => {
        const auth_token = response.data.token;
        localStorage.setItem("token", auth_token);
        this.props.history.push("/tournament/");
      })
      .catch( error => {
        alert("Wrong Username/Password Combination")
        console.log( error );
      } );

  }
      
  render () {
    return (
      <div className={classes.Login}>
        <div className={classes.inner}>
          <div className={classes.small}>
          <label><b>Username   </b></label>
          <input type="text" placeholder="Enter Username" value={this.state.username} onChange={(event) => this.setState({username: event.target.value})} required></input>
          </div>
          <div className={classes.small}>
          <label><b>Password   </b></label>
          <input type="password" placeholder="Enter Password" value={this.state.password} onChange={(event) => this.setState({password: event.target.value})} required></input>
          </div>
          <div className={classes.small}>
          <button type="submit" className={classes.btn} onClick={this.postDataHandler}>Login</button>
          </div>
        </div>
      </div>
    );

  }

}
export default Login;