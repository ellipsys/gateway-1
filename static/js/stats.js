$().ready(function() {
	$.ajax("/api/sensors/1234", {
		success: function(response) {
			$('#uptime').text(response.uptime);
			console.log($('#uptime'));
		}
	}) ;
});
