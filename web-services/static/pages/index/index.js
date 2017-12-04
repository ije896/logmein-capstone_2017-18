var section_1_label_visible = false;
var section_1_text_visible = false;

// var section_2_image_visible = false;
var section_2_label_visible = false;
var section_2_text_visible = false;

var section_3_label_visible = false;
var section_3_text_visible = false;

var section_4_label_visible = false;
var section_4_text_visible = false;

var section_5_label_visible = false;

// $(document).ready(function() {
//
// });

window.onload = function() {
	var obama_svg = $('#obama').drawsvg({});
	var mlk_svg = $('#mlk').drawsvg({});
	var lincoln_svg = $('#lincoln').drawsvg({});

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
				0.5 * $(window).height()).toString() + 'px';
		$('#index-section-2').show().css('height', section_2_height);

		$('#index-section-2-label').hide();
		$('#section-2-text').hide();

		var section_3_height =
			($('#index-section-3-label').show().height() +
				$('#section-3-text').show().height() +
				0.4 * $(window).height()).toString() + 'px';
		$('#index-section-3').show().css('height', section_3_height);

		$('#index-section-3-label').hide();
		$('#section-3-text').hide();


		var section_4_height =
			($('#index-section-4-label').show().height() +
				$('#section-4-text').show().height() +
				0.5 * $(window).height()).toString() + 'px';
		$('#index-section-4').show().css('height', section_4_height);

		$('#index-section-4-label').hide();
		$('#section-4-text').hide();

		var section_5_height =
			($('#index-section-5-label').show().height() +
				0.5 * $(window).height()).toString() + 'px';
		$('#index-section-5').show().css('height', section_5_height);

		$('#index-section-5-label').hide();

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
			if ($('#index-section-2-label').show().offset().top < $(window).height() - $('#index-section-2-label').height() * 0.9) {
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
				$('#section-2-text').animate({right: '12%'}, 700);
				section_2_text_visible = true;
				// console.log('scrolled');


				obama_svg.drawsvg('animate');
        		$('#obama > g').css({fill: '#000000', transition: '2.0s'});

			} else {
				$('#section-2-text').hide();
			}
		}




		if (!section_3_label_visible) {
			if ($('#index-section-3-label').show().offset().top < $(window).height() - $('#index-section-3-label').height() * 0.9) {
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
				$('#section-3-text').animate({left: '15%'}, 700);
				section_3_text_visible = true;
				// console.log('scrolled');

				// mlk_svg.drawsvg('animate');
        		$('#mlk > g').css({fill: '#000000', transition: '2.0s'});

			} else {
				$('#section-3-text').hide();
			}
		}


		if (!section_4_label_visible) {
			if ($('#index-section-4-label').show().offset().top < $(window).height() - $('#index-section-4-label').height() * 0.8) {
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
				$('#section-4-text').animate({right: '12%'}, 700);
				section_4_text_visible = true;
				// console.log('scrolled');

				// lincoln_svg.drawsvg('animate');
        		// $('#mlk > g').css({fill: '#000000', transition: '2.0s'});
				$('#path2490').css({fill: '#9d9d9d', transition: '0.75s'});
				$('#path2488').css({fill: '#5d5d5d', transition: '0.5s'});
				$('#path2486').css({fill: '#2f2f2f', transition: '1.0s'});
				$('#path2484').css({fill: '#0d0d0d', transition: '0.25s'});

			} else {
				$('#section-4-text').hide();
			}
		}

		if (!section_5_label_visible) {
			if ($('#index-section-5-label').show().offset().top < $(window).height() - $('#index-section-5-label').height() * 0.9) {
				$('#index-section-5-label').hide();

				$('#index-section-5 > .animated-border-top').show().css('left', '0').css('right', 'unset').animate({width: '100%'}, 1000);

				$('#index-section-5-label').fadeIn(500);
				$('#upload-button').fadeIn(500);
				section_5_label_visible = true;

				$('#index-section-5-label > .animated-border-left').animate({height: '100%'}, 1000);
				$('#index-section-5-label > .animated-border-top').animate({width: '100%'}, 1000);
				$('#index-section-5-label > .animated-border-right').animate({height: '100%'}, 1000);
				$('#index-section-5-label > .animated-border-bottom').animate({width: '100%'}, 1000);



			} else {
				$('#index-section-5-label').hide();
			}
		}

	});


	// $('#upload-button').on('mouseenter', function() {
	// 	// $('#upload-button').css({border: 'black', transition: '1.0s'});
	// 	console.log('yep');
	// });

	$('#upload-button').on('click', function() {
		// console.log('clicked');
		$('.popup').fadeIn(600);
	});

	$('#submit-fp').on('click', function() {
		// console.log('click2');

		$('.popup > .popup-in').fadeOut(500, function() {

			var image = new Image();
			image.src ='/static/pages/index/loading_spinner.gif';
			$('.loading-spinner').attr('src',image.src);
			$('.loading-spinner').fadeIn(500);
		});

		setTimeout(function() {
			console.log('done waiting');
			window.location.href = 'http://127.0.0.1:5000/results';
		}, 2500);



	});


	// if ($('#myChart').show().offset().top < $('#myChart').height()) {

	// }
};
