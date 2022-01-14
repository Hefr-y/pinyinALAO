def Levenshtein_Distance(str1, str2):
    """Calculer la distance d'édition entre str1 et str2

    Args:
        str1{str}: N'importe quelle chaîne
        str1{str}: N'importe quelle chaîne

    Returns:
        sim{float}: similarité des chaînes.
                    La similarité est obtenue par 1/(1+x).
                    La variable {x} est la distance d'édition de Levenshtein.
    """
    matrix = [[ i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)

    dist = matrix[len(str1)][len(str2)]
    sim = 1/(1+dist)
    sim = round(sim,3)
    return sim

sim = Levenshtein_Distance("zhong", "zong")

print(sim)