# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T12:55:02.556149+00:00
État : OK | marchés EUR : 426 | V4 : 405 | données valides : 426
Récupération : 2026-09-23T12:54:30.789882+00:00 | âge ticker : 152.0 s | durée : 153.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- AVNT-EUR : 0.10231 € ; score 92.37/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.6195 € ; score 90.91/100 ; SURVEILLE ; WIDE_SPREAD_RISK, STABILITY_HOLD
- SYN-EUR : 0.194053 € ; score 87.93/100 ; SURVEILLE ; seuil achat non atteint
- SOMI-EUR : 0.17111 € ; score 82.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RSR-EUR : 0.0015172 € ; score 82.45/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.034424 | +43.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.300302 | +32.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.33515 | +30.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.043704 | +29.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.018972 | +23.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SENT-EUR | 0.02047 | +23.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.085223 | +20.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.159 | +19.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.286 | +19.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 310.46 | +18.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1270 scans ; 543757 observations ; 648 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
