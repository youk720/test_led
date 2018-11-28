'use strict';
// var $ = require("jquery");

$('#on').on('click', function() {
  // something commands
  on();
});
$('#off').on('click', function() {
  // something commands
  off();
});
// module.exports = led_status;
$('body').on("keydown", function(e) {
if(e.keyCode === 70) {
  //70キー=Fキー off関数召喚
  on();
  }
});
$('body').on("keydown", function (m){
  if(m.keyCode === 68){
    //68 = dキー off関数召喚
  off();
  }
});
var socket = io();
function on(){
  socket.emit("sw status", '');
  socket.emit("sw status", "led=True");
  $('#result').html("led=True");
}
function off(){
  socket.emit("sw status", '');
  socket.emit("sw status", "led=False");
  $('#result').html("led=False");
}
