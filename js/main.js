function showInfo(data) {
	console.info("We got the data !")
	console.log(data);
}

$( document ).ready(function() {
	// Data
	console.info( "jQuery is ready!" );
	$.getJSON("data.json", function  (data) {
		showInfo(data);
	});
	

	// Map
	L.mapbox.accessToken = 'pk.eyJ1IjoibWFraW8xMzUiLCJhIjoiWXZmbWtDcyJ9.FNmZbgxFztDTj05JWOBNKA';
	var map = L.mapbox.map('map', 'examples.map-y7l23tes')
		.setView([40, -74.50], 9);
});