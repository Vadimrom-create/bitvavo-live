# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T06:01:50.006350+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T06:01:18.909137+00:00 | âge ticker : 144.2 s | durée : 145.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BABY-EUR : 0.011903 € ; score 89.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TRB-EUR : 17.545 € ; score 88.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DUSK-EUR : 0.078168 € ; score 88.46/100 ; SURVEILLE ; seuil achat non atteint
- RLC-EUR : 0.31861 € ; score 86.94/100 ; SURVEILLE ; SPREAD_RISK
- MOODENG-EUR : 0.043112 € ; score 86.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016869 | +116.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.075806 | +62.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.23872 | +38.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.78718 | +24.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013993 | +22.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.2362 | +21.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.103365 | +19.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.037552 | +16.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.033587 | +16.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.064192 | +16.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1508 scans ; 645284 observations ; 954 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
