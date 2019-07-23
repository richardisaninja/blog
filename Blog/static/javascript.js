var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
showDivs(slideIndex += n);
}

function currentDiv(n) {
showDivs(slideIndex = n);
}

function showDivs(n) {
var i;
var x = document.getElementsByClassName("mySlides");
var dots = document.getElementsByClassName("demo");
if (n > x.length) {slideIndex = 1}
if (n < 1) {slideIndex = x.length}
for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
}

x[slideIndex-1].style.display = "block";  

}

function display_c(){
var refresh=1000; // Refresh rate in milli seconds
mytime=setTimeout('display_ct()',refresh)
}

function display_ct() {
var x = new Date()
document.getElementById('ct').innerHTML = x;
display_c();
}

$(document).ready(function(){
    var amount = $('.col-4').length;
    $('.amount').html("Total number of posts submitted: "+ amount);
    $('.comment-content').hide();
},

$('.comments').click(function(){

$(".comment-content").toggle();
})
)


//FORM validations
function validateForm() {
    var x = document.forms["myForm"]["title"].value;
    var y = document.forms["myForm"]["content"].value;
    if (x == "" || x.length<5) {
      alert("Title must be more than 5 characters");
      return false;
    }
    if (y == "" || y.length<5) {
        alert("Content must be more than 5 characters");
        return false;
      }
}

function validateFormC() {
   
    var y = document.forms["myForm"]["content"].value;

    
    if (y == "" || y.length<5) {
        alert("Content must be more than 5 characters");
        return false;
      }
}
//end section

