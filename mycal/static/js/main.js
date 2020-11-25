console.log("loaded")
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let attendanceBoxes = document.querySelectorAll('.checks')
for (let box of attendanceBoxes){
    box.addEventListener('change', e => {
        console.log(e.target.checked)
        if (e.target.checked){ 
        let elem = e.target;
        let pk = elem.dataset.pk;
        let type = elem.name;
        let value = elem.checked;
        console.log(elem)
        fetch('update-pal/', {
            method: 'POST',
            credentials: 'same-origin',
            headers:{
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
                'X-CSRFToken': csrftoken,
        },
            body: JSON.stringify({'pk':pk, 'type':type}) //JavaScript object of data to POST
        })
        .then(response => {
              return response.json() //Convert response to JSON
        })
        .then(data => {
            console.log(data)
        //Perform actions with the response data from the view
        })
      
        }
    })
}



