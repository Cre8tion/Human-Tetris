//var timeleft = 10;
//var i = 0;

//var timer = setInterval(function() {

  
  // Display the result in the element with id="demo"
//  document.getElementById("demo").style.color = "white"
//  document.getElementById("demo").innerHTML = timeleft + "s ";
//  timeleft--; 
//  if (timeleft == 0) {
//     timeleft = 5
//     }

// }, 1000);

var i = 0;
var intervalId;

function startTimer(duration, display) {
  timeleft = duration;
  intervalId = setInterval(function(){

  if (timeleft == 0 & (i % 2 == 0) & (i != 0)) {
     timeleft = 10;
     i = i + 1;
     }
  else if (timeleft == 0){
  	timeleft = 5;
  	i = i + 1;
  }
  document.getElementById("demo").style.color = "white";
  document.getElementById("demo").innerHTML = timeleft + "s ";  
  timeleft--; 
  }, 1000);
}

function resetTimer() {
  clearInterval(intervalId);
}

startTimer(5)
