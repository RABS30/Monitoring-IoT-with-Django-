 let socket;
  if(window.location.protocol == 'http:'){
      socket = new WebSocket('ws://'+window.location.host+'/ws/socket-server/');
 }else{
    socket = new WebSocket('wss://'+window.location.host+'/ws/socket-server/');
}
console.log('Connecting to WebSocket server...');

// Saat berhasil terhubung
socket.onopen = (e) => {
    console.log('berhasil terhubung ke websockets');
    const data = JSON.stringify({
        type   : 'status',
        message: 'connected'});

    socket.send(data);
};

// Saat gagal terhubung
socket.onerror = function(err){
    console.log("Koneksi ke server gagal", err.message);
    socket.close()
};
// Saat koneksi terputus
socket.onclose = function (event) {
    console.log('Disconnected from WebSocket server');
    setTimeout(function(e){
        location.reload();
    }, 4000);
};



export { socket };

