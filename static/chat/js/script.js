const chatSocket = new WebSocket("ws://" + window.location.host + "/");
chatSocket.onopen = function (e) {
  console.log("The connection was setup successfully !");
};
chatSocket.onclose = function (e) {
  console.log("Something unexpected happened !");
};
document.querySelector("#id_message_send_input").focus();
document.querySelector("#id_message_send_input").onkeyup = function (e) {
  if (e.keyCode == 13) {
    document.querySelector("#id_message_send_button").click();
  }
};
document.querySelector("#id_message_send_button").onclick = function (e) {
  var messageInput = document.querySelector(
    "#id_message_send_input"
  ).value;
  chatSocket.send(JSON.stringify({ message: messageInput, username : "{{request.user.username}}"}));
};
chatSocket.onmessage = function (e) {
  const data = JSON.parse(e.data);
  var div = document.createElement("div");
  div.innerHTML = data.username + " : " + data.message;
  document.querySelector("#id_message_send_input").value = "";
  document.querySelector("#id_chat_item_container").appendChild(div);
};