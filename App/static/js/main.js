var cnt=0;

var q = document.getElementsByClassName("question");
var f = document.getElementsByClassName("form");
var inp = document.getElementsByTagName("input");
var hp = document.getElementById("hyouka_p");


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
        if(!(inp[1+6*cnt+0].checked)&& !(inp[1+6*cnt+1].checked)&&
        !(inp[1+6*cnt+2].checked)&& !(inp[1+6*cnt+3].checked)&&
        !(inp[1+6*cnt+4].checked) &&!(inp[1+6*cnt+5].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==31){
        if(!(inp[183].checked)&& !(inp[184].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==32){
        if(!(inp[185].checked)&& !(inp[186].checked)&& !(inp[187].checked)&& !(inp[188].checked)&& !(inp[189].checked) && !(inp[190].checked) && !(inp[191].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==34){
        if( !(inp[192].checked)&& !(inp[193].checked)&& !(inp[194].checked) && !(inp[195].checked) && !(inp[196].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==35){
        if(!(inp[197].checked)&& !(inp[198].checked)&& !(inp[199].checked)&& !(inp[200].checked) && !(inp[201].checked) && !(inp[202].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==36){
        if(!(inp[203].checked)&& !(inp[204].checked) && !(inp[205].checked) && !(inp[206].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==37){
        if(!(inp[207].checked)&& !(inp[208].checked)&& !(inp[209].checked) && !(inp[210].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==41){
        if(!(inp[234].checked)&& !(inp[235].checked) && !(inp[236].checked) && !(inp[237].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}else if(cnt==42){
        if(!(inp[238].checked)&& !(inp[239].checked) && !(inp[240].checked) && !(inp[241].checked)){
            document.getElementById("inputerror").style.display = "block";
            return;
    }}


    var q = document.getElementsByClassName("question");
    var f = document.getElementsByClassName("form");

    q[cnt].style.display = "none";
    f[cnt].style.display = "none";

    cnt += 1;

    if (cnt<43){
        q[cnt].style.display = "block";
        f[cnt].style.display = "block";
    }else{

        q[43].style.display = "block";
        f[43].style.display = "block";
        document.getElementById("finish").style.display = "block";
        document.getElementById("next").style.display = "none";
    }
    document.getElementById("inputerror").style.display = "none";
});
