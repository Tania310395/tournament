import React, { Component } from 'react';
import Player from '../AddPlayer/Player/Player';
import axios from 'axios';

class PlayerMatch extends Component {
  state = {
      name: []
  }

  componentDidMount () {
    let url = "/api/playerdetails/"+ this.props.id;
    axios.get( url)
      .then( response => {
        const players = response.data.data;
        this.setState( { name: players } );
        } )
        .catch( error => {
            console.log( error );
        } );
  }

  render () {

        let players = this.state.name.map ( player => {
          return (<Player name={player} />);
        });

        return (
          <div>
          <table>
          <tr><th>Player Name</th></tr>
            <section className="players">
              {players}
            </section>
          </table>
          </div>
        );
      }
}

export default PlayerMatch;