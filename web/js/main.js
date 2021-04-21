import * as symptoms from './modules/symptoms.js';

document.getElementById('diagnose-btn').addEventListener('click', () => {
  navigate('main-menu', 'page-0')
}, false);
document.getElementById('add-btn').addEventListener('click', () => {
  navigate('main-menu', 'add-symptom')
}, false);
document.getElementById('next-btn-0').addEventListener('click', () => 
{checkIfValid('page-0')}, false);
document.getElementById('del-btn').addEventListener('click', () => {
  navigate('main-menu', 'delete-symptoms'), eel.get_ulhi_and_symptoms()
}, false);
document.getElementById('next-btn-1').addEventListener('click', () => 
{checkIfValid('page-1'), eel.get_symptoms()}, false);
document.getElementById('back-btn-0').addEventListener('click', () => {
  navigate('page-0', 'main-menu')
}, false);
document.getElementById('back-btn-1').addEventListener('click', () => {
  navigate('page-1', 'page-0')
}, false);
document.getElementById('back-btn-2').addEventListener('click', () => {
  navigate('page-2', 'page-1')
}, false);
document.getElementById('back-btn-3').addEventListener('click', () => {navigate('add-symptom','main-menu'),resetFields(),hideMessage("success-1"),hideMessage("error-3")}, false);
document.getElementById('back-btn-lbp').addEventListener('click', () => {
  navigate('page-3', 'page-2')
}, false);
document.getElementById('back-btn-ulhi').addEventListener('click', () => {
  navigate('page-4', 'page-2')
}, false);
document.getElementById('back-btn-alert').addEventListener('click', () => {navigate('set-alert','main-menu'),resetFields(),hideMessage("success-2"),hideMessage("error-4")}, false);

document.getElementById('back-btn-del').addEventListener('click', () => {
  navigate('delete-symptoms', 'main-menu'), hideMessage("success-3")
}, false);
document.getElementById('submit-btn-1').addEventListener('click', checkSymptomValues, false);
document.getElementById('submit-btn-2').addEventListener('click', () => {checkIfValid('add-symptom')}, false); 
document.getElementById('submit-btn-lbp').addEventListener('click',() => {checkIfValid('page-3')}, false);
document.getElementById('submit-btn-ulhi').addEventListener('click', submit, false);
document.getElementById('submit-btn-del').addEventListener('click', getValuesToDelete, false);
document.getElementById('finish-btn').addEventListener('click', () => {
  navigate('results-page', 'main-menu')
}, false);
document.getElementById('email-all-btn').addEventListener('click', displayEmailModal, false);
document.getElementById('alert-btn').addEventListener('click', () => {
  navigate('main-menu', 'set-alert'), eel.get_alert_vals()
}, false);
document.getElementById('submit-btn-alert').addEventListener('click',() => {checkIfValid('set-alert')}, false);
// document.getElementById('email-btn').addEventListener('click',emailDiagnosis, false);
document.getElementById('reset').addEventListener('click', displayResetModal, false);


const delay = ms => new Promise(res => setTimeout(res, ms));

var low_bp_symptoms = [];

eel.init_alerts(); //ensure alerts are initially 0
eel.get_statistics();
eel.get_low_bp_symptom();


function resetFields(){
  var fields = document.getElementsByTagName('input'),
    length = fields.length;
    while (length--) {
    if (fields[length].type === 'text' || fields[length].type == 'email' || fields[length].type == 'number'){
       fields[length].value = ''; 
      }
      if (fields[length].type == "radio") {
        fields[length].checked = false;
    }
  }

  document.getElementById("checksymptom").checked = false;
}

eel.expose(setLbpSymptoms);
function setLbpSymptoms(values){
  low_bp_symptoms = values;
  console.log(low_bp_symptoms);
}


function resetDb() {
  eel.reset_db();
  eel.get_statistics();
  // if (confirm("Are you sure you would like to reset the current database?")) {
  //   alert("Database reset successfully!");
  // } 
}

