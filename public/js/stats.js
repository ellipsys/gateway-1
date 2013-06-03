$().ready(function() {
	$.ajax("sensors/dd", {
		success: function(response) {
			console.log(response.links);
		}
	}) ;
});
