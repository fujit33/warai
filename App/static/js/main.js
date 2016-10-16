var cnt=0;

var x = document.getElementsByClassName("question");
var y = document.getElementsByClassName("form");

for (var i = 1; i < x.length; i++) {
    x[i].style.display = "none";
    y[i].style.display = "none";
}
document.getElementById("finish").style.display = "none";

document.getElementById("next").addEventListener("click", function() {
    var x = document.getElementsByClassName("question");
    var y = document.getElementsByClassName("form");

    x[cnt].style.display = "none";
    y[cnt].style.display = "none";
    cnt += 1;

    if (cnt<36){
        x[cnt].style.display = "block";
        y[cnt].style.display = "block";
    }else{
        document.getElementById("finish").style.display = "block";
        document.getElementById("next").style.display = "none";
    }
});