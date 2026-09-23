# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T13:14:12.177386+00:00
État : OK | marchés EUR : 426 | V4 : 405 | données valides : 426
Récupération : 2026-09-23T13:13:43.261498+00:00 | âge ticker : 152.8 s | durée : 153.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VVV-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DATAIP-EUR : 0.1971 € ; score 91.22/100 ; SURVEILLE ; seuil achat non atteint
- KAT-EUR : 0.004433 € ; score 87.64/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- XDC-EUR : 0.027316 € ; score 87.45/100 ; SURVEILLE ; STABILITY_HOLD
- SYN-EUR : 0.191534 € ; score 86.26/100 ; SURVEILLE ; WICK_SETUP
- VVV-EUR : 27.9671 € ; score 85.97/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.036387 | +52.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.29671 | +30.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.33085 | +28.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.042751 | +27.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.020736 | +24.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16056 | +19.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.01699 | +17.95 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CHR-EUR | 0.018126 | +17.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| COTI-EUR | 0.01536 | +16.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.51399 | +15.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1271 scans ; 544183 observations ; 649 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
