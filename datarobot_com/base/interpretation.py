def interpretation(polarite, subjectivite):

    if -1 <= polarite < -0.5:
        avis_polarite = "l'avis de l'auteur sur le sujet est négatif."
    elif -0.5 <= polarite <= 0.5:
        avis_polarite = "l'avis de l'auteur sur le sujet est plutôt neutre."
    else:
        avis_polarite = "l'avis de l'auteur sur le sujet est plutôt positif."
    if 0 <= subjectivite < 0.2:
        avis_subjectivite = "Le texte est objectif."
    elif 0.2 <= subjectivite <= 0.5:
        avis_subjectivite = "Le texte est plutôt objectif."
    elif 0.5 < subjectivite <= 0.8:
        avis_subjectivite = "Le texte est plutôt subjectif."
    else:
        avis_subjectivite = "Le texte est complètement subjectif."

    return avis_polarite + " " + avis_subjectivite


polarite_exemple = 0.1275343162175902
subjectivite_exemple = 0.36195611426928137
interpretation_resultat = interpretation(polarite_exemple, subjectivite_exemple)
print(interpretation_resultat)
