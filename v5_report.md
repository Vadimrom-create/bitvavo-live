# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T21:01:42.145064+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T21:01:12.552113+00:00 | âge ticker : 147.6 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- BIGTIME-EUR : 0.008479 € ; score 93.92/100 ; SURVEILLE ; seuil achat non atteint
- OP-EUR : 0.12772 € ; score 93.64/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.012409 € ; score 91.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SNX-EUR : 0.23469 € ; score 90.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BAT-EUR : 0.08451 € ; score 86.66/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 172.175 | +62.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.2846 | +43.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006688 | +30.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013681 | +22.80 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.885 | +21.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.028365 | +17.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.015272 | +15.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0043958 | +15.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00703 | +15.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 4.7938 | +14.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1646 scans ; 704210 observations ; 1171 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
