def interpretation(polarite, subjectivite):
    """
    interpretation is a function that converts a polarite and sujectivite number into a phrase

    polarite: a number generated with TextBlob library, a sentiment analysis library
    subjectivite: a number generated with TextBlob library, a sentiment analysis library

    return a concatenated str of polarity and subjectivity about an article
    """

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
