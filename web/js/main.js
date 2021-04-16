import * as symptoms from './modules/symptoms.js';

document.getElementById('diagnose-btn').addEventListener('click', () => {navigate('main-menu','page-0')}, false);
document.getElementById('add-btn').addEventListener('click', () => {navigate('main-menu','add-symptom')}, false);
document.getElementById('next-btn-0').addEventListener('click', () => 
{navigate('page-0','page-1')}, false);
document.getElementById('next-btn-1').addEventListener('click', () => 
{navigate('page-1','page-2'), eel.get_symptoms()}, false);
document.getElementById('back-btn-0').addEventListener('click', () => {navigate('page-0','main-menu')}, false);
document.getElementById('back-btn-1').addEventListener('click', () => {navigate('page-1','page-0')}, false);
document.getElementById('back-btn-2').addEventListener('click', () => {navigate('page-2','page-1')}, false);
document.getElementById('back-btn-3').addEventListener('click', () => {navigate('add-symptom','main-menu')}, false);
document.getElementById('back-btn-lbp').addEventListener('click', () => {navigate('page-3','page-2')}, false);
document.getElementById('back-btn-ulhi').addEventListener('click', () => {navigate('page-4','page-2')}, false);
document.getElementById('submit-btn-1').addEventListener('click', checkSymptomValues, false);
document.getElementById('submit-btn-2').addEventListener('click', addSymptom, false);
document.getElementById('submit-btn-lbp').addEventListener('click',() => {navigate('page-3','page-4'), eel.get_ulhi()}, false);
document.getElementById('submit-btn-ulhi').addEventListener('click',submit, false);
document.getElementById('finish-btn').addEventListener('click', () => {navigate('results-page','main-menu')}, false);
document.getElementById('email-all-btn').addEventListener('click',emailDiagnosesReport, false);
// document.getElementById('email-btn').addEventListener('click',emailDiagnosis, false);


const delay = ms => new Promise(res => setTimeout(res, ms));

eel.get_total_diagnoses();
// eel.assert_all_symptoms_from_txt();

// function emailDiagnosis(){
//   var email = document.getElementById('email').value;
//   alert("The patient's diagnosis results has been emailed to them successfully!");
// }

function emailDiagnosesReport(){
eel.email_all_diagnoses();
alert("Diagnoses report generated and emailed successfully!");
}

function checkSymptomValues(){
  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');
  var lowBp = false;
  for(var i = 0; i < checkboxes.length; i++){
    console.log(checkboxes[i].value + "==" + "dizziness");
    if(checkboxes[i].value === "dizziness\n" || checkboxes[i].value === "blurred vision\n" || checkboxes[i].value === "fainting\n"){
      lowBp = true;
      console.log("true");
      break;
    } 
  }
  if(lowBp == true){
    navigate('page-2','page-3');
  } else {
    eel.get_ulhi();
    navigate('page-2','page-4');
  }
}

function timeout(ms) { //pass a time in milliseconds to this function
  return new Promise(resolve => setTimeout(resolve, ms));
}

function hideSpinner(){
  document.getElementById("loader-1").style.display="none";
}

function showSpinner(){
  document.getElementById("loader-1").style.display="block";
}
function submit(){
  navigate("page-4","results-page");
  showSpinner();
  setTimeout(hideSpinner, 3000)

  getDiagnosisDetails();
}

eel.expose(showResult)
function showResult(res){
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

  for(var i = 0; i < symptom_checkboxes.length; i++){
    symptoms.push(symptom_checkboxes[i].value);
  }

  for(var i = 0; i < ulhi_checkboxes.length; i++){
    ulhi.push(ulhi_checkboxes[i].value);
  }

  console.log(firstname);
  console.log(lastname);
  console.log(age);
  celciusToFarenheit(temperature);
  console.log(symptoms);
  eel.diagnose(firstname,lastname,email,age,symptoms,ulhi,celciusToFarenheit(temperature));

}

function celciusToFarenheit(celsius) 
{
  var cTemp = celsius;
  var cToFahr = cTemp * 9 / 5 + 32;
  var message = cTemp+'\xB0C is ' + cToFahr + ' \xB0F.';
  console.log(message);
  return cToFahr;
}

eel.expose(add_symptom_checkboxes);
function add_symptom_checkboxes(symptoms) {
  createSymptomCheckboxes(symptoms)
  console.log(symptoms);
}

function addSymptom(){
  var severity = document.querySelector('input[name="severity"]:checked').value;
  console.log(severity);
  var symptom = document.getElementById("symptom-input").value;
  eel.add_symptom(symptom,severity);
} 

eel.expose(addStats);
function addStats(stats) {
  console.log(stats);
  document.getElementById("total-stat").innerHTML = "Total Diagnoses: " + stats;
}

function updateStats(stat){ 
  eel.update_stats(stat); 
  console.log("updating"); 
}


function navigate(fromScreen,toScreen){
  document.getElementById(fromScreen).style.display="none";
  document.getElementById(toScreen).style.display="inline";
}

function createSymptomCheckboxes(symptoms){

  const parent = document.getElementById('symptom-checkboxes') //clear current checkboxes
  while (parent.firstChild) {
      parent.firstChild.remove();
  }

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

  eel.expose(createUlhiCheckboxes);
  function createUlhiCheckboxes(ulhi){

    const parent = document.getElementById('ulhi-checkboxes') //clear current checkboxes
    while (parent.firstChild) {
        parent.firstChild.remove();
    }
  
    for (var i = 0; i < ulhi.length; i++){   
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

}