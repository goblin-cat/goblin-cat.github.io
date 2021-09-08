// set a variable that is "css style" that is stored in idk local session? cookie?
// when any page is loaded, swap out template based on this variable

if (localStorage.style == "light" ){
	changeStyleSheet("/portfolio/lightStyle.css");
} else if (localStorage.style == "dark" ){
	changeStyleSheet("/portfolio/darkStyle.css");
}else if (localStorage.style == "fun" ){
	changeStyleSheet("/portfolio/funStyle.css");
} else {
	// by default, light
	changeStyleSheet("/portfolio/lightStyle.css");
}

function changeStyleSheet(sheet){
	// http://www.developphp.com/video/JavaScript/Change-Style-Sheet-Using-Tutorial-CSS-Swap-Stylesheet
	document.getElementById('pagestyle').setAttribute('href', sheet);
}

function changeToLight(){
	localStorage.style = "light";
	location.reload();
}

function changeToDark(){
	localStorage.style = "dark";
	location.reload();
}

function changeToFun(){
	localStorage.style = "fun";
	location.reload();
}