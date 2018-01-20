import React, { Component } from 'react';
import PlayerMatch from '../../PlayerMatch/PlayerMatch';
import Round from '../Round/Round';
import classes from './Match.css';

class Match extends Component {

  render () {
    return (
      <div className={classes.main}>
      <div className={classes.match}>
      <div  className={classes.player}><PlayerMatch id={this.props.match.params.id} /></div>
      <div  className={classes.other}><Round id={this.props.match.params.id} /></div>
      <div className={classes.clear}></div>
      </div>
      </div>
    );
  }
}

export default Match;