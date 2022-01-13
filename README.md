L'objectif principal de notre application est d'apprendre le pinyin chinois. Nous nous adressons aux étrangers qui apprennent le chinois ou aux enfants dont la langue maternelle est le chinois.

L'application comporte deux services principaux, l'un est une fonction de requête où l'utilisateur saisit un caractère chinois et la page web renvoie tous les pinyins de ce caractère (si le caractère est polyphonique).
Dans l'autre cas, l'utilisateur saisit le pinyin d'un caractère chinois sur la base du caractère chinois que nous lui fournissons, et nous évaluons dans quelle mesure le pinyin est correct pour ce caractère, plutôt que de simplement donner un résultat indiquant s'il est correct ou non.

Grâce au travail de la dernière année scolaire, ils ont mis le corpus sur github.

Cela s'explique par le fait que le pinyin des caractères chinois contient généralement deux parties, la voyelle et la rime. Nous déterminerons dans quelle mesure ces deux parties correspondent à la bonne réponse en fonction de la saisie de l'utilisateur.



consonne initiale
Rime syllabique en mandarin