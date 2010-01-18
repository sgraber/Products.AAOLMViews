// javascript timeline from the SIMILE/Timeline widget project: http://simile.mit.edu/timeline/
// below code customized from: http://simile.mit.edu/timeline/docs/create-timelines.html
// api docs: http://simile.mit.edu/timeline/docs/
// new project home on google code: http://code.google.com/p/simile-widgets/ 

var tl;

function onLoad() {
  var eventSource = new Timeline.DefaultEventSource();
  
  // make the info bubble bigger than default
  var theme = Timeline.ClassicTheme.create();
  theme.event.bubble.width = 250;
  theme.event.bubble.height = 200;

  // setup dates on the timeline
  var date = new Date();
  var months = new Array(12);
  months[0]="Jan";
  months[1]="Feb";
  months[2]="Mar";
  months[3]="Apr";
  months[4]="May";
  months[5]="Jun";
  months[6]="Jul";
  months[7]="Aug";
  months[8]="Sep";
  months[9]="Oct";
  months[10]="Nov";
  months[11]="Dec";
  
  var month = months[date.getMonth()];
  var day = date.getDate();
  var year = date.getFullYear();
  var dateToday = month + " " + day + " " + year + " 00:00:00 GMT";  // today's date. used for marking past events on the timeline.
  var dateBegin = "Jan 01 1900 00:00:00 GMT";  // when we will start marking things on the timeline as 'past'. will be colored differently.
  var timeOffset = -5;  // offset from GMT
  
  // get the month three months from today. used for offsetting the timeline a bit to show more upcoming dates than past dates.
  var m = date.getMonth() + 1;
  if (m > 11){
  	m = m - 11;
  }
  var dateOffset = months[m] + " " + day + " " + year + " 00:00:00 GMT";
  
  var bandInfos = [
    // create the top band that displays months on the timeline
    // may want to do something here w/ the golden ratio: 1:1.61803399 (61.8%, 38.2%)
    Timeline.createBandInfo({
        eventSource:    eventSource,
        date:			dateOffset,
        width:          "75%",  // total widths from combined createBandInfo must not exceed 100%
        intervalUnit:   Timeline.DateTime.MONTH, 
        timeZone:		timeOffset,
        intervalPixels: 150, 
        theme:			theme
    }),
    // create the bottom band that displays years on the timeline
    Timeline.createBandInfo({
        showEventText:  false,
		trackHeight:    0.5,
		trackGap:       0.2,
        eventSource:    eventSource,
        date:			dateOffset,
        width:          "25%",  // total widths from combined createBandInfo must not exceed 100%
        intervalUnit:   Timeline.DateTime.YEAR,
        timeZone:		timeOffset,
        intervalPixels: 200,
        theme:			theme
    })
  ];
  bandInfos[1].syncWith = 0;  		// make the bottom and top bands sync with one another
	  bandInfos[1].highlight = true; 	// make the bottom band have a highlighted section that spans the shown upper section
	  bandInfos[1].decorators = [  		// color the section of the bottom band timeline differently for past events
        new Timeline.SpanHighlightDecorator({
            startDate:  dateBegin,
            endDate:    dateToday,
            startLabel: "",
            endLabel:   "",
            color:      "#dedfe8",
            opacity:    40,
            theme:      theme
        })
  ];
	  bandInfos[0].decorators = [		// color the section of the top band timeline differently for past events
        new Timeline.SpanHighlightDecorator({
            startDate:  dateBegin,
            endDate:    dateToday,
            startLabel: "",
            endLabel:   "",
            color:      "#dedfe8",
            opacity:    40,
            theme:      theme
        })
  ];
	  
  tl = Timeline.create(document.getElementById("my-timeline"), bandInfos, Timeline.HORIZONTAL);  // find id="my-timeline" and replace it w/ our javascript timeline
  Timeline.loadXML("example1.xml", function(xml, url) { eventSource.loadXML(xml, url); });  // load the timeline data from our xml file

}

var resizeTimerID = null;
function onResize() {
    if (resizeTimerID == null) {
        resizeTimerID = window.setTimeout(function() {
            resizeTimerID = null;
            tl.layout();
        }, 500);
    }
}