import React, { useState,useRef,useEffect } from 'react';
import APIService from './Components/APIService'

function   Board  ({setgameState,setgamewiner})  {
  var [GameState, setGameState] = useState({"A": 4,"B": 10, "C": 4, "D": 4, "E": 4, "F": 4, "1": 0, "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4,"2": 0});
 
  
  function getstylerandom(i) {
    var colors = ['rgba(39, 245, 161, 0.71)', 'rgba(39, 153, 245, 0.71)', 'rgba(208, 39, 245, 0.71)'];
    var random_color = colors[i % 3];
    return  {
      backgroundColor:random_color,
      position: 'absolute',
      top: Math.floor(50+(i*7)),
      left: Math.floor(40+(i*2)),
      transform: 'translate(-50%, -50%)',
     
  };
  }
  

   function getstyle(i) {
   
    
   

    
    if (GameState[i] != 0){
     
      return  {
          
     
        boxShadow: '5px 7px 12px 12px rgb(105 211 178)',
       
    };


    }
  }
  function check_gameover(){
   
    fetch("/gameover").then((res) =>
    res.json().then((data) => {
      console.log(data);
      // Setting a data from api
      setgameState(data[0]);
      if(data[0]){
        onclickpi("A")
      }
  })
    );
    var p1 = GameState[1]+GameState["A"]+GameState["B"]+GameState["C"]+GameState["D"]+GameState["E"]+GameState["F"]
    var p2 = GameState[2]+GameState["G"]+GameState["H"]+GameState["I"]+GameState["J"]+GameState["K"]+GameState["L"]
    if(p1 >p2 ){
      setgamewiner(1)
    }else{
      setgamewiner(2)
    }
    console.log(GameState)
  }
  function comp_move(){
    check_gameover();
    APIService.move_comp()
    .then((response) =>{
      // Setting a data from api
      console.log(response)
      
      setGameState({
          "A": response[0].A,
          "B": response[0].B,
          "C": response[0].C,
          "D": response[0].D,
          "E": response[0].E,
          "F": response[0].F,
          "G": response[0].G,
          "H": response[0].H,
          "I": response[0].I,
          "J": response[0].J,
          "K": response[0].K,
          "L": response[0].L,
          1: response[0][1],
          2: response[0][2],
      });
      if(response[1] == 2){
        
        comp_move();

      }
  })
    .catch(error => console.log('error',error))

  

  }
  
  
  
  
  function onclickpi(move1){
    check_gameover();
    var p = "A"
    var move = move1
    APIService.move_player({move,p})
    .then((response) =>{
      // Setting a data from api
      console.log(response)
      
      setGameState({
          "A": response[0].A,
          "B": response[0].B,
          "C": response[0].C,
          "D": response[0].D,
          "E": response[0].E,
          "F": response[0].F,
          "G": response[0].G,
          "H": response[0].H,
          "I": response[0].I,
          "J": response[0].J,
          "K": response[0].K,
          "L": response[0].L,
          1: response[0][1],
          2: response[0][2],
      });
      if(response[1] == 2){

        comp_move();
      }
  })
    .catch(error => console.log('error',error))

  
  }
  useEffect(() => {
    // Using fetch to fetch the api from 
    // flask server it will be redirected to proxy
    fetch("/data").then((res) =>
    res.json().then((data) => {
      // Setting a data from api
      setGameState({
          "A": data.A,
          "B": data.B,
          "C": data.C,
          "D": data.D,
          "E": data.E,
          "F": data.F,
          "G": data.G,
          "H": data.H,
          "I": data.I,
          "J": data.J,
          "K": data.K,
          "L": data.L,
          1: data[1],
          2: data[2],
      });
  })
    );
}, []);
  return (
    <div className="board">
      {console.log(Object.entries(GameState).map(([key, value]) => value))}
  <div class="section endsection">
      <div class="pot" id="mb"> <h8>PLAYER 2 :  {GameState[2]}</h8>{<div class="balls">{[...Array(GameState[2])].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div> 
  </div>
  <div class="section midsection">
    <div class="midrow topmid">
      
      <div class="pot" id="pt1" style={ getstyle("A")} onClick={()=>{onclickpi("A")}}><h8> A  {GameState.A}</h8>  {<div class="balls">{[...Array(GameState.A)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pt2" style={getstyle("B")}   onClick={()=>{onclickpi("B")}}><h8> B  {GameState.B}</h8> {<div class="balls">{[...Array(GameState.B)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pt3" style={getstyle("C")}  onClick={()=>{onclickpi("C")}}><h8> C  {GameState.C}</h8> {<div class="balls">{[...Array(GameState.C)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pt4" style={getstyle("D")}  onClick={()=>{onclickpi("D")}}><h8> D   {GameState.D}</h8> {<div class="balls">{[...Array(GameState.D)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pt5" style={getstyle("E")}  onClick={()=>{onclickpi("E")}}><h8> E  {GameState.E}</h8>  {<div class="balls">{[...Array(GameState.E)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pt6" style={getstyle("F")}  onClick={()=>{onclickpi("F")}}><h8> F  {GameState.F}</h8> {<div class="balls">{[...Array(GameState.F)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
    </div>
    <div class="midrow botmid">
      <div class="pot" id="pb6"><h8> L  {GameState.L}</h8>{<div class="balls">{[...Array(GameState.L)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pb5"><h8> K  {GameState.K}</h8>{<div class="balls">{[...Array(GameState.K)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pb4"><h8> J  {GameState.J}</h8>{<div class="balls">{[...Array(GameState.J)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pb3"><h8> I  {GameState.I}</h8>{<div class="balls">{[...Array(GameState.I)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pb2"><h8> H   {GameState.H}</h8>{<div class="balls">{[...Array(GameState.H)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
      <div class="pot" id="pb1"><h8> G  {GameState.G}</h8>{<div class="balls">{[...Array(GameState.G)].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>
    </div>
  </div>
  <div class="section endsection">
      <div class="pot" id="mt"> <h8>PLAYER 1 :  {GameState[1]}</h8>{<div class="balls">{[...Array(GameState[1])].map((e, i) => <div class="ball b1" style={getstylerandom(i)} ></div>)}</div>}</div>        
  </div>
</div>
    
  );
};

export default Board;