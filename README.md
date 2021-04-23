# COVID-19-Expert-System
Python & Prolog Covid-19 Expert System for an Artificial Intelligence class at UTECH

## Description
The Ministry of Health (MOH) has embarked on some programs/initiatives aimed at identifying and controlling
illnesses such as the Corona virus COVID-19. The Director of the MOH highlighted the need to educate the public
about these illnesses and has made the move to partner with the school of computing at the University of Technology
Jamaica (UTECH) to create an Expert system that could assist the MOH in its efforts.

The proposed Expert System (ES) should be populated with the details of various factors that will determine if a
person is at risk of having (or possibly has) COVID-19. Also, the steps that are required both in the short term and
long term. The information will be gathered by a team of three computer science students with skills in knowledge
acquisition and representation. The team will interview domain experts and use the data gathered to design and
implement the system prototype.
The expert system should provide an interface to allow the MOH to add knowledge to the system which will be used
in performing diagnoses.

It should also provide an option that allows the stakeholders to query the expert system providing details of possible
pending problems. This option should display the percentage of persons (based on the total persons diagnosed) who
are at risk of having (or possibly have) COVID-19. Two sets of statistics should be displayed by this option: The
percentage of persons with mild symptoms and the percentage of persons with severe symptoms.

The prototype should be able to accept the details of various contributory factors then make predictions based on the
details provided along with the encoded expert knowledge base. The details captured should include the patient’s
temperature which should be captured in degrees Celsius (°C) and converted to degrees Fahrenheit (°F). The system
should also ascertain if the patient has experienced dizziness, fainting or blurred vision. If any of these symptoms
are experienced the system should capture the systolic and diastolic values (mm Hg) for the patient to ascertain if the
patient has low blood pressure A systolic reading lower than 90 mm Hg or a diastolic reading lower than 60 mm Hg
indicates low blood pressure An option should be provided to allow the addition of other symptoms that require the
blood pressure check.

The set of questions the expert system asks should be guided by the input of the Stakeholders and the information
stored in the system’s knowledge base. Once the user has provided sufficient details the expert system should be able
to determine if a person is at risk of having (or possibly has) COVID-19. The system should display the possible
actions that are required both in the short term and long term based on the severity of symptoms.
The system should also provide the MOH with advice regarding the possible actions required and alert the
authorities of any spike or usual increase in reports of persons prone to having (or possible has) COVID-19.
The expert system’s knowledge base should be a prolog database that is accessed via Python.

The ES is expected to retain all the data entered by the user therefore allowing it to grow and become an important
asset to the MOH.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following libraries.

```bash
pip install eel
pip install openpyxl 
pip install sqlalchemy 
pip install pyswip
```
