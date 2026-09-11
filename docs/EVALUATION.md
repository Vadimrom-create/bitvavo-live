# Protocole fixé avant optimisation

Référence : source V4 du commit `ab25cdd5951448e6ac889bd1d1b8fd3defc93e12`, avec son état, ses sélections, ses règles d’entrée, son module HEI, sa réentrée et sa stabilisation. Score opportunity : maximum de deux chemins, `0,62 ignition + 0,23 tendance + 0,10 persistance + 0,05 liquidité` et `0,68 tendance + 0,18 ignition + 0,09 persistance + 0,05 liquidité`. Seuil achat 8,55 ; entrée 7,40 ; deux confirmations et filtres existants. La réentrée possède ses règles propres, conservées.

Les corrections de qualité des données et de risque sont une enveloppe de publication distincte. Le journal conserve à la fois la décision V4 non modifiée et la décision publiée. Les nouveaux diagnostics ne changent pas la baseline.

Horizons : +15m, +30m, +1h, +2h et +4h. Seuils : +5, +10, +15, +20, +30 et +40 %. Le résultat principal pré-enregistré est +5 % dans les quatre heures, avec au maximum -5 % d’excursion adverse avant le seuil. Les autres couples sont descriptifs ; choisir après coup celui qui favorise une version invaliderait une affirmation de supériorité.

Les mesures utilisent la première bougie 5m entière commençant après le scan, ce qui écarte jusqu’à cinq minutes initiales inconnues. Aucun haut/bas antérieur au signal n’est attribué au signal. Une séquence incomplète est censurée, jamais classée faussement négative. Les retours terminaux, MFE, MAE, délai d’atteinte et drawdown avant objectif sont conservés. L’ordre des événements à l’intérieur d’une bougie étant inconnu, le bas est réputé précéder le haut pour le calcul prudent du drawdown.

La matrice TP/FP/TN/FN s’applique à toutes les observations de marché, avec précision achat distincte. Elle n’affirme pas l’indépendance des observations qui se chevauchent. Les achats sont regroupés par épisodes espacés d’au moins quatre heures pour les statistiques de trades. Une absence de suivi antérieur à une hausse est `INSUFFICIENT_HISTORY` et non `FALSE_NEGATIVE`.

Le tableau de contrôle distingue le classement 24 h des accélérations de court terme. Le détecteur d’événement cherche une hausse de 5 % par rapport au plus bas de l’heure précédente et examine les états 15m/30m/1h/2h/4h avant son origine. Une détection utile précède cette origine d’au moins 15 minutes. La hausse résiduelle indiquée correspond au prix courant par rapport au prix du signal antérieur ; elle n’est ni une preuve de fill ni le résultat net d’un trade.

L’expected value est celle d’une simulation séparée : limit disponible pendant une bougie, quantité figée ex ante, stop structurel, sortie intégrale à TP1 ou à quatre heures, frais et slippage explicites. Un stop prévaut si stop et objectif sont touchés dans la même bougie. Les données OHLC ne reconstituent ni le carnet historique ni une exécution garantie. Aucune capitalisation ni optimisation du portefeuille n’est simulée.

## Comparaison V4 / V5

| Mesure | V4 | V5 |
|---|---|---|
| Recall utile | À mesurer sur événements mûrs | Pas de politique candidate optimisée |
| Précision ACHÈTE | À mesurer sur épisodes mûrs | Indisponible |
| Faux positifs / faux négatifs | Journal complet désormais disponible | Indisponible |
| Avance / hausse restante | Mesure chronologique progressive | Indisponible |
| MAE / MFE | Horizons complets requis | Indisponible |
| Expected value | Simulation ex ante, pas résultat de compte | Indisponible |
| TOO LATE | Décisions observées ; évitement profitable non démontré | Indisponible |
| Supériorité hors échantillon | Référence | Non démontrée |

Une V5 future doit être définie avant d’ouvrir le jeu de validation, rejouée sur les mêmes périodes et marchés, et comparée avec une séparation temporelle comportant un embargo supérieur à l’horizon maximal. Les sélections, versions du code, coûts et exclusions doivent être identiques ou explicitement attribués. Le nombre d’épisodes et l’incertitude sont indispensables ; un seul gagnant n’est pas une preuve. Aucune taille d’échantillon seule ne garantit une validation, notamment si les événements proviennent d’un même régime de marché.

## Phase 3 : contrats de mesure et portée

