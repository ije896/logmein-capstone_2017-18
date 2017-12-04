window.onload = function() {
    var ctx = document.getElementById("myChart").getContext('2d');
				var myChart = new Chart(ctx, {
					type: 'horizontalBar',
					data: {
						labels: ["110 - 120 wpm", "120 - 130 wpm", "130 - 140 wpm", "140 - 150 wpm"],
						datasets: [{
							label: 'Frequency of Speech Rate',
							data: [0.5, 0.1, 0.3, 0.1],
							backgroundColor: [
								'rgba(255, 99, 132, 0.2)',
								'rgba(54, 162, 235, 0.2)',
								'rgba(255, 206, 86, 0.2)',
								'rgba(75, 192, 192, 0.2)'
							],
							borderColor: [
								'rgba(255,99,132,1)',
								'rgba(54, 162, 235, 1)',
								'rgba(255, 206, 86, 1)',
								'rgba(75, 192, 192, 1)'
							],
							borderWidth: 1
						}]
					},
					options: {
						scales: {
							xAxes: [{
								ticks: {
									beginAtZero: true
								}
							}],
							yAxes: [{
								ticks: {
									beginAtZero: true
								}
							}]
						}
					}
				});


				var ctx_2 = document.getElementById("myChart-2").getContext('2d');
				var myChart_2 = new Chart(ctx_2, {
					"type":"line",
					"data": {
						"labels": ["Start","","","","","","End"],
						"datasets":
							[{"label":"Pitch ","data":[125,140,130,120,120,125,140],
								"fill":false,"borderColor":"rgb(75, 192, 192)",
								"lineTension":0.1
							}]},
					"options":{
						scales: {
							yAxes: [{
								ticks: {
									min: 100,
									max: 160
								}
							}]
						}
					}});

				var ctx_3 = document.getElementById("myChart-3").getContext('2d');
				var myChart_3 = new Chart(ctx_3,{
					"type": "radar",
					"data": {
						"labels": ["Anger", "Disgust", "Fear", "Joy", "Sadness"],
						"datasets": [
							{
								"label": "Emotional Tone",
								"data": [0.4, 0.1, 0.3, 0.7, 0.6],
								"fill": true,
								"backgroundColor": "rgba(255, 99, 132, 0.2)",
								"borderColor": "rgb(255, 99, 132)",
								"pointBackgroundColor": "rgb(255, 99, 132)",
								"pointBorderColor": "#fff",
								"pointHoverBackgroundColor": "#fff",
								"pointHoverBorderColor": "rgb(255, 99, 132)"
							}
							]
					},
					"options":
						{
							"elements":
								{
									"line":
										{
											"tension": 0,
											"borderWidth": 3
										}
								}
						}
				});


				var ctx_4 = document.getElementById("myChart-4").getContext('2d');
				var myChart_4 = new Chart(ctx_4, {
					"type":"line",
					"data": {
						"labels": ["3rd","4th","5th","6th","7th", "8th", "9th", "10th", "11th", "12th", "12+"],
						"datasets":
							[{"label":"Grade Level Readability ","data":[,,,,,,0,,,],
								"fill":false,"borderColor":"rgb(75, 192, 192)",
								"lineTension":0.1
							}]},
					"options":{
						scaleShowLabels: false,
						scales: {
							yAxes: [{
								// display: false,
								gridLines : {
                    				drawBorder: false,
                				},
								ticks: {
									min: 0,
									max: 0
								},
								afterBuildTicks: function(myChart_4) {
									myChart_4.ticks = [];
									myChart_4.ticks.push();
								  }

							}],
							xAxes: [
								{
									gridLines: {

									}
								}
							]

						}
					}});

				var ctx_5 = document.getElementById("myChart-5").getContext('2d');
				var myChart_5 = new Chart(ctx_5, {
					type: 'bar',
					data: {
						labels: ["Left", "Mid-left", "Mid", "Mid-right", "Right"],
						datasets: [{
							label: 'Time spent in portion of stage',
							data: [0.25, 0.1, 0.4, 0.1, 0.15],
							backgroundColor: [
								'rgba(255, 99, 132, 0.2)',
								'rgba(54, 162, 235, 0.2)',
								'rgba(255, 206, 86, 0.2)',
								'rgba(75, 192, 192, 0.2)',
								"rgba(54, 162, 235, 0.2)"
							],
							borderColor: [
								'rgba(255,99,132,1)',
								'rgba(54, 162, 235, 1)',
								'rgba(255, 206, 86, 1)',
								'rgba(75, 192, 192, 1)',
								"rgb(54, 162, 235)"
							],
							borderWidth: 1
						}]
					},
					options: {
						scales: {
							xAxes: [{
								ticks: {
									beginAtZero: true
								}
							}],
							yAxes: [{
								ticks: {
									beginAtZero: true
								}
							}]
						}
					}
				});

				var ctx_6 = document.getElementById("myChart-6").getContext('2d');
				var myChart_6 = new Chart(ctx_6, {
					type: 'horizontalBar',
					data: {
						labels: ["Joy", "Sorrow", "Anger", "Surprise"],
						datasets: [{
							label: 'Expression Likelihood',
							data: [0.75, 0.05, 0.05, 0.15],
							backgroundColor: [
								'rgba(255, 99, 132, 0.2)',
								'rgba(54, 162, 235, 0.2)',
								'rgba(255, 206, 86, 0.2)',
								'rgba(75, 192, 192, 0.2)'
							],
							borderColor: [
								'rgba(255,99,132,1)',
								'rgba(54, 162, 235, 1)',
								'rgba(255, 206, 86, 1)',
								'rgba(75, 192, 192, 1)'
							],
							borderWidth: 1
						}]
					},
					options: {
						scales: {
							xAxes: [{
								ticks: {
									beginAtZero: true
								}
							}],
							yAxes: [{
								ticks: {
									beginAtZero: true
								}
							}]
						}
					}
				});

    var mySVG = $('svg').drawsvg({
        // callback: function() {
        //     $('#obama > g').css({fill: '#000000', transition: '0.5s'});
        // }
    });

    $('#btn-draw').on('click', function() {
        console.log('clicked');

        mySVG.drawsvg('animate');
        // $('#obama > g').css({fill: '#000000', transition: '2.0s'});


    });
};