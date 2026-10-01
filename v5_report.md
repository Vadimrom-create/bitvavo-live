# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T20:43:09.200525+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T20:42:11.420190+00:00 | âge ticker : 177.2 s | durée : 177.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 151.17 € ; score 95.14/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.44549 € ; score 93.99/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012284 € ; score 91.74/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : 0.0020439 € ; score 90.74/100 ; SURVEILLE ; WICK_SETUP
- TRB-EUR : 18.95 € ; score 90.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00064569 | +155.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5705 | +60.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.20422 | +40.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.112919 | +35.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0761002 | +23.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04545 | +23.40 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.52175 | +20.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.42226 | +18.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVE-EUR | 0.009367 | +18.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0023821 | +18.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1931 scans ; 826408 observations ; 1493 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
