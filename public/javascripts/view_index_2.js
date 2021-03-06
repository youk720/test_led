'use strict';

var socket = io();

// OFFボタン操作時
$('#off').on('click', function() {
  // something commands
  off();
});

// 送信ボタンクリック時
$('#sw').submit(function() {
  sub_send();
});

// Fキー操作時
$('body').on("keydown", function(e) {
if(e.keyCode === 70) {
  //70キー=Fキー off関数召喚
  sub_send();
  }
});

/* 参考サイト
  https://teratail.com/questions/89507
*/

let m = [];
let x = $('input[name=led_select]').change(function(){
  $('input[name=led_select]:checked').each(function(){
    m.push($(this).val());
  });
});

function sub_send(){
  socket.emit("sw status", '');
  socket.emit("sw status", m);
}

function off(){
  // 同上
  socket.emit("sw status", '');
  socket.emit("sw status", m);
}
