import * as symptoms from './modules/symptoms.js';

document.getElementById('diagnose-btn').addEventListener('click', () => {navigate('main-menu','page-0')}, false);
document.getElementById('add-btn').addEventListener('click', () => {navigate('main-menu','add-symptom')}, false);
document.getElementById('next-btn-0').addEventListener('click', () => 
{navigate('page-0','page-1'), eel.get_symptoms()}, false);
document.getElementById('next-btn-1').addEventListener('click', () => 
{navigate('page-1','page-2'), eel.get_symptoms()}, false);
document.getElementById('back-btn-0').addEventListener('click', () => {navigate('page-0','main-menu')}, false);
document.getElementById('back-btn-1').addEventListener('click', () => {navigate('page-1','page-0')}, false);
document.getElementById('back-btn-2').addEventListener('click', () => {navigate('page-2','page-1')}, false);
document.getElementById('back-btn-3').addEventListener('click', () => {navigate('add-symptom','main-menu')}, false);
document.getElementById('back-btn-lbp').addEventListener('click', () => {navigate('page-3','page-2')}, false);
document.getElementById('submit-btn-1').addEventListener('click', checkSymptomValues, false);
document.getElementById('submit-btn-2').addEventListener('click', addSymptom, false);
document.getElementById('submit-btn-lbp').addEventListener('click',submit, false);


eel.get_total_diagnoses();

function checkSymptomValues(){
  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');
  var lowBp = false;
  for(var i = 0; i < checkboxes.length; i++){
    console.log(checkboxes[i].value + "==" + "dizziness");
    if(checkboxes[i].value === "dizziness\n" || checkboxes[i].value === "blurred vision\n" || checkboxes[i].value === "fainting\n"){
      lowBp = true;
      console.log("ture");
      break;
    } 
  }
  if(lowBp == true){
    document.getElementById('page-2').style.display="none";
    document.getElementById('page-3').style.display="inline";
  } else {
    // submit();
  }
}

function submit(){
  getDiagnosisDetails();
  updateStats('total');
}

function getDiagnosisDetails() {
  var firstname = document.getElementById('f_name').value;
  var lastname = document.getElementById('l_name').value;
  var age = document.getElementById('age').value;
  var temperature = document.getElementById('temperature').value;

  var symptoms = [];
  var checkboxes = document.querySelectorAll('input[type=checkbox]:checked');

  for(var i = 0; i < checkboxes.length; i++){
    symptoms.push(checkboxes[i].value);
  }

  console.log(firstname);
  console.log(lastname);
  console.log(age);
  celciusToFarenheit(temperature);
  console.log(symptoms);
  var gender = "male";

  eel.diagnose(firstname,lastname,age,gender,symptoms,temperature);
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
  createCheckboxes(symptoms)
  console.log(symptoms);
}

function addSymptom(){
  var symptom = document.getElementById("symptom-input").value;
  eel.add_symptom(symptom);
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

function switchScreen(fromScreen,toScreen){
  document.getElementById(fromScreen).style.display="none";
  document.getElementById(toScreen).style.display="inline";
}

function createCheckboxes(symptoms){

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

}