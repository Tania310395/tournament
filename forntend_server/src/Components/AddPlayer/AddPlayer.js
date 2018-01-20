import React, { Component } from 'react';
import Player from './Player/Player';
import axios from 'axios';
import { Route, NavLink } from 'react-router-dom';
import classes from './AddPlayer.css';

class Addplayer extends Component {

  state = {
    name: [],
    playername: '',
    pname: ''
  }

  componentDidMount () {
    let url = "/api/playerdetails/" + this.props.match.params.id
    axios.get( url)
      .then( response => {
        const players = response.data.data;
        this.setState( { name: players } );
        } )
        .catch( error => {
            console.log( error );
        } );
  }

  postDataHandler = () => {
    const data = {
      playername: this.state.playername
    };
    let url = "/api/players/" + this.props.match.params.id
    axios.post( url , data)
      .then(response => {
        this.componentDidMount()
      })
      .catch( error => {
          alert("Cannot add Player")
          console.log( error );
      } );

  }

  matchHandler = () => {
    let url = "/api/tournaments/" + this.props.match.params.id
    axios.get(url)
    .then(response => {
      console.log(response)
      url = "/tournament/" + this.props.match.params.id;
      this.props.history.push(url)
    })
    .catch(error => {
      alert("total palyer no is not power of 2")
      console.log(error)
    })
  }

  render () {

      let players = this.state.name.map ( player => {
        return (<Player name={player} />);
      });

      let url = "/tournament/" + this.props.match.params.id;


      return (
        <div className={classes.player}>
        <label className={classes.span}><b>  Player  </b></label>
          <input type="text" placeholder="Add player" value={this.state.playername} onChange={(event) => this.setState({playername: event.target.value})} required></input>
          <br></br>
          <div className={classes.inner}>
          <button className={classes.button} type="submit" id="btn-login" onClick={this.postDataHandler}>Add</button>
          <button className={classes.button} type="submit" onClick={this.matchHandler}>
              Startgame
          </button>
          <section className={classes.players}>
          <table className={classes.tablestructure}>
            {players}
          </table>
          </section>
          </div>
        </div>
      );
    }
}

export default Addplayer;