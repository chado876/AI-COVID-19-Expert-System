:- dynamic serious_symptoms/1.
:- dynamic common_symptoms/1.
:- dynamic less_common_symptoms/1.

serious_symptoms(none).
common_symptoms(none).
less_common_symptoms(none).



diagnose(Temp,Age,UHI,Fever,DryCough,Tiredness,Aches,SoreThroat,Diarrhoea,Conjuctivitis,Headache,LossOfTasteOrSmell,RashOrDiscolouration,ChestPain,LossOfSpeechOrMovement,Serious,Common,LessCommon,CurrentFever,Result):-    			
    			(Temp > 100.4 ->  HasFever = y; HasFever = n),
    			write("TEMP:"),write(Temp),nl,
    			write("FEVER"),write(Fever),nl,
   				write("HasFever::"),
    			write(HasFever),nl,
    			
    			(serious_symptoms(Fever) -> SeriousSymptomsVal1 is 1; SeriousSymptomsVal1 is 0),
				(serious_symptoms(DryCough) -> SeriousSymptomsVal2 is SeriousSymptomsVal1 + 1; SeriousSymptomsVal2 is SeriousSymptomsVal1),
				(serious_symptoms(Conjuctivitis) -> SeriousSymptomsVal3 is SeriousSymptomsVal2 + 1; SeriousSymptomsVal3 is SeriousSymptomsVal2),
    			(serious_symptoms(Tiredness) -> SeriousSymptomsVal4 is SeriousSymptomsVal2 + 1; SeriousSymptomsVal4 is SeriousSymptomsVal3),
				(serious_symptoms(Aches) -> SeriousSymptomsVal5 is SeriousSymptomsVal4 + 1; SeriousSymptomsVal5 is SeriousSymptomsVal4),
				(serious_symptoms(SoreThroat) -> SeriousSymptomsVal6 is SeriousSymptomsVal5 + 1; SeriousSymptomsVal6 is SeriousSymptomsVal5),
				(serious_symptoms(Diarrhoea) -> SeriousSymptomsVal7 is SeriousSymptomsVal6 + 1; SeriousSymptomsVal7 is SeriousSymptomsVal6),
				(serious_symptoms(Headache) -> SeriousSymptomsVal8 is SeriousSymptomsVal7 + 1; SeriousSymptomsVal8 is SeriousSymptomsVal7),
				(serious_symptoms(LossOfTasteOrSmell) -> SeriousSymptomsVal9 is SeriousSymptomsVal8 + 1; SeriousSymptomsVal9 is SeriousSymptomsVal8),
				(serious_symptoms(RashOrDiscolouration) -> SeriousSymptomsVal10 is SeriousSymptomsVal9 + 1; SeriousSymptomsVal10 is SeriousSymptomsVal9),
				(serious_symptoms(ChestPain) -> SeriousSymptomsVal11 is SeriousSymptomsVal10 + 1; SeriousSymptomsVal11 is SeriousSymptomsVal10),
				(serious_symptoms(LossOfSpeechOrMovement) -> SeriousSymptomsVal is SeriousSymptomsVal11 + 1; SeriousSymptomsVal is SeriousSymptomsVal11),
    			
    			write("TOTAL SERIOUS SYMPTOM VAL::"),write(SeriousSymptomsVal),nl,
    			
        		(common_symptoms(Fever) -> CommonSymptomsVal1 is 1; CommonSymptomsVal1 is 0),
				(common_symptoms(DryCough) -> CommonSymptomsVal2 is CommonSymptomsVal1 + 1; CommonSymptomsVal2 is CommonSymptomsVal1),
				(common_symptoms(Conjuctivitis) -> CommonSymptomsVal3 is CommonSymptomsVal2 + 1; CommonSymptomsVal3 is CommonSymptomsVal2),
    			(common_symptoms(Tiredness) -> CommonSymptomsVal4 is CommonSymptomsVal2 + 1; CommonSymptomsVal4 is CommonSymptomsVal3),
				(common_symptoms(Aches) -> CommonSymptomsVal5 is CommonSymptomsVal4 + 1; CommonSymptomsVal5 is CommonSymptomsVal4),
				(common_symptoms(SoreThroat) -> CommonSymptomsVal6 is CommonSymptomsVal5 + 1; CommonSymptomsVal6 is CommonSymptomsVal5),
				(common_symptoms(Diarrhoea) -> CommonSymptomsVal7 is CommonSymptomsVal6 + 1; CommonSymptomsVal7 is CommonSymptomsVal6),
				(common_symptoms(Headache) -> CommonSymptomsVal8 is CommonSymptomsVal7 + 1; CommonSymptomsVal8 is CommonSymptomsVal7),
				(common_symptoms(LossOfTasteOrSmell) -> CommonSymptomsVal9 is CommonSymptomsVal8 + 1; CommonSymptomsVal9 is CommonSymptomsVal8),
				(common_symptoms(RashOrDiscolouration) -> CommonSymptomsVal10 is CommonSymptomsVal9 + 1; CommonSymptomsVal10 is CommonSymptomsVal9),
				(common_symptoms(ChestPain) -> CommonSymptomsVal11 is CommonSymptomsVal10 + 1; CommonSymptomsVal11 is CommonSymptomsVal10),
				(common_symptoms(LossOfSpeechOrMovement) -> CommonSymptomsVal is CommonSymptomsVal11 + 1; CommonSymptomsVal is CommonSymptomsVal11),
    			
    			write("TOTAL Common SYMPTOM VAL::"),write(CommonSymptomsVal),nl,
    
    			(less_common_symptoms(Fever) -> LessCommonSymptomsVal1 is 1; LessCommonSymptomsVal1 is 0),
				(less_common_symptoms(DryCough) -> LessCommonSymptomsVal2 is LessCommonSymptomsVal1 + 1; LessCommonSymptomsVal2 is LessCommonSymptomsVal1),
				(less_common_symptoms(Conjuctivitis) -> LessCommonSymptomsVal3 is LessCommonSymptomsVal2 + 1; LessCommonSymptomsVal3 is LessCommonSymptomsVal2),
    			(less_common_symptoms(Tiredness) -> LessCommonSymptomsVal4 is LessCommonSymptomsVal2 + 1; LessCommonSymptomsVal4 is LessCommonSymptomsVal3),
				(less_common_symptoms(Aches) -> LessCommonSymptomsVal5 is LessCommonSymptomsVal4 + 1; LessCommonSymptomsVal5 is LessCommonSymptomsVal4),
				(less_common_symptoms(SoreThroat) -> LessCommonSymptomsVal6 is LessCommonSymptomsVal5 + 1; LessCommonSymptomsVal6 is LessCommonSymptomsVal5),
				(less_common_symptoms(Diarrhoea) -> LessCommonSymptomsVal7 is LessCommonSymptomsVal6 + 1; LessCommonSymptomsVal7 is LessCommonSymptomsVal6),
				(less_common_symptoms(Headache) -> LessCommonSymptomsVal8 is LessCommonSymptomsVal7 + 1; LessCommonSymptomsVal8 is LessCommonSymptomsVal7),
				(less_common_symptoms(LossOfTasteOrSmell) -> LessCommonSymptomsVal9 is LessCommonSymptomsVal8 + 1; LessCommonSymptomsVal9 is LessCommonSymptomsVal8),
				(less_common_symptoms(RashOrDiscolouration) -> LessCommonSymptomsVal10 is LessCommonSymptomsVal9 + 1; LessCommonSymptomsVal10 is LessCommonSymptomsVal9),
				(less_common_symptoms(ChestPain) -> LessCommonSymptomsVal11 is LessCommonSymptomsVal10 + 1; LessCommonSymptomsVal11 is LessCommonSymptomsVal10),
				(less_common_symptoms(LossOfSpeechOrMovement) -> LessCommonSymptomsVal is LessCommonSymptomsVal11 + 1; LessCommonSymptomsVal is LessCommonSymptomsVal11),
    			
    			write("TOTAL Less Common SYMPTOM VAL::"),write(LessCommonSymptomsVal),nl,
    			% calculate risk score to determine severity of the info provided by the user
                (RiskScore is SeriousSymptomsVal+LessCommonSymptomsVal+CommonSymptomsVal),
    			write("RISK:"),write(RiskScore),nl,
    			write("SERIOUS:"),write(SeriousSymptomsVal),nl,
        		write("Common:"),write(CommonSymptomsVal),nl,
            	write("Less Common:"),write(LessCommonSymptomsVal),nl,
    			write("Age:"),write(Age),nl,
    			write("Total Underlying Health Issues:"),write(UHI),nl,

	
				%Result is 0,  
   				%nl,write(HasFever),
    			%(HasFever == y) ->  Result is 1;Result is 2.
    			((HasFever == y, SeriousSymptomsVal > 0) -> Risk = "Very High Risk";
                (HasFever == y, LessCommonSymptomsVal > 0) -> Risk = "Low Risk";
                (HasFever == y, CommonSymptomsVal > 0) -> Risk = "High Risk";
                (Age > 60, UHI > 0, SeriousSymptomsVal > 0) -> Risk = "Very High Risk";  
				(Age > 60, UHI > 0, LessCommonSymptomsVal > 0) -> Risk = "Low Risk";  
                (Age > 60, UHI > 0, CommonSymptomsVal > 0) -> Risk = "High Risk";  
                (HasFever == y, RiskScore < 1) -> Risk = "Lower Risk";
    			Risk = "Not at Risk"),
    			(HasFever == y -> CurrentFever = "true"; CurrentFever = "false"),
				Serious = SeriousSymptomsVal,
				Common = CommonSymptomsVal,
				LessCommon = LessCommonSymptomsVal,
				Result = Risk.
			
    			
	%diagnose(100.2,34,3,n,dy_cough,tiedness,ahes_and_pains,ore_throat,diarroea,conjuctiitis,headahe,loss_of_tate,ash,chest_pain,los_of_speech,Result).


