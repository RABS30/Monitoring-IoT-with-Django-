let socket = new WebSocket('ws://127.0.0.1:8000/ws/socket-server/');
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
    ws.close()
};
// Saat koneksi terputus
socket.onclose = function (event) {
    console.log('Disconnected from WebSocket server');
    setTimeout(function(e){
        location.reload();
    }, 4000);
};



export { socket };

