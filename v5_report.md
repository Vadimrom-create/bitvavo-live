# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T22:16:52.991610+00:00
État : OK | marchés EUR : 429 | V4 : 395 | données valides : 429
Récupération : 2026-09-29T22:16:20.664229+00:00 | âge ticker : 148.8 s | durée : 149.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RAY-EUR : 1.65571 € ; score 88.18/100 ; SURVEILLE ; seuil achat non atteint
- PENGU-EUR : 0.0088209 € ; score 86.80/100 ; SURVEILLE ; WICK_SETUP
- ARB-EUR : 0.18286 € ; score 86.37/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.012417 € ; score 84.33/100 ; SURVEILLE ; WICK_SETUP
- ROSE-EUR : 0.007994 € ; score 84.12/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017299 | +33.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.66382 | +30.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0439 | +23.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.002176 | +22.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.063533 | +21.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.29171 | +21.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35936 | +18.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0051312 | +18.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FUEL-EUR | 0.0006708 | +15.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDP-EUR | 0.02165 | +15.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1797 scans ; 768823 observations ; 1339 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
