serious_symptoms(rash).
serious_symptoms(fever).
serious_symptoms(dry_cough).

common_symptoms(flu).
common_symptoms(loss_of_taste).

less_common_symptoms(none).
less_common_symptoms(runny_nose).

performAnalysis(DifficultyBreathing, RunnyNose, Aches, LossOfSmell, LossOfTaste, DryCough, Fever, Rash):-
				FeverVal is 1,
    			write('1'),
    
				% check serious symptoms severity
				(serious_symptoms(DifficultyBreathing) -> SeriousSymptomsVal is 3; SeriousSymptomsVal is 0),
				(serious_symptoms(RunnyNose) -> SeriousSymptomsVal is SeriousSymptomsVal + 3; SeriousSymptomsVal is SeriousSymptomsVal),
				(serious_symptoms(Aches) -> SeriousSymptomsVal is SeriousSymptomsVal + 3; SeriousSymptomsVal is SeriousSymptomsVal),
				(serious_symptoms(LossOfSmell) -> SeriousSymptomsVal is SeriousSymptomsVal + 3; SeriousSymptomsVal is SeriousSymptomsVal),
				(serious_symptoms(LossOfTaste) -> SeriousSymptomsVal is SeriousSymptomsVal + 3; SeriousSymptomsVal is SeriousSymptomsVal),
    			write('2'),

				% check less common symptoms
				(less_common_symptoms(DifficultyBreathing) -> LessCommonSymptomsVal is 1; LessCommonSymptomsVal is 0),
                %(less_common_symptoms(RunnyNose) -> LessCommonSymptomsVal is LessCommonSymptomsVal + 1; LessCommonSymptomsVal is LessCommonSymptomsVal),
                (less_common_symptoms(Aches) -> LessCommonSymptomsVal is LessCommonSymptomsVal + 1; LessCommonSymptomsVal is LessCommonSymptomsVal),
                (less_common_symptoms(LossOfSmell) -> LessCommonSymptomsVal is LessCommonSymptomsVal + 1; LessCommonSymptomsVal is LessCommonSymptomsVal),
                (less_common_symptoms(LossOfTaste) -> LessCommonSymptomsVal is LessCommonSymptomsVal + 1; LessCommonSymptomsVal is LessCommonSymptomsVal),
    			write('3'),

                % check common symptoms
                %(common_symptoms(DifficultyBreathing) -> CommonSymptomsVal is 2; CommonSymptomsVal is 0),
                %(common_symptoms(RunnyNose) -> CommonSymptomsVal is CommonSymptomsVal + 2; CommonSymptomsVal is CommonSymptomsVal),
                %(common_symptoms(Aches) -> CommonSymptomsVal is CommonSymptomsVal + 2; CommonSymptomsVal is CommonSymptomsVal),
                %(common_symptoms(LossOfSmell) -> CommonSymptomsVal is CommonSymptomsVal + 2; CommonSymptomsVal is CommonSymptomsVal),
               %(common_symptoms(LossOfTaste) -> CommonSymptomsVal is CommonSymptomsVal + 2; CommonSymptomsVal is CommonSymptomsVal),
    			CommonSymptomsVal is 1,
    			write('4'),

                % calculate risk score to determine severity of the info provided by the user
                (RiskScore is SeriousSymptomsVal+LessCommonSymptomsVal+CommonSymptomsVal),
    			write('5'),

                % prolog function call to determine the risk result based on user input
    			write('yasso'),
    			nl,write("FeverVal:"),write(FeverVal),write(" RS:"),write(RiskScore),
    			write(" SS:"),write(SeriousSymptomsVal),write("LCS:"),write(LessCommonSymptomsVal),write("CSV: "),write(CommonSymptomsVal),
				determine_risk_val(FeverVal, RiskScore, SeriousSymptomsVal, LessCommonSymptomsVal, CommonSymptomsVal).

% function to determine if client is at risk
determine_risk_val(FeverVal, RiskScore, SeriousSymptomsVal, LessCommonSymptomsVal, CommonSymptomsVal):-
    			nl,write("here!"),
                (FeverVal == 1, SeriousSymptomsVal > 0) -> R is 0 ,
                (FeverVal == 1, LessCommonSymptomsVal > 0) -> R = "Your risk is very high. You have a fever and at least one less common covid 19 symptoms",
                (FeverVal == 1, CommonSymptomsVal > 0) -> R = "Your risk is very high. You have a fever and at least one common covid 19 symptoms",
				(FeverVal == 1, RiskScore < 1) -> R = "Youre at risk. You don't have any common, serious or less common symptoms, however you have a fever based on the temperature above." ,
				write('here'),
                R = "Youre not at risk",
				write(R).

