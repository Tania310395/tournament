import React, { Component } from 'react';
import axios from 'axios';
import PlayerStandings from '../Playerstandings/Playerstandings';
import Round from '../Round/Round';
import { Link } from 'react-router-dom';
import classes from './Swisspairing.css';

class SwissPairing extends Component {
  state = {
    swisspairing: [],
    winner: [],
    standing_update: false
  }

  componentDidMount () {
      this.getswisspairing()
  }

  getswisspairing(){
    let url = "/api/swisspairing/"+ this.props.id;
    axios.get( url)
      .then( response => {
        let sp = response.data.swiss_pairing;
        let w = response.data.winner;
        console.log(w)
        this.setState({swisspairing: sp, winner: w})
      } )
      .catch( error => {
        console.log( error );
      } );

  }


  changeWinnerHandler = (index, name) => {

    this.state.winner.splice(index,1,name)
    console.log(this.state.winner)
  }

  FinishHandler = () => {
    let url = "/api/matchs/"+ this.props.id;
    this.state.swisspairing.map((swisspairing,index) => {
      let data = {
        player1: swisspairing[0],
        player2: swisspairing[1],
        winner: this.state.winner[index]
      }
      axios.post(url, data)
      .then(response => {
        console.log(data)
        console.log(response)
        this.setState({standing_update: true})
      })
      .catch( error => {
        console.log(data)
      })
    })
    axios.get()

  } 

  render (){

    let swisspairings = this.state.swisspairing.map((swisspairing, index) => {
      console.log(index)
      return (
        <tr>
          <td>{swisspairing[0]}</td>
          <td>{swisspairing[1]}</td>
          <td>
             <select onChange={( event ) => this.changeWinnerHandler(index, event.target.value)}>
                 <option>{swisspairing[0]}</option>
                 <option>{swisspairing[1]}</option>
             </select>
          </td> 
        </tr>
      );
    })

    return (
      <div>
      <table>
        <tr className={classes.tablevalue}>
           <th>Player1</th>
           <th>Player2</th>
           <th>Winner</th>
        </tr>
          {swisspairings}
      </table>
      <button type="submit" className={classes.btn} onClick={this.FinishHandler}>Finish</button>
      <button type="submit" className={classes.btn} onClick={this.props.close}>Close</button>
      </div>
    );
  }
}

export default SwissPairing;