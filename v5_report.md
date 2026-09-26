# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T18:24:02.021765+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T18:23:28.661818+00:00 | âge ticker : 154.6 s | durée : 155.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ID-EUR : 0.03519 € ; score 87.37/100 ; SURVEILLE ; LOW_LIQUIDITY
- SUSHI-EUR : 0.23969 € ; score 86.27/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.0039182 € ; score 85.45/100 ; SURVEILLE ; seuil achat non atteint
- FLUX-EUR : 0.065173 € ; score 85.44/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.033201 € ; score 84.29/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00174 | +115.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020478 | +43.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.127 | +42.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006264 | +40.48 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 107.44 | +25.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062307 | +21.45 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.043939 | +21.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WELL-EUR | 0.00224 | +19.58 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AGI-EUR | 0.006032 | +18.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KAS-EUR | 0.042919 | +17.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1552 scans ; 664072 observations ; 1019 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
