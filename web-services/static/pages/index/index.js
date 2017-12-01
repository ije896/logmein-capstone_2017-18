var section_1_label_visible = false;
var section_1_text_visible = false;

// var section_2_image_visible = false;
var section_2_label_visible = false;
var section_2_text_visible = false;
var section_2_text_2_visible = false;

var section_3_label_visible = false;
var section_3_text_visible = false;
var section_3_text_2_visible = false;

var section_4_label_visible = false;
var section_4_text_visible = false;
var section_4_text_2_visible = false;

// $(document).ready(function() {
//
// });

window.onload = function() {
	$('#index-top-scene').fadeIn(500, function() {
		$('#index-top-scene-label').fadeIn(1000);
		$('#index-section-1').show();
		$('#index-section-2').show();
		$('#index-section-3').show();
		$('#index-section-4').show();

		var section_1_height =
			($('#index-section-1-label').show().height() +
				$('#section-1-text').show().height() +
				0.2 * $(window).height()).toString() + 'px';
		$('#index-section-1').show().css('height', section_1_height);
		$('#index-section-1-label').hide();
		$('#section-1-text').hide();

		var section_2_height =
			($('#index-section-2-label').show().height() +
				$('#section-2-text').show().height() +
				$('#section-2-text-2').show().height() +
				0.5 * $(window).height()).toString() + 'px';
		$('#index-section-2').show().css('height', section_2_height);

		$('#myChart').css('max-height', ($('#section-2-text').show().height()).toString() + 'px');
		$('#myChart').css('top', ($('#section-2-text').position().top + $('#myChart').height() / 2).toString() + 'px' );

		$('#section-2-text-2').css('top', ($('#section-2-text').position().top + $('#section-2-text').height() + 0.05 * $(window).height()).toString() + 'px');

		$('#myChart-2').css('max-height', ($('#section-2-text-2').show().height()).toString() + 'px');
		$('#myChart-2').css('top', ($('#section-2-text-2').position().top + $('#myChart-2').height() / 4).toString() + 'px' );

		$('#index-section-2-label').hide();
		$('#section-2-text').hide();
		$('#section-2-text-2').hide();

		var section_3_height =
			($('#index-section-3-label').show().height() +
				$('#section-3-text').show().height() +
				$('#section-3-text-2').show().height() +
				0.4 * $(window).height()).toString() + 'px';
		$('#index-section-3').show().css('height', section_3_height);

		$('#myChart-3').css('max-height', ($('#section-3-text').height()).toString() + 'px');
		$('#myChart-3').css('top', ($('#section-3-text').position().top + $('#myChart-3').height() / 6).toString() + 'px' );

		// console.log($('#section-3-text').position().top);
		// console.log($('#section-3-text').height());
		// console.log(0.05 * $(window).height());
		// console.log(($('#section-3-text').position().top + $('#section-3-text').height() + 0.05 * $(window).height()).toString() + 'px');
		$('#section-3-text-2').css('top', ($('#section-3-text').position().top + $('#section-3-text').height() + 0.1 * $(window).height()).toString() + 'px');

		$('#myChart-4').css('max-height', ($('#section-3-text-2').show().height()).toString() + 'px');
		$('#myChart-4').css('top', ($('#section-3-text-2').position().top + $('#myChart-4').height() / 5.5).toString() + 'px' );

		$('#index-section-3-label').hide();
		$('#section-3-text').hide();
		$('#section-3-text-2').hide();


		var section_4_height =
			($('#index-section-4-label').show().height() +
				$('#section-4-text').show().height() +
				$('#section-4-text-2').show().height() +
				0.5 * $(window).height()).toString() + 'px';
		$('#index-section-4').show().css('height', section_4_height);

		$('#myChart-5').css('max-height', ($('#section-4-text').height()).toString() + 'px');
		$('#myChart-5').css('top', ($('#section-4-text').position().top + $('#myChart-5').height() / 6).toString() + 'px' );

		// console.log($('#section-3-text').position().top);
		// console.log($('#section-3-text').height());
		// console.log(0.05 * $(window).height());
		// console.log(($('#section-3-text').position().top + $('#section-3-text').height() + 0.05 * $(window).height()).toString() + 'px');
		$('#section-4-text-2').css('top', ($('#section-4-text').position().top + $('#section-4-text').height() + 0.025 * $(window).height()).toString() + 'px');

		$('#myChart-6').css('max-height', ($('#section-4-text-2').show().height()).toString() + 'px');
		$('#myChart-6').css('top', ($('#section-4-text-2').position().top + $('#myChart-6').height() / 5.5).toString() + 'px' );

		$('#index-section-4-label').hide();
		$('#section-4-text').hide();
		$('#section-4-text-2').hide();

	});

	$('body').scroll(function() {

		// var bottomPos = $(window).scrollTop() + $(window).height();
		if (!section_1_label_visible) {
			if ($('#index-section-1-label').show().offset().top < $(window).height() - $('#index-section-1-label').height()) {
				$('#index-section-1-label').hide();
				$('#index-section-1-label').fadeIn(500);
				section_1_label_visible = true;

				// var label_height = $('#index-section-1-label').height().toString() + 'px';
				// var label_width = $('#index-section-1-label').width().toString() + 'px';
				//
				// $('#index-section-1-label > .animated-border-left').animate({height: label_height}, 1000);
				// $('#index-section-1-label > .animated-border-top').animate({width: label_width}, 1000);
				// $('#index-section-1-label > .animated-border-right').animate({height: label_height}, 1000);
				// $('#index-section-1-label > .animated-border-bottom').animate({width: label_width}, 1000);

				$('#index-section-1-label > .animated-border-left').animate({height: '100%'}, 1000);
				$('#index-section-1-label > .animated-border-top').animate({width: '100%'}, 1000);
				$('#index-section-1-label > .animated-border-right').animate({height: '100%'}, 1000);
				$('#index-section-1-label > .animated-border-bottom').animate({width: '100%'}, 1000);

			} else {
				$('#index-section-1-label').hide();
			}
		}

		if (!section_1_text_visible) {
			if ($('#section-1-text').show().offset().top < $(window).height() - $('#section-1-text').height() * 0.75) {
				$('#section-1-text').hide();
				$('#section-1-text').fadeIn({queue: false, duration: 500});
				// $('#section-1-text').animate({top: '15vh'}, 700);
				$('#section-1-p1').animate({left: 0}, 700);
				$('#section-1-p2').animate({right: 0}, 700);
				section_1_text_visible = true;
				// console.log('scrolled');
			} else {
				$('#section-1-text').hide();
			}
		}


		// if (!section_2_image_visible) {
		// 	if ($('#index-section-2').offset().top < $(window).height() - $('#index-section-2').height() * 0.6) {
		// 		// console.log('scrolled');
		// 		$('#index-section-2-image').fadeIn({queue: false, duration: 400}).animate({bottom: '0'}, 400);
		// 		section_2_image_visible = true;
		// 	} else {
        //
		// 	}
		// }

		if (!section_2_label_visible) {
			if ($('#index-section-2-label').show().offset().top < $(window).height() - $('#index-section-2-label').height()) {
				$('#index-section-2-label').hide();

				$('#index-section-2 > .animated-border-top').show().animate({width: '100%'}, 1000);

				$('#index-section-2-label').fadeIn(500);
				section_2_label_visible = true;

				$('#index-section-2-label > .animated-border-left').css('top', '0').css('bottom', 'unset').animate({height: '100%'}, 1000);
				$('#index-section-2-label > .animated-border-top').css('left', '0').css('right', 'unset').animate({width: '100%'}, 1000);
				$('#index-section-2-label > .animated-border-right').css('bottom', '0').css('top', 'unset').animate({height: '100%'}, 1000);
				$('#index-section-2-label > .animated-border-bottom').css('right', '0').css('left', 'unset').animate({width: '100%'}, 1000);


			} else {
				$('#index-section-2-label').hide();
			}
		}

		if (!section_2_text_visible) {
			if ($('#section-2-text').show().offset().top < $(window).height() - $('#section-2-text').height() * 0.75) {
				$('#section-2-text').hide();
				$('#section-2-text').fadeIn({queue: false, duration: 500});
				$('#section-2-text').animate({right: '6%'}, 700);
				section_2_text_visible = true;
				// console.log('scrolled');

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
			} else {
				$('#section-2-text').hide();
			}
		}

		if (!section_2_text_2_visible) {
			if ($('#section-2-text-2').show().offset().top < $(window).height() - $('#section-2-text-2').height() * 0.75) {
				$('#section-2-text-2').hide();
				$('#section-2-text-2').fadeIn({queue: false, duration: 500});
				$('#section-2-text-2').animate({left: '10%'}, 700);
				section_2_text_2_visible = true;
				// console.log('scrolled');

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

			} else {
				$('#section-2-text-2').hide();
			}
		}



		if (!section_3_label_visible) {
			if ($('#index-section-3-label').show().offset().top < $(window).height() - $('#index-section-3-label').height()) {
				$('#index-section-3-label').hide();

				$('#index-section-3 > .animated-border-top').show().css('left', '0').css('right', 'unset').animate({width: '100%'}, 1000);

				$('#index-section-3-label').fadeIn(500);
				section_3_label_visible = true;

				$('#index-section-3-label > .animated-border-left').animate({height: '100%'}, 1000);
				$('#index-section-3-label > .animated-border-top').animate({width: '100%'}, 1000);
				$('#index-section-3-label > .animated-border-right').animate({height: '100%'}, 1000);
				$('#index-section-3-label > .animated-border-bottom').animate({width: '100%'}, 1000);

			} else {
				$('#index-section-3-label').hide();
			}
		}

		if (!section_3_text_visible) {
			if ($('#section-3-text').show().offset().top < $(window).height() - $('#section-3-text').height() * 0.75) {
				$('#section-3-text').hide();
				$('#section-3-text').fadeIn({queue: false, duration: 500});
				$('#section-3-text').animate({left: '10%'}, 700);
				section_3_text_visible = true;
				// console.log('scrolled');

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
			} else {
				$('#section-3-text').hide();
			}
		}

		if (!section_3_text_2_visible) {
			if ($('#section-3-text-2').show().offset().top < $(window).height() - $('#section-3-text-2').height() * 0.75) {
				$('#section-3-text-2').hide();
				$('#section-3-text-2').fadeIn({queue: false, duration: 500});
				$('#section-3-text-2').animate({right: '6%'}, 700);
				section_3_text_2_visible = true;
				// console.log('scrolled');

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

			} else {
				$('#section-3-text-2').hide();
			}
		}


		if (!section_4_label_visible) {
			if ($('#index-section-4-label').show().offset().top < $(window).height() - $('#index-section-4-label').height()) {
				$('#index-section-4-label').hide();

				$('#index-section-4 > .animated-border-top').show().animate({width: '100%'}, 1000);

				$('#index-section-4-label').fadeIn(500);
				section_4_label_visible = true;

				$('#index-section-4-label > .animated-border-left').css('top', '0').css('bottom', 'unset').animate({height: '100%'}, 1000);
				$('#index-section-4-label > .animated-border-top').css('left', '0').css('right', 'unset').animate({width: '100%'}, 1000);
				$('#index-section-4-label > .animated-border-right').css('bottom', '0').css('top', 'unset').animate({height: '100%'}, 1000);
				$('#index-section-4-label > .animated-border-bottom').css('right', '0').css('left', 'unset').animate({width: '100%'}, 1000);


			} else {
				$('#index-section-4-label').hide();
			}
		}

		if (!section_4_text_visible) {
			if ($('#section-4-text').show().offset().top < $(window).height() - $('#section-4-text').height() * 0.75) {
				$('#section-4-text').hide();
				$('#section-4-text').fadeIn({queue: false, duration: 500});
				$('#section-4-text').animate({right: '6%'}, 700);
				section_4_text_visible = true;
				// console.log('scrolled');

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
			} else {
				$('#section-4-text').hide();
			}
		}

		if (!section_4_text_2_visible) {
			if ($('#section-4-text-2').show().offset().top < $(window).height() - $('#section-4-text-2').height() * 0.75) {
				$('#section-4-text-2').hide();
				$('#section-4-text-2').fadeIn({queue: false, duration: 500});
				$('#section-4-text-2').animate({left: '10%'}, 700);
				section_4_text_2_visible = true;
				// console.log('scrolled');

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

			} else {
				$('#section-4-text-2').hide();
			}
		}

	});

	// if ($('#myChart').show().offset().top < $('#myChart').height()) {

	// }
};

