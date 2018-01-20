import React,{ Component } from 'react';
import axios from 'axios';
import SwissPairing from '../Swisspairing/Swisspairing';
import ReportMatch from '../Reportmatch/Reportmatch';
import Modal from '../../UI/Modal/Modal';
import classes from './Round.css';

class Round extends Component{

  state = {
    round: [],
    playerstandings: [],
    status: false,
    conditionalrender: false,
    matchrender: false,
  }

   roundid = {
    roundid: 0
  }



  componentDidMount () {
    this.getPlayerStanding()
    this.getrounddetails()
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

  getrounddetails(){
    let url = "/api/round/"+ this.props.id;
    axios.get( url)
      .then( response => {
        let r = response.data.data;
        this.setState({round: r})
        
      } )
      .catch( error => {
        console.log( error );
      } );
  }

  ModalPlayHandler = () => {
    this.setState({status: true, conditionalrender: false})
  }

  Modalcancelhandler = () => {
    this.setState({status: false, matchrender: true})
    this.getrounddetails()
  }

  ModalViewHandler = ( val ) => {
    this.setState({status: true, conditionalrender: true}) 
    this.roundid.roundid = val
    console.log(this.roundid.roundid)
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


    let rounds = this.state.round.map(round => {
      let button = round[1]
      if (button){
        if (button == 'View'){
        return (
          <tr>
            <th>Round{round[0]}</th>
            <td><button type="submit" class={classes.btn} onClick={() => this.ModalViewHandler(round[0])}>{round[1]}</button></td>
          </tr>
        );
       }
       else {
        return (
          <tr>
            <th>Round{round[0]}</th>
            <td><button type="submit" class={classes.btn} onClick={this.ModalPlayHandler}>{round[1]}</button></td>
          </tr>
        );
       }
      }
    return (
      <tr>
        <th>Round{round}</th>   
      </tr>
    );
      
    }) 


    let viewModal = <SwissPairing id={this.props.id} close={this.Modalcancelhandler} status={this.props.status}/>
    if (this.state.conditionalrender){
      viewModal = <ReportMatch id={this.props.id} round={this.roundid.roundid} close={this.Modalcancelhandler} status={this.props.status}/>
    } 

    if(this.state.matchrender){
      return (
        <Round id={this.props.id} />
      );

    }
    else{
      return (
      <div>
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
      <div>
        <table className={classes.round}>
            {rounds}
        </table>
        <Modal show={this.state.status} modalClosed={this.Modalcancelhandler}>
            {viewModal}
        </Modal>
      </div>
      </div>
      );
    }


  }
}

export default Round;