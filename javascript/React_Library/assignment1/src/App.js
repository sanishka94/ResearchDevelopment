import React, { Component } from 'react';

import './App.css';
import './User/UserInput';
import './User/UserOutput';
import UserInput from './User/UserInput';
import UserOutput from './User/UserOutput';

class App extends Component {
  state = {
    username: 'myName'
  }

  usernameChangedHandler = (event) => {
    this.setState({
      username: event.target.value
    })
  }

  render() {
    return (
      <div className="App">
        <h1>This is my assignment attempt</h1>
        <UserInput changed={this.usernameChangedHandler}  value={this.state.username}></UserInput>
        <UserOutput username={this.state.username}></UserOutput>
        <UserOutput username={this.state.username}></UserOutput>
        <UserOutput username={this.state.username}></UserOutput>
      </div>
    );
  }
}


export default App;
