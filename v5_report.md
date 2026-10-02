# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T14:09:46.227712+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 426
Récupération : 2026-10-02T14:08:51.665487+00:00 | âge ticker : 180.3 s | durée : 182.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MEGA-EUR : 0.04367 € ; score 89.96/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 62.67 € ; score 88.56/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TRB-EUR : 18.257 € ; score 87.92/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- SYRUP-EUR : 0.22098 € ; score 87.52/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.45e-06 € ; score 87.16/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.06 | +58.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.110877 | +27.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.1575 | +20.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.030345 | +18.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.09139 | +17.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GALA-EUR | 0.002342 | +17.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.53997 | +17.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.081728 | +16.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.7262 | +16.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BAT-EUR | 0.08991 | +15.92 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1983 scans ; 848744 observations ; 1567 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
