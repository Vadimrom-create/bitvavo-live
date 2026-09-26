# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T21:52:04.154632+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T21:51:04.329294+00:00 | âge ticker : 188.8 s | durée : 190.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- VVV-EUR : 26.04 € ; score 91.58/100 ; SURVEILLE ; WICK_SETUP
- USELESS-EUR : 0.254 € ; score 90.28/100 ; SURVEILLE ; WICK_SETUP
- RAY-EUR : 1.82317 € ; score 89.76/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LIGHTER-EUR : 4.2871 € ; score 87.57/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.023258 € ; score 86.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00174 | +115.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006917 | +55.93 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.126588 | +46.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019013 | +35.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 108.183 | +26.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.06274 | +22.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.044011 | +20.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006 | +18.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.66632 | +17.67 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TREAD-EUR | 0.757 | +15.62 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1565 scans ; 669623 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