function checkIfValid(screen){
  if(screen === "page-0"){
    var isEmpty = false;  

    var f_name = document.getElementById("f_name").value.length;
    var l_name = document.getElementById("l_name").value.length;
    var email = document.getElementById("email").value.length;

    if(f_name == 0 || l_name == 0 || email == 0){
      isEmpty = true;
    } else {
      isEmpty = false;
    }

    if(isEmpty){
      document.getElementById("error-0").style.display="inline";
    } else {
      document.getElementById("error-0").style.display="none";
      navigate("page-0","page-1");
    }
  } else if (screen === "page-1") {
    var isEmpty = false;  

    var temperature = document.getElementById("temperature").value.length;
    var age = document.getElementById("age").value.length;

    if(temperature== 0 || age == 0){
      isEmpty = true;
    } else {
      isEmpty = false;
    }

    if(isEmpty){
      document.getElementById("error-1").style.display="inline";
    } else {
      document.getElementById("error-1").style.display="none";
      navigate("page-1","page-2");
    }

  } 
  else if (screen === "page-3"){
    var isEmpty = false; 

    var systolic = document.getElementById("systolic").value.length;
    var diastolic = document.getElementById("diastolic").value.length;

    if(systolic== 0 || diastolic == 0){
      isEmpty = true;
    } else {
      isEmpty = false;
    }

    if(isEmpty){
      document.getElementById("error-2").style.display="inline";
    } else {
      document.getElementById("error-2").style.display="none";
      eel.get_ulhi()
      navigate("page-3","page-4");
    }

  } 
  else if (screen === "add-symptom"){
    var isEmpty = false; 

    var symptom = document.getElementById("symptom-input").value.length; 
    var severity = document.querySelector('input[name="severity"]:checked');

    if(symptom == 0 || severity.length == 0){
      isEmpty = true;
    } else {
      isEmpty = false;
    }

    if(isEmpty){
      document.getElementById("error-3").style.display="inline";
    } else {
      document.getElementById("error-3").style.display="none";
      document.getElementById("success-1").style.display="inline";
      addSymptom();
    }
  } 
  else if (screen === "set-alert"){
    var isEmpty = false; 

    var alert = document.getElementById("alert-input").value.length; 
    var risk = document.querySelector('input[name="risk"]:checked');

    if(alert == 0 || risk.length == 0){
      isEmpty = true;
    } else {
      isEmpty = false;
    }

    if(isEmpty){
      document.getElementById("error-4").style.display="inline";
    } else {
      document.getElementById("error-4").style.display="none";
      document.getElementById("success-2").style.display="inline";
      setAlert();
    }
  }
  
}  

function hideMessage(msg){
  document.getElementById(msg).style.display="none";
}
 

eel.expose(getStatValues)
function getStatValues(total,veryHighRisk,highRisk,lowRisk,noRisk){

  if (total > 0 ){
    var vhrper = ((veryHighRisk/total)*100).toFixed(0);
    var hrper = ((highRisk/total)*100).toFixed(0);
    var lrper = ((lowRisk/total)*100).toFixed(0);
    var nrper = ((noRisk/total)*100).toFixed(0);
  } else {
    vhrper = 0;
    hrper = 0;
    lrper = 0;
    nrper = 0;  
  }
 
  document.getElementById("total-stat").innerHTML = "Total Diagnoses: " + total
  document.getElementById("veryhigh-stat").innerHTML = "Very High Risk: " + veryHighRisk + " (" + vhrper +"%)"
  document.getElementById("high-stat").innerHTML = "High Risk: " + highRisk + " (" + hrper +"%)"
  document.getElementById("low-stat").innerHTML = "Low Risk: " + lowRisk + " (" + lrper +"%)"
  document.getElementById("norisk-stat").innerHTML = "No Risk: " + noRisk + " (" + nrper +"%)"
} 
eel.expose(setAlertVals)

function setAlertVals(alertvals) {
  document.getElementById("alert-lbl-1").innerHTML = "Very High Risk (" + alertvals[0] + ")"
  document.getElementById("alert-lbl-2").innerHTML = "High Risk (" + alertvals[1] + ")"
  document.getElementById("alert-lbl-3").innerHTML = "Low Risk (" + alertvals[2] + ")"
  document.getElementById("alert-lbl-4").innerHTML = "Not at Risk (" + alertvals[3] + ")"
}

