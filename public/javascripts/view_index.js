'use strict';
// var $ = require("jquery");

//  ONボタン操作時
$('#on').on('click', function() {
  // something commands
  on();
});
// OFFボタン操作時
$('#off').on('click', function() {
  // something commands
  off();
});

// Fキー操作時
$('body').on("keydown", function(e) {
if(e.keyCode === 70) {
  //70キー=Fキー off関数召喚
  on();
  }
});
// Dキー操作時
$('body').on("keydown", function (m){
  if(m.keyCode === 68){
    //68 = dキー off関数召喚
  off();
  }
});

var socket = io();

// 上でそれぞれ操作があった時に操作する関数
function on(){
  // socketで元々あった、値を消す
  socket.emit("sw status", '');
  // 新しく発光するよう叩く
  socket.emit("sw status", "led=True");
}
function off(){
  // 同上
  socket.emit("sw status", '');
  socket.emit("sw status", "led=False");
}
