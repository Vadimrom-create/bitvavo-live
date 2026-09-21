# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:10:01.323581+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T22:09:27.409148+00:00 | âge ticker : 152.8 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- THE-EUR : 0.07074 € ; score 90.97/100 ; SURVEILLE ; seuil achat non atteint
- MANTA-EUR : 0.061041 € ; score 89.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KSM-EUR : 4.0388 € ; score 89.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SKY-EUR : 0.062873 € ; score 88.78/100 ; SURVEILLE ; WICK_SETUP
- IO-EUR : 0.13139 € ; score 84.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015094 | +92.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.015853 | +84.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.0522 | +51.51 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.120688 | +47.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31425 | +39.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043871 | +34.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010659 | +34.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008599 | +32.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.02605 | +23.79 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PEPE-EUR | 4.2437e-06 | +22.49 % | DETECTED_EARLY | NONE | NONE |

Historique : 1123 scans ; 481135 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
