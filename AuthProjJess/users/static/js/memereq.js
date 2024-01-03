function log(){
    alert("Log In Successful!");
  };
  function signup(){
    var response = confirm('Please confirm Sign Up...');
    if (confirm == false){
      preventDefault();
    }
  };
  function feature(){
    alert("This feature is on the making...");
  };
  
    
    let name = document.getElementById('fname');
    let Email = document.getElementById('Email');
    let phone = document.getElementById('phone');
    let region = document.getElementById('region');
    let code = document.getElementById('code');
    let country = document.getElementById("country");
    let city = document.getElementById("city");
    let countryErrorBlock = document.getElementById("country-error");
  form.addEventListener('submit', e => {
      e.preventDefault();
  
      validateInputs();
  });
  
  const setError = (element, message) => {
      const inputControl = element.parentElement;
      const errorDisplay = inputControl.querySelector('.error');
  
      errorDisplay.innerText = message;
      inputControl.classList.add('error');
      inputControl.classList.remove('success')
  }
  
  const setSuccess = element => {
      const inputControl = element.parentElement;
      const errorDisplay = inputControl.querySelectorAll('.error');
  
      errorDisplay.innerText = '';
      inputControl.classList.add('success');
      inputControl.classList.remove('error');
  }

  const error = (element, message) => {
      const column = element.nextElementSibling;
      // const errorDisplay = column.querySelector('.error');
  
      column.innerText = message;
      column.classList.add('error');
      column.classList.remove('success');
  }
  const success = element => {
    const column = element.nextElementSibling;
    column.innerText = "";
    column.classList.add("success");
    column.classList.remove("error");
  }
  const isValidEmail = Email => {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(String(Email).toLowerCase());
  }
  
  const validateInputs = () => {
      
      const fnameValue = fname.value.trim();
      const EmailValue = Email.value.trim();
      const phoneValue = phone.value.trim();
      const regionValue = region.value.trim();
      const codeValue = code.value.trim();
      const countryValue = country.options[country.selectedIndex].text.trim();
      const cityValue = city.value.trim();
      console.log(countryValue);

        if(fnameValue === '') {
            setError(fname, 'Full name is required');
        }else{
            setSuccess(fname);
        }

        if(EmailValue === '') {
            setError(Email, 'Email is required');
        } else if (!isValidEmail(EmailValue)) {
            setError(Email, 'Provide a valid email address');
        } else {
            setSuccess(Email);
        }

        if(phoneValue === '') {
            setError(phone, 'Phone number is required');
        } else if (phoneValue.length < 11 ) {
            setError(phone, 'Phone number must be at 11 characters.');
        } else {
            setSuccess(phone);
        }

        if(countryValue === "Country"){
            countryError(countryErrorBlock, "Please select a Country");
        } else {
            countrySuccess(countryErrorBlock);
        }    

        if(cityValue === ""){
            error(city, "City is Required");
        } else {
            success(city);
        }

        if(regionValue === "") {
            error(region, 'Region is required');
        }else{
            success(region);    
        }

        if(codeValue === '') {
            error(code, 'Postal Code is required');
        } else if (codeValue.length < 4 ) {
            error(code, 'Postal code must be at least 4 characters.');
        } else {
            success(code);
        }
    };
  
// Special Methods for Country
countryError = (element, message) => {
    element.innerText = message;
    element.classList.add("error");
    element.classList.remove("success"); // No need para nako. wa gihapoy makita
}
countrySuccess = element => {
    element.innerText = "";
    element.classList.add("success");
    element.classList.remove("error"); // No need para nako. wa gihapoy makita
}

// To Dos: Street Address


// Changes
// Variables: added country, city, countryErrorBlock Lines: 20-22 & 73-75

// changed error and success functions
// use nextElementSibling instead of querySelector Lines: 48 & 56

// specific methods for country when error/success Lines: 127 and 132

// css grid

// html: 
// select => hidden -> selected