L'évaluation `HISTORY_CONTINUITY_V2` exige une séquence continue jusqu'à la bougie de franchissement incluse, avec clôture observée. Un trou, une bougie contradictoire ou une dernière bougie partielle ne confirme pas un événement court. Les anciens rapports restent dans leurs révisions/journaux ; un recalcul ne reprend pas leur identité d'évaluation.

`market_control_current.json` décrit uniquement la présence dans les listes publiées du cycle. `market_control_history.json` interroge toutes les observations de son namespace de données, sans plafond 50/40 ni sélection des vingt premiers marchés. Il conserve aussi la première détection historique connue. `market_control.json/.txt` restent des interfaces de compatibilité à portée courante explicite. Absence du top courant et absence historique sont distinctes.

Les namespaces `history`, `history_legacy_diagnostics` et `history_corrected` séparent données historiques, diagnostics corrigés sur V4 historique et acquisition corrigée. Les états corrigés commencent explicitement dans `policy_state/CORRECTED_INPUTS_V1` ; ils ne rajeunissent pas les anciens profils. Un horizon futur manquant est censuré. Des données décisionnelles manquantes avec un résultat positif observable restent comptabilisables dans le futur bilan end-to-end, sans devenir automatiquement un FN décisionnel conditionnel.

## Phase 3 — comparaison appariée versionnée

`research/comparison.py` et `scripts/run_comparison.py` enregistrent le cycle explicite et son hash, avant ses résultats futurs. Le snapshot contient la sortie V4 effectivement produite et les mêmes observations disponibles au cutoff pour V1/V2. Le statut de disponibilité de la publication commence à `UNKNOWN` ; un timestamp de replay ne le remplace jamais. Le lot de publication apporte ensuite un reçu immuable, sans réécrire le cycle.

Les comparaisons restent séparées par `data_policy`. Sans snapshots appariés réellement présents, le contraste d'entrées retourne `UNAVAILABLE`. Le masque G commun est la capacité structurelle vérifiable, indépendante du rang et du résultat. Les exigences d'entrée/exécution restent des capacités distinctes. La référence de prix est celle connue dans le snapshot ; la fenêtre future commence à la première bougie 5m entière après le cutoff, jamais à une heure antérieure de V4. Le prix peut être antérieur au cutoff : son horodatage et son âge restent dans la source. Les données arrivées après le cutoff sont rejetées.

Budget : trois candidats. Convention technique commune : disponibilité au cutoff + 120 s, résultat plus tardif indisponible. Cette convention n'est ni un seuil de trading ni une durée scientifiquement validée ; elle doit figurer dans le futur gel. Le chemin natif utilise la disponibilité de publication réellement observée. Le délai jusqu'à la première cible et sa lecture secondaire à au moins 15 minutes restent distincts d'une détection avant le début causal d'un mouvement, qui ne peut être inventée à partir d'OHLC.

Les épisodes sont ancrés sans futur par marché/setup, avec niveaux d'invalidation conservés depuis l'ancrage et borne descriptive de quatre heures. Un changement de setup documenté ou une invalidation structurelle observable peut en ouvrir un autre ; le glissement du support et une donnée temporairement manquante ne le font pas. Les marchés sans setup vérifiable restent des épisodes de population descriptifs, pas des trades ni des essais indépendants. Le même événement peut être détecté dans un scan ultérieur, sans déplacer sa référence. Les doublons et l'ordre d'ingestion ne multiplient pas les épisodes.

Les FN end-to-end sont décomposés exclusivement en données, décision et intégration. La métrique conditionnelle n'est pas additionnée aux FN globaux. Une publication inconnue donne des bornes, pas un succès/échec supposé. Les horizons immatures et trous futurs sont censurés ; leur marché, liquidité et catégorie sont conservés. Les fenêtres sans scan sont déclarées séparément ; leurs outcomes non observés restent inconnus. Les rapports comprennent transitions de buckets, rotation/rangs, MFE/MAE, paires individuelles et réservations de capital, sans intervalle de confiance prétendument validé.

Les plans utilisent le planificateur de risque existant, sont datés avant exécution et sont limités à un par politique/cycle. Aucun latent, support expérimental ou re-entry en attente ne devient un trade. Portefeuilles commun/native et politiques sont séparés. Une corrélation avec une position ouverte non revalidée bloque la proposition suivante ; une exécution ambiguë garde le capital réservé. Les coûts sont des hypothèses communes, pas les frais privés vérifiés. Le simulateur exclut la première bougie partielle, traite une simple mèche sous limite comme ambiguë, applique stop avant cible et gap défavorable, et ne libère pas optimistement une exposition incertaine. Aucun ordre n'est envoyé.
