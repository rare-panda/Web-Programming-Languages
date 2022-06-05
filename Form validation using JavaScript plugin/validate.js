window.onload = function(){

    //there will be one span element for each input field
    // when the page is loaded, we create them and append them to corresponding input element 
	// they are initially empty and hidden

	var email = document.getElementById("email");
    var span1 = document.createElement("span");
	span1.style.display = "none"; //hide the span element
    email.parentNode.appendChild(span1);

    email.onfocus = function(){
        email.className = "form-control";
    	span1.innerHTML = "Enter email in the format: abc@def.xyz";
        span1.style.display = "inline";
        span1.className = "emailclass";
    }

    email.onblur = function(){
        span1.style.display = "none";
    }

    var pwd = document.getElementById("pwd");
    var span2 = document.createElement("span");
    span2.style.display = "none"; //hide the span element
    pwd.parentNode.appendChild(span2);

    pwd.onfocus = function(){
        pwd.className = "form-control";
        span2.innerHTML = "Password should include at least six characters";
        span2.style.display = "inline";
        span2.className = "pwdclass";
    }

    pwd.onblur = function(){
        span2.style.display = "none";
    }

    var cnfpwd = document.getElementById("confirm");
    var span3 = document.createElement("span");
    span3.style.display = "none"; //hide the span element
    cnfpwd.parentNode.appendChild(span3);

    cnfpwd.onfocus = function(){
        cnfpwd.className = "form-control";
        span3.innerHTML = "Should be the same as password entered above";
        span3.style.display = "inline";
        span3.className = "confirmclass";
    }
    
    cnfpwd.onblur = function(){
        span3.style.display = "none";
    }

    
    var form = document.getElementById("myForm");
    form.onsubmit = function(e){
        var mailformat = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        if(!mailformat.test(email.value)){
            span1.innerHTML = "Invalid Email";
            span1.style.display = "block";
            span1.className = "error";
            email.className = 'error';
            e.preventDefault();
        }

    	if(pwd.value.length < 6){
            span2.innerHTML = "Password not valid.";
            span2.style.display = "block";
            span2.className = "error";
            pwd.className = 'error';
            span3.style.display = "block";
            span3.innerHTML = "Password not valid."
            span3.className="error";
            cnfpwd.className = 'error';
            e.preventDefault();
        }
    
        if(pwd.value != cnfpwd.value){
            span3.innerHTML = "Both the passwords doesn't match";
            span3.style.display = "block";
            span3.className = "error";
            cnfpwd.className = 'error';
            span2.style.display = "block";
            span2.className = "error";
            pwd.className = 'error';
            e.preventDefault();
    
        }


    	//e.preventDefault();

    }


}


