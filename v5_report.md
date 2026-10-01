# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T16:57:30.128045+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-01T16:56:57.726562+00:00 | âge ticker : 159.9 s | durée : 161.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TRX-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- INIT-EUR : 0.090666 € ; score 87.90/100 ; SURVEILLE ; SPREAD_RISK
- 0G-EUR : 0.26648 € ; score 87.82/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- IO-EUR : 0.14047 € ; score 86.71/100 ; SURVEILLE ; WICK_SETUP
- ENSO-EUR : 0.9064 € ; score 86.70/100 ; SURVEILLE ; seuil achat non atteint
- ARB-EUR : 0.17661 € ; score 84.64/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00061 | +135.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.8514 | +79.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0742954 | +27.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.18266 | +26.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04751 | +25.59 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.49967 | +23.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.176782 | +19.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.029269 | +16.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.0094 | +15.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.40946 | +15.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1920 scans ; 821678 observations ; 1485 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
