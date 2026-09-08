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
