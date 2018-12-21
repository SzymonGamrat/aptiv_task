socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('client_connected', {data: 'Polaczono z nowym klientem'});
});

socket.on('message', function (data) {
    console.log('message form backend ' + data);
});

socket.on('alert', function (data) {
    alert('Alert Message!! ' + data);
});




function LED_on() {
	
     socket.emit('enable_led', '1')
}

function alert_button() {
    socket.emit('disable_led', '0' )
}

function blink_button() {
    socket.emit('blink', '1')
    alert("LED blink");
}


function stop_button() {
	
    socket.emit('STOP', '0')
    alert("LED STOP blinking")	
}

window.onload = function() {
   console.log("foo");
};
