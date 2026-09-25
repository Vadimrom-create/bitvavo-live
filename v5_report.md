# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T19:12:26.714126+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T19:11:50.451420+00:00 | âge ticker : 163.9 s | durée : 165.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LTC-EUR : 62.148 € ; score 93.87/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : 0.7543 € ; score 93.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TAO-EUR : 269.84 € ; score 92.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RPL-EUR : 1.8318 € ; score 91.30/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- EGLD-EUR : 4.0481 € ; score 90.31/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.074163 | +70.64 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WMTX-EUR | 0.0226 | +31.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.21308 | +31.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.49275 | +27.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014666 | +27.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.089966 | +22.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74951 | +20.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22575 | +17.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.062691 | +17.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 85.97 | +14.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1465 scans ; 626923 observations ; 880 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
