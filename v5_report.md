# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T06:00:30.744895+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T05:59:54.130148+00:00 | âge ticker : 160.3 s | durée : 161.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AUDIO-EUR : 0.01518 € ; score 90.16/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 62.343 € ; score 88.68/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BRETT-EUR : 0.0052906 € ; score 87.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TRB-EUR : 18.717 € ; score 87.82/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PENDLE-EUR : 2.154 € ; score 86.31/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00067055 | +158.00 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.131189 | +56.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.46442 | +33.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.028457 | +28.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04734 | +19.64 % | DETECTED_EARLY | NONE | NONE |
| ALICE-EUR | 0.16835 | +14.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20589 | +12.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.6809 | +11.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PONKE-EUR | 0.023239 | +11.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.50811 | +10.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1960 scans ; 838878 observations ; 1526 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
