# Baseline de redevabilité HUMAN SWING / ChatGPT — 2026-10-08

**Mesure figée** le 8 octobre 2026, sur les fichiers cités ; horodatages d'origine en UTC. Ce rapport est **un point de départ**, pas une preuve de performance future. L'issue #134 et `docs/SCAN_DECISION_ACCOUNTABILITY_V1.md` définissent le protocole.

## Tableau de bord

| Domaine | Cohorte et horizon | Observation | Décision à ce stade |
|---|---|---|---|
| **PnL réel attribuable à ChatGPT** | historique utilisateur / décisions appariées | **NON MESURABLE** : pas de registre horodaté complet ChatGPT → exécution → issues / alternative Solaire | Instrumenter privé avant toute affirmation chiffrée |
| **V4 historique** | 2 112 scans, 903 729 observations, 134 trades théoriques | EV estimée par trade rempli : **−0,6871 €** ; politiques/cohortes mélangées, évaluation initiale 4h | Pas une métrique de portefeuille ni du jugement ChatGPT |
| **Sorties shadow : référence** | 75 cas mûrs à 4h | PnL net simulé **−104,56 €** ; 22/75 positifs | Aucune démonstration de rentabilité |
| **Sorties shadow : 1,4R** | mêmes 75 cas mûrs à 4h | PnL net simulé **−47,75 €**, soit **+56,81 € vs référence** ; 27/75 positifs | Intéressant uniquement à 4h ; ne pas extrapoler |
| **Sorties shadow : 1,5R / 1,6R** | mêmes 75 cas mûrs à 4h | **−76,30 € / −89,79 €** | Tous les scénarios restent négatifs |
| **Sorties 1,4R à 12h / 24h** | N=54 / 28 | Différentiel vs référence : **−15,74 € / −51,20 €** | Effet dépendant de l'horizon, pas de changement global |
| **Rejets et réentrées** | 1 024 évaluations à 4h ; 1 017 à 24h | 260 événements avec passage d'exécution, 170 entrées admissibles ; compter séparément épisodes indépendants | Exploiter contrefactuels et maturation, sans assimiler compteurs à des trades |
| **Réentrée confirmée** | 6 cas à 4h | 4/6 excursion favorable +5%, médiane close +5,10% | Échantillon trop petit ; poursuivre |
| **HUMAN SWING R2 clean-forward** | 2 snapshots ; 17 Top10 ; 5 HUMAN_REVIEW | **0 événement maturé 24h/7j** dans rapport OOS consulté ; verdict insuffisant | Ne pas affirmer supériorité |
| **HUMAN SWING R2 live shadow** | 2026-10-08 20:42 UTC | 325 actifs classés ; 95 exclus ; Top20 = 20 ; HUMAN_REVIEW = 6 | Données collectées, résultats maturés nécessaires |
| **Seuil structurel 5% vs 6% shadow** | dernier cycle consulté, 2 nouveaux événements | 0 avantage validé dans ce cycle ; suivi 5% séparé des achats | Ne pas modifier production |
| **Emerging liquidity shadow** | dernier cycle consulté, 6 signaux | Deux signaux à faible volume ; zéro PASS exécution à 100 € ou 250 € | Ne pas assimiler forte rotation globale à carnet Bitvavo rempli |

## Incidents de décision à réconcilier
1. **OGN** : signaux de machine et alertes d'achat antérieurs à la forte hausse ; vérifier recommandations exactes des SCAN, entrée exécutable, trajet stops/TP. `INSUFFICIENT_HISTORY` dans un test limité ne signifie pas absence de détection : la mémoire 72h a des traces antérieures.
2. **RLC** : multiples alertes validées ; comparer retour APRÈS chaque entrée et trajectoire stop/TP, jamais la hausse max cumulée.
3. **ZRC** : accélération observée et volume/capitalisation saillant mais spread/carnet Bitvavo différents des volumes globaux ; ne pas conclure « achetable » avant preuve de liquidité sur l'heure considérée.

Pour chacun, séparer `NON_DETECTÉ`, `DETECTÉ_MAIS_NON_ACHETABLE`, `ACHÈTE_PAR_SOLAIRE_REFUSÉ_PAR_CHATGPT`, `ACHETÉ`, `REJET_JUSTIFIÉ` et `DONNÉES_INSUFFISANTES`.

## Inventaire des shadows et des prochaines mesures
- `production_exit_policy_shadow_status.json` : PnL et comparaisons horizon par horizon.
- `production_rejection_shadow_status.json` : rejets/réentrées et évaluations mûres ; trier par raison et coût réel.
- `production_v21_range5_shadow_status.json` : 5% vs 6%, ne pas généraliser un seul cycle.
- `production_emerging_liquidity_shadow_status.json` : volume marché, spread, profondeur à 100/250 €, aller/retour.
- `decision_layer.json`, `candidate_memory.json`, `v5_report.json`, `market_control.json` : historique causal et traçabilité ; **un statut sans historique complet ne suffit pas**.
- `swing_selector_shadow.json` et `research/swing_selector_oos_latest.json` : R2 classement vs preuve clean-forward.

## Ce que le bilan suivant doit contenir
Pour chaque shadow : **date de début**, versions gelées, N événements indépendants, N maturés par horizon, nouveaux cas, taux TP et stop, MAE/MFE, PnL **net** si identifiable, différence appariée vs baseline, erreurs de qualité et degré de confiance ; sinon `NON_MESURABLE` + raison. Comparaison de valeur de ChatGPT obligatoire, mais étiquetée non mesurable tant que le journal privé n'existe pas.

**Décision actuelle :** aucune promotion en production sur la seule base de ces observations ; conserver priorité HUMAN SWING. Le bilan hebdomadaire est assuré par la tâche existante côté ChatGPT ; ce fichier ne garantit pas de livraison de notifications (paramètres du compte distincts).

## Sources versionnées
- [V4 historique](../evaluation.json)
- [Shadow sorties](../production_exit_policy_shadow_status.json)
- [Shadow rejets / réentrées](../production_rejection_shadow_status.json)
- [Shadow seuil 5%](../production_v21_range5_shadow_status.json)
- [Shadow liquidité](../production_emerging_liquidity_shadow_status.json)
- [R2 OOS](swing_selector_oos_latest.json)
- [R2 live shadow](../swing_selector_shadow.json)
