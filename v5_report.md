# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T21:01:51.685586+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T21:00:54.759938+00:00 | âge ticker : 174.1 s | durée : 175.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ROSE-EUR : 0.007957 € ; score 92.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.07089 € ; score 90.27/100 ; SURVEILLE ; WICK_SETUP
- MIOTA-EUR : 0.047516 € ; score 89.47/100 ; SURVEILLE ; WICK_SETUP
- NOS-EUR : 0.3933 € ; score 87.99/100 ; SURVEILLE ; WICK_SETUP
- TAIKO-EUR : 0.07952 € ; score 86.74/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016692 | +30.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.653 | +27.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0779 | +26.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021714 | +22.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.29168 | +20.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35417 | +18.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0051928 | +15.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0649 | +13.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.089393 | +13.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AAVE-EUR | 146.5 | +12.41 % | DETECTED_EARLY | NONE | NONE |

Historique : 1793 scans ; 767107 observations ; 1339 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
