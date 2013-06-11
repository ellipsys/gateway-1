$().ready(function() {

	$.get('/data.html', function(data) { 
		var lines = data.split('\n');
		var data = [];
		var rowData = [];
	
		$.each(lines, function(lineNo, value) { 
			var row = value.split(',');		
			if (row[1] != undefined) { 
				if (parseFloat(row[1]) < 40 && parseFloat(row[1]) > 5) {
					data.push([row[0]*1000, parseFloat(row[1])]);
				}
			}
			rowData.push(row[0]*1000);
		});	

    Highcharts.setOptions({                                            // This is for all plots, change Date axis to local timezone
      global : {
        useUTC : false
      }
    });

		$('#container').highcharts('StockChart', {
           	chart: {
							zoomType: 'xy'
						},
						title: {
                text: 'Temperatuur'
            },

            //subtitle: {
            //    text: 'Source: Google Analytics'
            //},

            xAxis: {
                type: 'datetime',
								ordinal: false,
                tickInterval: 3 * 3600 * 1000, // one week
                tickWidth: 1,
                gridLineWidth: 1,
								
                labels: {
                    align: 'left',
                    x: 3,
                    y: -3
                }
            },

            yAxis: [{ // left y axis
                title: {
                    text: null
                },
                labels: {
                    align: 'left',
                    x: 3,
                    y: 16,
                    formatter: function() {
                        return Highcharts.numberFormat(this.value, 0);
                    }
                },
                showFirstLabel: false
            }, { // right y axis
                linkedTo: 0,
                gridLineWidth: 0,
                opposite: true,
                title: {
                    text: null
                },
                labels: {
                    align: 'right',
                    x: -3,
                    y: 16,
                    formatter: function() {
                        return Highcharts.numberFormat(this.value, 0);
                    }
                },
                showFirstLabel: false
            }],

            legend: {
						    enabled: true,
								layout: 'vertical',
								align: 'left',
                verticalAlign: 'middle',
                y: 20,
                //floating: true,
                borderWidth: 0
            },

            tooltip: {
                shared: true,
                crosshairs: true
            },

            plotOptions: {
                line: {
									gapSize: 0
								},
								series: {
                    cursor: 'pointer',
                    point: {
                        events: {
                            click: function() {
                                hs.htmlExpand(null, {
                                    pageOrigin: {
                                        x: this.pageX,
                                        y: this.pageY
                                    },
                                    headingText: this.series.name,
                                    maincontentText: Highcharts.dateFormat('%A, %b %e, %Y', this.x) +':<br/> '+
                                        this.y +' visits',
                                    width: 200
                                });
                            }
                        }
                    },
                    marker: {
                  		enabled: false,  
									    lineWidth: 0 
                    }
                }
            },

            series: [{
								name: 'Sensor 1',
                lineWidth: 2,
								marker: {
                    radius: 1 
                },
								data: data
            },{
								name: 'Sensor 2',
                lineWidth: 2,
								marker: {
                    radius: 1 
                },
								data: data
            }]
	 	});
});
});
