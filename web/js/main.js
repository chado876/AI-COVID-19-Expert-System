// document.getElementById("diagnose-btn").addEventListener("click", ()=>{eel.get_random_name()}, false);
// document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
// document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
// document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);


eel.expose(print_symptoms);
function print_symptoms(symptoms) {
  console.log(symptoms);
}

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

function switchToDiagnosisScreen() {
  document.getElementById("main-menu").style.display="none";
  eel.get_symptoms()
  document.getElementById("page-1").style.display="inline";
}

function switchToDiagnosisScreen2(){
  document.getElementById("page-1").style.display="none";
  document.getElementById("page-2").style.display="inline";
}

function switchToMainScreen(){
  document.getElementById("main-menu").style.display="inline";
  document.getElementById("page-1").style.display="none";
}
