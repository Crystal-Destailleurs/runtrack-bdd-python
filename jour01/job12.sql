 INSERT INTO etudiant (id, nom, prenom, age, email)
    -> VALUES (6, 'dupuis', 'martin',  18, 'martin.dupuis@plateforme.io');

    SELECT *
    -> FROM etudiant
    -> WHERE nom = 'dupuis';