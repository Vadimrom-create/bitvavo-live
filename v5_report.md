# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T02:01:39.714689+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T02:01:06.163052+00:00 | âge ticker : 146.3 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RECALL-EUR : 0.042831 € ; score 89.81/100 ; SURVEILLE ; WICK_SETUP
- BRETT-EUR : 0.0052484 € ; score 86.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LDO-EUR : 0.39677 € ; score 85.11/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 8.1194 € ; score 84.80/100 ; SURVEILLE ; seuil achat non atteint
- DYDX-EUR : 0.13358 € ; score 84.55/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.05912 | +48.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.006071 | +15.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023347 | +14.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENJ-EUR | 0.030741 | +14.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.48225 | +12.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.50123 | +10.59 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.54173 | +9.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.086899 | +9.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| APE-EUR | 0.14633 | +9.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UP-EUR | 0.065494 | +8.64 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2021 scans ; 864932 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
