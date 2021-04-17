:- dynamic serious_symptoms/1.
:- dynamic common_symptoms/1.
:- dynamic less_common_symptoms/1.

serious_symptoms(none).
common_symptoms(none).
less_common_symptoms(none).

%accept temperature,age, underlying health issues, up to 10 symptoms, and variables to hold total serious,
%total common, total less commmon, if the patient has a current fever & the result
diagnose(Temperature,Age,UHI,Symptom1,Symptom2,Symptom3,Symptom4,Symptom5,Symptom6,Symptom7,Symptom8,
		Symptom9,Symptom10,TotalSerious,TotalCommon,TotalLessCommon,CurrentFever,Result):-    			
    			(Temperature > 100.4 ->  HasFever = y; HasFever = n),
    			write("TEMP:"),write(Temp),nl,
   				write("HasFever::"),
    			write(HasFever),nl,
    			
				%check each of the 10 symptoms if they fall under serious, common or less common,
				%add 1 to the respective total value if it meets the condition

    			(serious_symptoms(Symptom1) -> SeriousSymptomsTotal1 is 1; SeriousSymptomsTotal1 is 0),
				(serious_symptoms(Symptom2) -> SeriousSymptomsTotal2 is SeriousSymptomsTotal1 + 1; SeriousSymptomsTotal2 is SeriousSymptomsTotal1),
				(serious_symptoms(Symptom3) -> SeriousSymptomsTotal3 is SeriousSymptomsTotal2 + 1; SeriousSymptomsTotal3 is SeriousSymptomsTotal2),
    			(serious_symptoms(Symptom4) -> SeriousSymptomsTotal4 is SeriousSymptomsTotal2 + 1; SeriousSymptomsTotal4 is SeriousSymptomsTotal3),
				(serious_symptoms(Symptom5) -> SeriousSymptomsTotal5 is SeriousSymptomsTotal4 + 1; SeriousSymptomsTotal5 is SeriousSymptomsTotal4),
				(serious_symptoms(Symptom6) -> SeriousSymptomsTotal6 is SeriousSymptomsTotal5 + 1; SeriousSymptomsTotal6 is SeriousSymptomsTotal5),
				(serious_symptoms(Symptom7) -> SeriousSymptomsTotal7 is SeriousSymptomsTotal6 + 1; SeriousSymptomsTotal7 is SeriousSymptomsTotal6),
				(serious_symptoms(Symptom8) -> SeriousSymptomsTotal8 is SeriousSymptomsTotal7 + 1; SeriousSymptomsTotal8 is SeriousSymptomsTotal7),
				(serious_symptoms(Symptom9) -> SeriousSymptomsTotal9 is SeriousSymptomsTotal8 + 1; SeriousSymptomsTotal9 is SeriousSymptomsTotal8),
				(serious_symptoms(Symptom10) -> SeriousSymptomsTotal is SeriousSymptomsTotal9 + 1; SeriousSymptomsTotal is SeriousSymptomsTotal9),
			
    			
    			write("TOTAL SERIOUS SYMPTOM Total::"),write(SeriousSymptomsTotal),nl,
    			
        		(common_symptoms(Symptom1) -> CommonSymptomsTotal1 is 1; CommonSymptomsTotal1 is 0),
				(common_symptoms(Symptom2) -> CommonSymptomsTotal2 is CommonSymptomsTotal1 + 1; CommonSymptomsTotal2 is CommonSymptomsTotal1),
				(common_symptoms(Symptom3) -> CommonSymptomsTotal3 is CommonSymptomsTotal2 + 1; CommonSymptomsTotal3 is CommonSymptomsTotal2),
    			(common_symptoms(Symptom4) -> CommonSymptomsTotal4 is CommonSymptomsTotal2 + 1; CommonSymptomsTotal4 is CommonSymptomsTotal3),
				(common_symptoms(Symptom5) -> CommonSymptomsTotal5 is CommonSymptomsTotal4 + 1; CommonSymptomsTotal5 is CommonSymptomsTotal4),
				(common_symptoms(Symptom6) -> CommonSymptomsTotal6 is CommonSymptomsTotal5 + 1; CommonSymptomsTotal6 is CommonSymptomsTotal5),
				(common_symptoms(Symptom7) -> CommonSymptomsTotal7 is CommonSymptomsTotal6 + 1; CommonSymptomsTotal7 is CommonSymptomsTotal6),
				(common_symptoms(Symptom8) -> CommonSymptomsTotal8 is CommonSymptomsTotal7 + 1; CommonSymptomsTotal8 is CommonSymptomsTotal7),
				(common_symptoms(Symptom9) -> CommonSymptomsTotal9 is CommonSymptomsTotal8 + 1; CommonSymptomsTotal9 is CommonSymptomsTotal8),
				(common_symptoms(Symptom10) -> CommonSymptomsTotal is CommonSymptomsTotal9 + 1; CommonSymptomsTotal is CommonSymptomsTotal9),
    			
    			write("TOTAL Common SYMPTOM Total::"),write(CommonSymptomsTotal),nl,
    
    			(less_common_symptoms(Symptom1) -> LessCommonSymptomsTotal1 is 1; LessCommonSymptomsTotal1 is 0),
				(less_common_symptoms(Symptom2) -> LessCommonSymptomsTotal2 is LessCommonSymptomsTotal1 + 1; LessCommonSymptomsTotal2 is LessCommonSymptomsTotal1),
				(less_common_symptoms(Symptom3) -> LessCommonSymptomsTotal3 is LessCommonSymptomsTotal2 + 1; LessCommonSymptomsTotal3 is LessCommonSymptomsTotal2),
    			(less_common_symptoms(Symptom4) -> LessCommonSymptomsTotal4 is LessCommonSymptomsTotal2 + 1; LessCommonSymptomsTotal4 is LessCommonSymptomsTotal3),
				(less_common_symptoms(Symptom5) -> LessCommonSymptomsTotal5 is LessCommonSymptomsTotal4 + 1; LessCommonSymptomsTotal5 is LessCommonSymptomsTotal4),
				(less_common_symptoms(Symptom6) -> LessCommonSymptomsTotal6 is LessCommonSymptomsTotal5 + 1; LessCommonSymptomsTotal6 is LessCommonSymptomsTotal5),
				(less_common_symptoms(Symptom7) -> LessCommonSymptomsTotal7 is LessCommonSymptomsTotal6 + 1; LessCommonSymptomsTotal7 is LessCommonSymptomsTotal6),
				(less_common_symptoms(Symptom8) -> LessCommonSymptomsTotal8 is LessCommonSymptomsTotal7 + 1; LessCommonSymptomsTotal8 is LessCommonSymptomsTotal7),
				(less_common_symptoms(Symptom9) -> LessCommonSymptomsTotal9 is LessCommonSymptomsTotal8 + 1; LessCommonSymptomsTotal9 is LessCommonSymptomsTotal8),
				(less_common_symptoms(Symptom10) -> LessCommonSymptomsTotal is LessCommonSymptomsTotal9 + 1; LessCommonSymptomsTotal is LessCommonSymptomsTotal9),
    			
    			write("TOTAL Less Common SYMPTOM Total::"),write(LessCommonSymptomsTotal),nl,

                (RiskScore is SeriousSymptomsTotal+LessCommonSymptomsTotal+CommonSymptomsTotal),
				
    			write("RISK:"),write(RiskScore),nl,
    			write("SERIOUS:"),write(SeriousSymptomsTotal),nl,
        		write("Common:"),write(CommonSymptomsTotal),nl,
            	write("Less Common:"),write(LessCommonSymptomsTotal),nl,
    			write("Age:"),write(Age),nl,
    			write("Total Underlying Health Issues:"),write(UHI),nl,

    			((HasFever == y, SeriousSymptomsTotal > 0) -> Risk = "Very High Risk";
                (HasFever == y, LessCommonSymptomsTotal > 0) -> Risk = "Low Risk";
                (HasFever == y, CommonSymptomsTotal > 0) -> Risk = "High Risk";
                (Age > 60, UHI > 0, SeriousSymptomsTotal > 0) -> Risk = "Very High Risk";  
				(Age > 60, UHI > 0, LessCommonSymptomsTotal > 0) -> Risk = "Low Risk";  
                (Age > 60, UHI > 0, CommonSymptomsTotal > 0) -> Risk = "High Risk";  
                (HasFever == y, RiskScore < 1) -> Risk = "Low Risk";
    			Risk = "Not at Risk"),
    			(HasFever == y -> CurrentFever = "true"; CurrentFever = "false"),
				TotalSerious = SeriousSymptomsTotal,
				TotalCommon = CommonSymptomsTotal,
				TotalLessCommon = LessCommonSymptomsTotal,
				Result = Risk.
			

	%diagnose(100.5,34,3,nausea,tiredness,aches,sore_throat,diarroea,conjuctivitis,headache,loss_of_taste,chest_pain,loss_of_speech,Serious,Common,LessCommon,CurrentFever,Result).


