import React from 'react';
import classes from './Player.css';

const Player = (props) => {
  return(
    <tr>
        <th>{props.name}</th>
    </tr>
    );
}


export default Player;