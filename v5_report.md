# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T08:16:57.111881+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-02T08:16:25.090301+00:00 | âge ticker : 146.9 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BABY-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUID-EUR : 1.4062 € ; score 90.43/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- STRK-EUR : 0.038781 € ; score 90.01/100 ; SURVEILLE ; STABILITY_HOLD
- ICP-EUR : 2.9255 € ; score 88.18/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HOT-EUR : 0.00041357 € ; score 87.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SUI-EUR : 1.05659 € ; score 87.64/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00068749 | +165.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.53402 | +43.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAND-EUR | 0.052873 | +36.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.113894 | +30.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.02625 | +15.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.089991 | +14.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.20114 | +13.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.01192 | +11.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AAVE-EUR | 162.34 | +11.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.6443 | +11.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1966 scans ; 841458 observations ; 1542 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