function setAlert() {
  var alert_type = document.querySelector('input[name="risk"]:checked').value;
  console.log(alert_type);
  var val = document.getElementById("alert-input").value;
  eel.update_alert(alert_type, val);
}

function emailDiagnosesReport() {
  eel.email_all_diagnoses();
}

function checkSymptomValues() {
  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');
  var lowBp = false;
  for (var i = 0; i < checkboxes.length; i++) {
    if (low_bp_symptoms.indexOf(checkboxes[i].value)>-1) {     
      lowBp = true;
      console.log("true");
      break;
    } else {
      console.log(checkboxes[i].value);
    }
  }
  if (lowBp == true) {
    navigate('page-2', 'page-3');
  } else {
    eel.get_ulhi();
    navigate('page-2', 'page-4');
  }
}

function timeout(ms) { //pass a time in milliseconds to this function
  return new Promise(resolve => setTimeout(resolve, ms));
}

function hideSpinner() {
  document.getElementById("loader-1").style.display = "none";
}

function hideModalSpinner() {
  document.getElementById("modal-loader").style.display = "none";
  document.getElementById('modal-txt').innerHTML = "Database reset successfully!";
  document.getElementById("confirm-btn").disabled = true;
}

function showSpinner() {
  document.getElementById("loader-1").style.display = "block";
}

function submit() {
  navigate("page-4", "results-page");
  showSpinner();
  setTimeout(hideSpinner, 3000);

  getDiagnosisDetails();
  eel.get_statistics();
  resetFields();
}

eel.expose(showResult)

function showResult(res) {
  console.log(res);
  document.getElementById('results').innerHTML = res;
}

function getDiagnosisDetails() {
  var firstname = document.getElementById('f_name').value;
  var lastname = document.getElementById('l_name').value;
  var age = document.getElementById('age').value;
  var temperature = document.getElementById('temperature').value;
  var email = document.getElementById('email').value;

  var symptoms = [];
  var symptom_checkboxes = document.querySelectorAll('#symptom-checkboxes input[type=checkbox]:checked');
  var ulhi = [];
  var ulhi_checkboxes = document.querySelectorAll('#ulhi-checkboxes input[type=checkbox]:checked');

  for (var i = 0; i < symptom_checkboxes.length; i++) {
    symptoms.push(symptom_checkboxes[i].value);
  }

  for (var i = 0; i < ulhi_checkboxes.length; i++) {
    ulhi.push(ulhi_checkboxes[i].value);
  }

  console.log(firstname);
  console.log(lastname);
  console.log(age);
  celciusToFarenheit(temperature);
  console.log(symptoms);
  eel.diagnose(firstname, lastname, email, age, symptoms, ulhi, celciusToFarenheit(temperature));

}

function celciusToFarenheit(celsius) {
  var cTemp = celsius;
  var cToFahr = cTemp * 9 / 5 + 32;

  return cToFahr.toFixed(1);
}

eel.expose(add_symptom_checkboxes);

function add_symptom_checkboxes(symptoms) {
  createSymptomCheckboxes(symptoms)
  console.log(symptoms);
}

function addSymptom() {
  var severity = document.querySelector('input[name="severity"]:checked').value;
  var symptom = document.getElementById("symptom-input").value;
  var isLbp = document.getElementById("checksymptom").checked;
  console.log(isLbp);
  eel.add_symptom(symptom, severity,isLbp);
}

eel.expose(addStats);

function addStats(stats) {
  console.log(stats);
  document.getElementById("total-stat").innerHTML = "Total Diagnoses: " + stats;
}

function updateStats(stat) {
  eel.update_stats(stat);
  console.log("updating");
}


function navigate(fromScreen, toScreen) {
  document.getElementById(fromScreen).style.display = "none";
  document.getElementById(toScreen).style.display = "inline";
}

