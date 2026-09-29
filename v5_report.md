# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T19:31:35.422379+00:00
État : OK | marchés EUR : 429 | V4 : 394 | données valides : 429
Récupération : 2026-09-29T19:31:05.015085+00:00 | âge ticker : 152.2 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUI-EUR : 1.01658 € ; score 90.75/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012492 € ; score 89.76/100 ; SURVEILLE ; seuil achat non atteint
- FLR-EUR : 0.0065 € ; score 89.76/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.71493 € ; score 87.63/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.45301 € ; score 87.55/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016607 | +32.11 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.63066 | +23.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35856 | +23.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021374 | +22.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.28661 | +21.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0126 | +20.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0052673 | +16.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.14884 | +15.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 11.445 | +14.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.060078 | +14.95 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1788 scans ; 764962 observations ; 1338 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
