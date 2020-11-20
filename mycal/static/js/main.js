console.log("loaded")

// let attendanceBoxes = document.querySelectorAll('checkbox')
// console.log(attendanceBoxes)


function getValue() {
    var checks = document.getElementsByClassName('checks');
    var str = ''

    for (i = 0; i < 3; i++) {
        if (checks[i].checked == true) {
            str += checks[i].value;
            console.log(str)
        }
    
      
    }
    console.log(str)
   
}

