
if (document.getElementById("vid1")) {
  videojs("vid1").ready(function() {

    var myPlayer = this;

    //Set initial time to 0
    var currentTime = 0;

    setInterval(function() {
      if (!myPlayer.paused()) {
        currentTime = myPlayer.currentTime();
      }
    }, 1000);

  });

  videojs("vid1", {"height":"auto",
"width":"auto"}).ready(function(){
    var myPlayer = this;    // Store the video object
    var aspectRatio = 4.5/8; // Make up an aspect ratio

    function resizeVideoJS(){
      // Get the parent element's actual width
      var width = document.getElementById(myPlayer.id()).parentElement.offsetWidth*.9;
      // Set width to fill parent element, Set height
      myPlayer.width(width).height( width * aspectRatio );
    }

    resizeVideoJS(); // Initialize the function
    window.onresize = resizeVideoJS; // Call the function on resize
  });

}

function validateForm() {
  var x = document.forms["myForm"]["title"].value;
  if (x == "" || x == null) {
    alert("Title must be filled out");
    return false;
  }
}

var _validFileExtensions = [".mp4", ".mkv"];    
function Validate(oForm) {
    var arrInputs = oForm.getElementsByTagName("input");
    for (var i = 0; i < arrInputs.length; i++) {
        var oInput = arrInputs[i];
        if (oInput.type == "file") {
            var sFileName = oInput.value;
            if (sFileName.length > 0) {
                var blnValid = false;
                for (var j = 0; j < _validFileExtensions.length; j++) {
                    var sCurExtension = _validFileExtensions[j];
                    if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
                        blnValid = true;
                        break;
                    }
                }
                
                if (!blnValid) {
                    alert("Sorry, " + sFileName + " is invalid, allowed extensions are: " + _validFileExtensions.join(", "));
                    return false;
                }
            }
        }
    }
  
    return true;
}

