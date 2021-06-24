
function scbybutton(n){
    var i=0;
    var slides=document.getElementsByClassName("slide");
    for(i=0;i<slides.length;i++){
        slides[i].style.display="none";
    }
slides[n-1].style.display="block";
var buttonsl=document.getElementsByClassName("slbutton");
for(i=0;i<buttonsl.length;i++){
    buttonsl[i].className=buttonsl[i].className.replace("active","");
}
buttonsl[n-1].className +=" active";
k=n;

}
var k=0;

function autoslideshow(){
    var j=0;
    var y=document.getElementsByClassName("slide");
    for(j=0;j<y.length;j++){
        y[j].style.display="none";
    }
    k++;
    if (k > y.length) {k = 1}    

y[k-1].style.display="block";
var getbutton =document.getElementsByClassName("slbutton");
for(var p=0;p<getbutton.length;p++){
    getbutton[p].className=getbutton[p].className.replace("active","");
}

getbutton[k-1].className +=" active";
setTimeout(autoslideshow,4000);
}