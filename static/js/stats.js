$().ready(function() {
	$.ajax("/sensors/dd", {
		success: function(response) {
			$('#uptime').text(response.uptime);
			console.log($('#uptime'));
		}
	}) ;
});
