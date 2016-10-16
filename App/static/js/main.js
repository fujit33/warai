var cnt=0;

var q = document.getElementsByClassName("question");
var f = document.getElementsByClassName("form");

for (var i = 1; i < q.length; i++) {
    q[i].style.display = "none";
}
for (var i = 1; i < f.length; i++) {
    f[i].style.display = "none";
}


document.getElementById("finish").style.display = "none";
document.getElementById("inputerror").style.display = "none";

document.getElementById("next").addEventListener("click", function() {
    if(cnt<30){
        if(!(document.getElementsByTagName("input")[1+6*cnt+0].checked)&& !(document.getElementsByTagName("input")[1+6*cnt+1].checked)&&
        !(document.getElementsByTagName("input")[1+6*cnt+2].checked)&& !(document.getElementsByTagName("input")[1+6*cnt+3].checked)&&
        !(document.getElementsByTagName("input")[1+6*cnt+4].checked) &&!(document.getElementsByTagName("input")[1+6*cnt+5].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}
    var q = document.getElementsByClassName("question");
    var f = document.getElementsByClassName("form");

    q[cnt].style.display = "none";
    f[cnt].style.display = "none";

    cnt += 1;

    if (cnt<36){
        q[cnt].style.display = "block";
        f[cnt].style.display = "block";
        if(cnt==35){
            f[cnt+1].style.display = "block";
        }
    }else{
        document.getElementById("finish").style.display = "block";
        document.getElementById("next").style.display = "none";
    }
    document.getElementById("inputerror").style.display = "none";
});
