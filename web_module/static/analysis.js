window.onload = function() {


var marksCanvas = document.getElementById("marksChart");

var tones = window.watson_data['document_tone']['tone_categories'][0]['tones'];


	var marksData = {
	  labels: ["Anger", "Disgust", "Fear", "Joy", "Sadness"],
	  datasets: [{
		label: "Emotional Tone",
		backgroundColor: "rgba(200,0,0,0.2)",
		data: [tones[0]['score'], tones[1]['score'], tones[2]['score'], tones[3]['score'], tones[4]['score']]
	  }]
	};

	var radarChart = new Chart(marksCanvas, {
	  type: 'radar',


	  data: marksData
	});

};