function createSymptomCheckboxes(symptoms) {

  const parent = document.getElementById('symptom-checkboxes') //clear current checkboxes
  while (parent.firstChild) {
    parent.firstChild.remove();
  }

  for (var i = 0; i < symptoms.length; i++) {
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

eel.expose(createUlhiCheckboxes);

function createUlhiCheckboxes(ulhi) {

  const parent = document.getElementById('ulhi-checkboxes') //clear current checkboxes
  while (parent.firstChild) {
    parent.firstChild.remove();
  }

  for (var i = 0; i < ulhi.length; i++) {
    console.log(ulhi[i]);

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = ulhi[i];
    checkbox.value = ulhi[i];

    var label = document.createElement('label')
    label.htmlFor = ulhi[i];
    label.appendChild(document.createTextNode(ulhi[i]));

    var br = document.createElement('br');

    var container = document.createElement('container');
    container.appendChild(checkbox);
    container.appendChild(label);
    container.appendChild(br);
    parent.appendChild(container);
  }
}

eel.expose(createUlhiAndSymptomsCheckboxes);

function createUlhiAndSymptomsCheckboxes(values) {
  console.log("here");
  console.log(values);

  const parent = document.getElementById('all-checkboxes') //clear current checkboxes
  while (parent.firstChild) {
    parent.firstChild.remove();
  }

  for (var i = 0; i < values.length; i++) {
    console.log(values[i]);

    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = values[i];
    checkbox.value = values[i];

    var label = document.createElement('label')
    label.htmlFor = values[i];
    label.appendChild(document.createTextNode(values[i]));

    var br = document.createElement('br');

    var container = document.createElement('container');
    container.appendChild(checkbox);
    container.appendChild(label);
    container.appendChild(br);
    parent.appendChild(container);
  }

}

eel.expose()

function getValuesToDelete() {
  var values = [];
  var all_checkboxes = document.querySelectorAll('#all-checkboxes input[type=checkbox]:checked');
  for (var i = 0; i < all_checkboxes.length; i++) {
    values.push(all_checkboxes[i].value);
  }
  eel.delete_symptoms(values);
  document.getElementById("success-3").style.display="inline";
}

function displayResetModal() {
  var modal = document.getElementById("modal");
  var span = document.getElementsByClassName("close")[0];
  modal.style.display = "block";

  var header = document.getElementById('header-title');
  header.innerHTML = "Reset Database";

  var modal_body = document.getElementById('modal-txt');
  modal_body.innerHTML = "Are you sure you want to reset the database? This will reset " +
    "all current diagnoses as well as statistics.";

  var modal_footer = document.getElementById('modal-footer');
  var confirm_btn = document.createElement("confirm-btn");
  confirm_btn.innerHTML = "Confirm";
  var cancel_btn = document.createElement("cancel-btn");
  cancel_btn.innerHTML = "Cancel";
  confirm_btn.className = "modal-btn";
  cancel_btn.className = "modal-btn";

  modal_footer.style.textAlign = "right";
  const parent = modal_footer;
  while (parent.firstChild) {
    parent.firstChild.remove();
  }

  modal_footer.appendChild(cancel_btn);
  modal_footer.appendChild(confirm_btn);

  cancel_btn.onclick = function () {
    modal.style.display = "none";
  }

  span.onclick = function () {
    modal.style.display = "none";
  }
// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }

  confirm_btn.onclick = function () {
    modal_body.innerHTML = "";
    var loader = document.getElementById("modal-loader");
    loader.style.display = "block";
    resetDb();
    setTimeout(hideModalSpinner, 3000);
  }
}

}


  function displayEmailModal() {
    var modal = document.getElementById("modal");
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "block";

    var header = document.getElementById('header-title');
    header.innerHTML = "Email Diagnoses";

    var modal_body = document.getElementById('modal-txt');
    modal_body.innerHTML = "A spreadsheet with all diagnoses has successfully been emailed to the admin account " +
      "<strong>'utechmohexpertsystem2021@gmail.com'<strong>. "

    var modal_footer = document.getElementById('modal-footer');
    var close_btn = document.createElement("close-btn");
    close_btn.innerHTML = "Close";
    close_btn.className = "modal-btn";
    modal_footer.style.textAlign = "right";
    const parent = modal_footer;
    while (parent.firstChild) {
      parent.firstChild.remove();
    }
    modal_footer.appendChild(close_btn);

    emailDiagnosesReport();

    close_btn.onclick = function () {
      modal.style.display = "none";
    }
    span.onclick = function () {
      modal.style.display = "none";
    }
  }

