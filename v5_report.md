# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T21:51:25.783816+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T21:50:53.783537+00:00 | âge ticker : 155.1 s | durée : 156.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ORCA-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- VIRTUAL-EUR : 0.72954 € ; score 93.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2068 € ; score 92.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WOO-EUR : 0.012503 € ; score 90.72/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- OP-EUR : 0.12913 € ; score 89.71/100 ; SURVEILLE ; seuil achat non atteint
- ARKM-EUR : 0.12486 € ; score 88.94/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 204.377 | +88.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28919 | +44.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006884 | +35.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030631 | +25.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013841 | +22.56 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.007099 | +18.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0044845 | +16.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.88226 | +16.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.5897 | +14.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22514 | +14.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1649 scans ; 705491 observations ; 1178 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
