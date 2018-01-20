import React,{ Component } from 'react';
import { NavLink } from 'react-router-dom';
import classes from './Tournaments.css';

const tournament = (props) => {
  let url = '/player/' + props.ke;
  return(
    <tr>
        <th><NavLink to={url} exact activeClassName="my-active" activeStyle={{color: '#fa923f',textDecoration: 'underline'}}>{props.name}</ NavLink></th>
        <th>{props.status}</th>
    </tr>
    );
}

export default tournament;