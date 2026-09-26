# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T14:10:31.659106+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T14:10:02.306481+00:00 | âge ticker : 146.1 s | durée : 146.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AXS-EUR : 1.0405 € ; score 93.24/100 ; SURVEILLE ; seuil achat non atteint
- OP-EUR : 0.13094 € ; score 92.00/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOVR-EUR : 0.8982 € ; score 89.57/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- APT-EUR : 0.7543 € ; score 89.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ESP-EUR : 0.091301 € ; score 87.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020828 | +153.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.021693 | +83.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.124999 | +48.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.064874 | +32.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AMP-EUR | 0.0005671 | +28.36 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.24065 | +24.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.042393 | +16.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.64443 | +15.67 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PROM-EUR | 5.4793 | +15.60 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| QNT-EUR | 93.52 | +14.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1537 scans ; 657667 observations ; 992 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
