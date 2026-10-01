# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T20:21:54.927037+00:00
État : OK | marchés EUR : 430 | V4 : 380 | données valides : 430
Récupération : 2026-10-01T20:21:20.023360+00:00 | âge ticker : 148.6 s | durée : 150.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.44507 € ; score 92.40/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TRB-EUR : 18.929 € ; score 87.67/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AAVE-EUR : 151.15 € ; score 87.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 60.689 € ; score 85.49/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.21513 € ; score 84.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00063321 | +150.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5799 | +66.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.20336 | +40.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.105784 | +26.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0758957 | +25.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04551 | +23.63 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.52879 | +21.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.030569 | +18.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.42372 | +18.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.166596 | +18.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1930 scans ; 825978 observations ; 1493 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
