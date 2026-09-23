# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T19:17:31.217762+00:00
État : OK | marchés EUR : 426 | V4 : 410 | données valides : 426
Récupération : 2026-09-23T19:16:59.992379+00:00 | âge ticker : 146.4 s | durée : 147.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DATAIP-EUR : 0.1967 € ; score 87.50/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.013576 € ; score 84.76/100 ; SURVEILLE ; seuil achat non atteint
- SYN-EUR : 0.185642 € ; score 84.60/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 53.417 € ; score 83.45/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- THE-EUR : 0.06917 € ; score 81.91/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.045638 | +38.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.031321 | +26.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017861 | +23.92 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NIL-EUR | 0.087573 | +23.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.8325 | +18.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15451 | +15.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LIGHTER-EUR | 4.8008 | +13.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.30257 | +11.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3422 | +11.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACE-EUR | 0.16414 | +10.36 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1291 scans ; 552703 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
