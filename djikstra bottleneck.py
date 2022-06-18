def djikstra_bottleneck(dg, s):
    """"
    arguments : dg - dictionnaire du graphe {sommet : {successeur: poids}}
                s - le sommet origine
                les sommets sont de type str
    sortie : s_connu - dictionnaire { sommet : [longueur, plus court chemin]}
    """
    # -------------------------------------initialisation----------------------------------------------------------------
    p = []  # la liste contenant les poids des arcs de plus cours chemins
    infini = sum(
        sum(dg[sommet][s2] for s2 in dg[sommet]) for sommet in dg) + 1  # on choisit cette valeur comme l'infini
    s_connu = {s: [0, [s]]}  # [longeur, plus court chemin]
    s_inconnu = {k: [infini, ''] for k in dg if k != s}  # [longueur, precedent]
    for suivant in dg[s]:
        s_inconnu[suivant] = [dg[s][suivant], s]
    print('dans le graphe d\'origine {} dont les arcs sont:'.format(s))  # affichage du graphe
    for k in dg:
        print(k, ':', dg[k])
    print()
    print('plus courts chemins de')
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
        print('longueur', longueur_u, ':', '->'.join(s_connu[u][1]))
        for v in s_connu[u][1][
                 :-1]:  # s_connu[u][1][:-1] contient les sommets de plus court chemins de s vers tout les autres
            p.append(dg[v][s_connu[u][1][s_connu[u][1].index(
                v) + 1]])  # on ajoute a la liste p le poids de l'arc qui relie les sommets de plus court chemins
        print(' l’engorgement de ce chemin = ', max(p))
    for k in s_inconnu:
        print('il n\'y a aucun chemin de {} a {}'.format(s, k))
    print()
    return s_connu

graphe = {  # j'ai utilisé le graphe de l'exo 2 comme un exemple pour vérifier
    's': {'a': 2,
          'b': 5},
    'a': {'b': 2,
          'c': 4,
          'd': 8},
    'b': {'c': 3,
          'e': 9},
    'c': {'d': 3,
          'e': 3},
    'd': {'e': 7,
          'f': 9},
    'f': {'e': 3}
}
# ---------------------------------------------main----------------------------------------------------------------------
print('\ntext file to dictionary=\n', graphe)
djikstra_bottleneck(graphe, 's')
