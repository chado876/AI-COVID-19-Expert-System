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
document.getElementById('submit-btn-1').addEventListener('click', () => {updateStats('total')}, false);
document.getElementById('submit-btn-2').addEventListener('click', addSymptom, false);

eel.read_stats();

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
  document.getElementById("total-stat").innerHTML = "Total Diagnoses: " + stats[0];
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