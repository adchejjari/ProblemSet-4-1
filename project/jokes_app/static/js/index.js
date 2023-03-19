const MAX_NAME_LENGH = 20;
const MIN_NAME_LENGH = 1;

const MAX_CONTENT_LENGH = 120;
const MIN_CONTENT_LENGH = 10;


function checkUserInput(){
    let name = document.getElementById('author').value;
    let content = document.getElementById('content').value;
    if (name.length > MAX_NAME_LENGH){
        alert("The name must not exceed 20 characters ");
        return;
    }

    if (name.length < MIN_NAME_LENGH){
        alert("The name field is empty");
        return;
    }

    if (content.length > MAX_CONTENT_LENGH){
        alert("The content must not exceed 120 characters ");
        return;
    }

    if (content.length < MIN_CONTENT_LENGH){
        alert("The content must exceed 10 characters ");
        return;
    }
    
    document.getElementById("data-form").submit(); 

}