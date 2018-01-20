import React,{ Component } from 'react';
import axios from 'axios';

class PlayerStandings extends Component {

  state = {
    playerstandings: [],
    round_no: 0
  }


  componentDidMount () {
      this.getPlayerStanding()
  }

  getPlayerStanding(){
    let url = "/api/standings/"+ this.props.id;
    axios.get( url)
      .then( response => {
        let stand = response.data.data;
        this.setState({playerstandings: stand})
      } )
      .catch( error => {
        console.log( error );
      } );

  }




  render (){

    let playerstandings = this.state.playerstandings.map(player => {
      return (
        <tr>
          <th>{player[0]}</th>
          <th>{player[1]}</th>
          <th>{player[2]}</th>
          <th>{player[3]}</th>
        </tr>
      );
    })

    return (
    <div>
      <table>
         <tr>
          <th>Player</th>
          <th>Matchs</th>
          <th>Win</th>
          <th>Looses</th>
        </tr>
        {playerstandings}
      </table>
      <p>{this.props.status}</p>
    </div>
    );
  }
}

export default PlayerStandings;