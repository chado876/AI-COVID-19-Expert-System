// document.getElementById("diagnose-btn").addEventListener("click", ()=>{eel.get_random_name()}, false);
// document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
// document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
// document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);


eel.expose(add_symptom_checkboxes);
function add_symptom_checkboxes(symptoms) {
  createCheckboxes(symptoms)
  console.log(symptoms);
}

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

function switchToDiagnosisScreen() {
  document.getElementById("main-menu").style.display="none";
  document.getElementById("page-1").style.display="inline";
}

function switchToDiagnosisScreen2(){
  document.getElementById("page-1").style.display="none";
  document.getElementById("page-2").style.display="inline";
  eel.get_symptoms()
}

function switchToMainScreen(){
  document.getElementById("main-menu").style.display="inline";
  document.getElementById("page-1").style.display="none";
}

function createCheckboxes(symptoms){
  for (var i = 0; i < symptoms.length; i++){
    console.log(symptoms[i]);

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = symptoms[i];
    checkbox.value = symptoms[i];
   
    var label = document.createElement('label')
    label.htmlFor = symptoms[i];
    label.appendChild(document.createTextNode(symptoms[i]));
    
    var br = document.createElement('br');
   
    var container = document.createElement('container');
    container.appendChild(checkbox);
    container.appendChild(label);
    container.appendChild(br);
    document.getElementById('symptom-checkboxes').appendChild(container);
  }

}