# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T17:19:15.986802+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-01T17:18:44.836843+00:00 | âge ticker : 151.2 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KSM-EUR : 4.5862 € ; score 86.32/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- WAL-EUR : 0.030245 € ; score 86.17/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.049075 € ; score 85.99/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- JUP-EUR : 0.2846 € ; score 85.94/100 ; SURVEILLE ; seuil achat non atteint
- STX-EUR : 0.3421 € ; score 85.70/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00056481 | +116.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6509 | +83.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0773591 | +32.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04782 | +27.38 % | DETECTED_EARLY | NONE | NONE |
| ALICE-EUR | 0.18218 | +25.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.42236 | +21.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.49137 | +21.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.030274 | +20.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.009605 | +17.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.171992 | +17.67 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1921 scans ; 822108 observations ; 1485 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
