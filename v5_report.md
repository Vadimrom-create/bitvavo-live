# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T21:58:36.919284+00:00
État : OK | marchés EUR : 430 | V4 : 380 | données valides : 430
Récupération : 2026-10-01T21:58:02.444867+00:00 | âge ticker : 157.2 s | durée : 158.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JASMY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.8984 € ; score 89.66/100 ; SURVEILLE ; seuil achat non atteint
- OGN-EUR : 0.018603 € ; score 88.17/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK
- DYDX-EUR : 0.13395 € ; score 85.18/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.1939 € ; score 84.25/100 ; SURVEILLE ; WICK_SETUP
- AVAX-EUR : 9.7117 € ; score 84.16/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00071699 | +180.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.12636 | +53.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.545 | +37.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.19443 | +32.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04621 | +26.29 % | DETECTED_EARLY | NONE | NONE |
| SCR-EUR | 0.026361 | +25.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.42433 | +22.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.163151 | +17.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.50172 | +16.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0024091 | +16.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1935 scans ; 828128 observations ; 1501 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
