$().ready(function() {
	$.ajax("sensors/dd", {
		success: function(response) {
			console.log(response);
			$("#uptime").text(response.uptime);
		}
	}) ;
});
