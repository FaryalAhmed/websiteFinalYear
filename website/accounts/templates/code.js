var check = function() {
  if (document.getElementById('inputPassword1').value ==
    document.getElementById('inputPassword2').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'Matched!';
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'Not matched :(';
  }
}

var check1 = function() {
  var letters = /^[A-Za-z]+$/;
  var x = document.forms["myForm"]["firstname"].value;
  if (x == "" || x == null) {
    alert("First name must be filled out");
    return false;
  }
  if (x.length < 3) {
    alert("First name is less than 3");
    return false;
  }
  if(!(!/[^a-zA-Z]/.test(x))){
    alert('Please input alphabet characters only in First name');
    return false;
  }
}

var check2 = function() {
  var letters = /^[A-Za-z]+$/;
  var x = document.forms["myForm"]["lastname"].value;
  if (x == "" || x == null) {
    alert("Last name must be filled out");
    return false;
  }
  if (x.length < 3) {
    alert("Last name is less than 3");
    return false;
  }
  if(!(!/[^a-zA-Z]/.test(x))){
    alert('Please input alphabet characters only in last name');
    return false;
  }
}

var check3 = function() {
  var x = document.forms["myForm"]["username"].value;
  if (x == "" || x == null) {
    alert("Username must be filled out");
    return false;
  }
}

var check4 = function() {
  var x = document.forms["myForm"]["contact_no"].value;
  if (x == "" || x == null) {
    alert("numbr must be filled out");
    return false;
  }
}

function ValidateEmail(inputText){
  var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  if(!inputText.value.match(mailformat)){
    alert("You have entered an invalid email address!");
    document.myForm.email.focus();
    return false;
  }
}
   ////////////////////////////
