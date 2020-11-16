let form = document.querySelector("form");

form.addEventListener("submit", function(event){
    event.preventDefault();

    let name = document.getElementById("name");
    let caseNumber = document.getElementById("case-number");

        console.log("valid");
        
        caseNumber.parentElement.classList.add("input-valid");
    
    }else{
        console.log("invalid");

        caseNumber.parentElement.classList.add("input-invalid");