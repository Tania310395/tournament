import React, {Component} from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import classes from './Reportmatch.css';

class ReportMatch extends Component {

  state = {
    reportmatch: []
  }


  componentDidMount () {
      this.getreport()
  }

  getreport(){
    let url = "/api/reportmatch/"+ this.props.id + "/" + this.props.round;
    axios.get( url)
      .then( response => {
        let rm = response.data.matchdetails;
        console.log(response)
        this.setState({reportmatch: rm})
      } )
      .catch( error => {
        console.log( error );
      } );
  }


  render (){

    let report = this.state.reportmatch.map(match => {
      return(
        <tr className={classes.tablevalue}>
          <td>{match[0]}</td>
          <td>{match[1]}</td>
          <td>{match[2]}</td>
        </tr>
      );
    })

    let url = "/tournament/" + this.props.id


    return (
      <div>
      <table>
        <tr>
           <th>Player1</th>
           <th>Player2</th>
           <th>Winner</th>
        </tr>
        {report}
      </table>
      <button type="submit" className={classes.btn} onClick={this.props.close}>Close</button>
      </div>
    );
  }
}

export default ReportMatch;