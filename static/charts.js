function drawChart() {
    var header = [['Position', 'SVM1', 'SVM2']];

    var options = {
	title: 'AAPPred B-cell epitope prediction',
	hAxis: {
	    viewWindowMode: "explicit",
	    viewWindow: {
	    },
	    gridlines: {
		count: bigstep/10,
	    }
	},

	vAxis: {
	    minValue: -3,
	    maxValue: 3,
	    ticks: [-3, -2, -1, 0, 1, 2, 3],
	},
	chartArea: {
	    left: 30,
	    top: 20,
	    width: 800,
	    height: 300
	},
	legend: {
	    position: "bottom",
	},
	series: {
	    0: {
		color: "#A00000"
	    },
	    1: {
		color: "#00A000"
	    }
	},
	focusTarget: "category"
    };

    var plots = document.getElementById("plots")
    for (var i = 0; i < rawData.length; i += bigstep) {
	var data = google.visualization.arrayToDataTable(header.concat(rawData.slice(i, i + bigstep)));
	var mn = rawData[i][0];
	options.hAxis.viewWindow.min=mn;
	options.hAxis.viewWindow.max=mn + bigstep;
	var div = newDiv()
	plots.appendChild(div);
	var chart = new google.visualization.LineChart(div);
	chart.draw(data, options);
	plots.appendChild(newOpen(chart.getImageURI()));
	options.title = null;
    }
}

function newDiv() {
    var div = document.createElement('div');
    div.style.width = "860px";
    div.style.height = "360px";
    return div;
}

function newOpen(url) {
    var a = document.createElement('a');
    a.href = url;
    a.innerHTML = "[open]";
    var div = document.createElement('div');
    div.className = "open";
    div.appendChild(a);
    return div;
}
