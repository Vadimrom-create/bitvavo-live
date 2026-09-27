# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T21:37:31.754740+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T21:37:00.248078+00:00 | âge ticker : 145.6 s | durée : 146.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ATH-EUR : 0.0056274 € ; score 93.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 62.378 € ; score 93.29/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2068 € ; score 92.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.31467 € ; score 91.73/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0056152 € ; score 90.10/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 199.188 | +83.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.29013 | +40.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.00678 | +32.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.02977 | +22.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013774 | +21.90 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.90003 | +20.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.007099 | +18.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.59494 | +16.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0044467 | +14.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 4.892 | +12.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1648 scans ; 705064 observations ; 1176 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
