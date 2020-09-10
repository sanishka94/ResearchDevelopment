import React, { Component } from 'react';
import './App.css';

class App extends Component {
  state = ({
    text: []
  })

  textChangeHandler = (event) => {
    let textArray = (event.target.value).split('');
    const newText = textArray.map((l, index) => {
      return { id: index, letter: l }
    });
    console.log(newText);
    this.setState({
      text: newText
    })
  }

  charClickHandler = (key) => {
    let letterIndex = this.state.text.findIndex(t => {
      return t.id === key;
    });

    const newChars = [...this.state.text];
    newChars.splice(letterIndex, 1);
    this.setState({
      text: newChars  
    })
  }

  render() {
    let chars = (
      this.state.text.map(t => {
        return (
          <CharComponent
            click={() => this.charClickHandler(t.id)}
            letter={t.letter}></CharComponent>
        )
      })
    );

    return (
      <div className="App">
        <div>
          <input 
          type="text" 
          onChange={(event) => this.textChangeHandler(event)} 
          value={this.state.text.map(t => t.letter).join('')} />
          
          <p>This is the new text: {(this.state.text).length}</p>
          <ValidationComponent textLength={(this.state.text).length}></ValidationComponent>
        </div>
        <div>
          {chars}
        </div>
      </div>
    );
  }
}

export default App;

const ValidationComponent = (props) => {
  return <p>{props.textLength < 5 ? "Text too short" : "Test too long"}</p>;
}

const CharComponent = (props) => {
  const style = {
    display: 'inline-block',
    padding: '16px',
    textAlign: 'center',
    margin: '16px',
    border: '1px solid black'
  }

  return <p onClick={props.click} style={style}>{props.letter}</p>;
}

