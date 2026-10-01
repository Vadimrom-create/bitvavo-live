# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T03:20:44.265417+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-10-01T03:20:12.039089+00:00 | âge ticker : 150.9 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- STRK-EUR : 0.038906 € ; score 89.62/100 ; SURVEILLE ; seuil achat non atteint
- KMNO-EUR : 0.038765 € ; score 87.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ICP-EUR : 2.9967 € ; score 85.52/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.7361 € ; score 84.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.092623 € ; score 84.12/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.1139 | +91.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34233 | +43.23 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.43694 | +28.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008533 | +27.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33641 | +22.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028723 | +22.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0183205 | +17.82 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.0623475 | +16.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.47331 | +16.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0021173 | +15.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1882 scans ; 805338 observations ; 1438 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
