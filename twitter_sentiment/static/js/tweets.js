var current_data;

function sentiment_to_color(sentiment){
	if(sentiment == 'positive') return 'green';
	else if(sentiment == 'negative') return 'red';
	else return 'grey';
}

function load_tweets(entered_text){
	$.ajax({
	    url: '/twitter/tweets/',
	    type: 'post',
	    data: {'query': entered_text, 'retweets_only': 'false', 'with_sentiment': 'true'},
	    dataType: 'json',
	    success: function(data) {
	    	current_data = data['data'];
	        var tweets = data['data'];
	        var container = $('#tweets');
	        if(tweets.length==0){
                	var contents="<div class='well' style='margin-top:30px;width:100%;font-weight:20px;'>Sorry No Tweets Found !!</div>";
                        }
            else{            
		        	var contents = "<div><table  style='width:500px;' class='table'><thead><tr><th>UserName</th><th>Text</th><th>Sentiment</th></tr></thead>";
		        	for(i = 0; i < tweets.length; i++){
		        	contents += "<tbody><tr class='  searchable'><td><i class='fa fa-user'></i>&nbsp;&nbsp;" + tweets[i].user + "</td><td>" + tweets[i].text + "</td><td><span style='color: " + sentiment_to_color(tweets[i].sentiment) + "'>" + tweets[i].sentiment + "</span></td></tr></tbody";
		        	}

		        	contents+= "</table></div>";

		        	container.html(contents);
		        	$('#search').val(entered_text);
		        	$('#loading').html("<p class='tweets_loading'>" 
		        						+ data['count'] 
		        						+ " Tweets loaded about&nbsp;&nbsp;\
		        						<span style='text-decoration:underline;\
		        						color:orange;'>"
		        						+ entered_text + "</span></p>\
		        						<div class='col-md-3 input-group \
		        						form-group'>\
		        						<span class='input-group-addon'>\
		        						<i class='fa fa-bar-chart'></i>\
		        						</span><input class='btn btn-primary pull-right' type='button' data-toggle='modal' data-target='#plot-graph' class='filter form-control'\
		        						value='Graphical Analysis'></div>");
		        	$('#plot_graph').html();
				}	    
	    	}

		});
	}

function get_csv(json){
	var fields = Object.keys(json[0]);
	var csv = json.map(function(row){
	  return fields.map(function(fieldName){
	    return JSON.stringify(row[fieldName] || '');
	  });
	});
	csv.unshift(fields);
	return csv.join('\r\n');
}

function download(filename, text) {
  var element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  element.style.display = 'none';
  document.body.appendChild(element);

  element.click();

  document.body.removeChild(element);
}


$('#input-search').click(function(){
	load_tweets($('#search').val());
});

$('#getcsv').click(function(){
	download('data.csv', get_csv(current_data));
});


$(document).ready(function(){
	//$('#loading').addClass('show');
	load_tweets('Machine Learning');
});