# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T04:03:06.933565+00:00
État : OK | marchés EUR : 430 | V4 : 388 | données valides : 430
Récupération : 2026-10-02T04:02:35.561098+00:00 | âge ticker : 150.0 s | durée : 150.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 156.89 € ; score 93.15/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- NMR-EUR : 10.2915 € ; score 91.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 61.156 € ; score 88.68/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.23133 € ; score 88.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.9869e-06 € ; score 88.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00065 | +152.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.140959 | +67.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.030736 | +41.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.44663 | +28.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04696 | +19.89 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.166453 | +19.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.17205 | +16.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20894 | +16.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TOWNS-EUR | 0.0021109 | +13.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.51405 | +12.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1954 scans ; 836298 observations ; 1518 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
