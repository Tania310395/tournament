import React, { Component } from 'react';
import Tournament from './Tournaments/Tournaments';
import axios from 'axios';
import classes from './Addtournament.css';

class AddTournament extends Component{
  state = {
    tournament: [],
    tour: '',
    id: '',
    name: '',
    status: ''
  }

  componentDidMount () {
    axios.defaults.headers.common['X-Auth-Token']=localStorage.getItem('token');          
    axios.get( "/api/tournaments")
      .then( response => {
        const updatedPosts = response.data.data;
        this.setState( { tournament: updatedPosts } );
        } )
        .catch( error => {
            alert("Tournament already exists")
            console.log( error );
        } );
  } 

  postDataHandler = () => {
    const data = {
      name: this.state.tour
    };
    axios.post( "/api/tournaments", data)
      .then(response => {
        this.componentDidMount()
      })
      .catch( error => {
          alert("Tournament already exists")
          console.log( error );
      } );
  }


  render () {

      let tours = this.state.tournament.map ( tour => {
        return (
          <Tournament
           ke={tour[0]}
           name = {tour[1]}
           status = {tour[2]} />
        );
      });

    return (
      <div className={classes.tournament}>
      <label className={classes.span}><b>   Tournament   </b></label>
        <input type="text" placeholder="Enter Tournament" value={this.state.tour} onChange={(event) => this.setState({tour: event.target.value})} required></input>
        <br></br>
        <div className={classes.inner}>
        <button type="submit" className={classes.btn} onClick={this.postDataHandler}>Add</button>
        <section className="tours">
        <table className={classes.tablestructure}>
          {tours}
        </table>
        </section>
      </div>
      </div>
    );
  }


}

export default AddTournament;

