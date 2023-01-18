import React, { useState,useEffect } from 'react';
import Board from './Board';

import swal from 'sweetalert';

const Game = () => {
  var [gameover, setGameover] = useState(false);
  var [winer, setWiner] = useState(5);
function restart(value){
  console.log(winer);
  console.log(winer);
  console.log(winer);
  console.log(winer);
  fetch("/restart").then((res) =>
  res.json().then((data) => {
    console.log(data);
    // Setting a data from api
    
   
    setGameover(data[0]);
    
})
  );
  window.location.reload(false);
}

  useEffect(() => {
    // Using fetch to fetch the api from 
    // flask server it will be redirected to proxy
    fetch("/gameover").then((res) =>
    res.json().then((data) => {
      console.log(data);
      // Setting a data from api
      setGameover(data[0]);
  })
    );
}, []);
  return (
    <div className="game">
      <div class="wooden-text">
  <div>MANCALA</div>
  <div class="small">AI GAME</div>
</div>
      {(gameover) ? (<div>{ swal("Game over", "the winer is : player "+winer, "success", {button: "PLay again",}).then((value) => {restart();})}</div>):(<Board setgameState={setGameover} setgamewiner={setWiner}  />)}
      

    </div>
  );
};

export default Game;