# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T11:19:51.175225+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-02T11:19:17.272475+00:00 | âge ticker : 159.9 s | durée : 161.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SYRUP-EUR : 0.21536 € ; score 88.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EPIC-EUR : 0.47437 € ; score 88.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ENS-EUR : 6.2863 € ; score 86.27/100 ; SURVEILLE ; seuil achat non atteint
- NOM-EUR : 0.0022533 € ; score 85.37/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- ETC-EUR : 8.1376 € ; score 84.26/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.05799 | +52.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.118175 | +33.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SWEAT-EUR | 0.0007 | +29.89 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CT-EUR | 0.52953 | +23.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.026583 | +18.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.092433 | +18.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MAGIC-EUR | 0.054271 | +16.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.012222 | +15.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.080455 | +14.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 165.61 | +13.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1975 scans ; 845328 observations ; 1557 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
