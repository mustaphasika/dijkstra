def djikstra(dg, s):
    """"
    arguments : dg - dictionnaire du graphe {sommet : {successeur: poids}}
                s - le sommet origine
                les sommets sont de type str
    sortie : s_connu - dictionnaire { sommet : [longueur, plus court chemin]}
    """
    # -------------------------------------initialisation----------------------------------------------------------------
    infini = sum(
        sum(dg[sommet][s2] for s2 in dg[sommet]) for sommet in dg) + 1  # on choisit cette valeur comme l'infini
    s_connu = {s: [0, [s]]}  # [longeur, plus court chemin]
    s_inconnu = {k: [infini, ''] for k in dg if k != s}  # [longueur, precedent]
    for suivant in dg[s]:
        s_inconnu[suivant] = [dg[s][suivant], s]
    # -------------------------------------La recherche du chemin--------------------------------------------------------
    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
        u = min(s_inconnu, key=s_inconnu.get)  # recuperer le sommet relier a l'origine dont le poids est minimum
        longueur_u, precedent_u = s_inconnu[u]
        for v in dg[u]:
            if v in s_inconnu:
                d = longueur_u + dg[u][v]
                if d < s_inconnu[v][0]:
                    s_inconnu[v] = [d, u]
        s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u]]
        del s_inconnu[u]
    for k in s_inconnu:
        print('il n\'y a aucun chemin de {} a {}'.format(s, k))
    print()
    return s_connu

# ---------------------------------tronsformer le fichier txt en dictionnaire-------------------------------------------
dictionary = {}
vdict = {}
with open("/djikstra-test2.txt") as file:
    for line in file:
        """print(line.split()[1:])"""
        for v in line.split()[1:]:
            """print(v.split(','))"""
            (key, value) = v.split(',')
            """print(key, value)"""
            vdict[key] = int(value)
        (key2, value2) = (line.split()[0], dict)
        dictionary[key2] = vdict
        vdict = {}

# ---------------------------------------------mainnn----------------------------------------------------------------------
s = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
for _ in s:
    print('la distance de s a', _, 'est :', djikstra(dictionary, '1').get(str(_))[0], 'les sommet visités sont:',
          djikstra(dictionary, '1').get(str(_))[1])
