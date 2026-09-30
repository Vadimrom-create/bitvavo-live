# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T08:18:16.222134+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T08:17:45.007119+00:00 | âge ticker : 150.5 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BABY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PLUME-EUR : 0.016035 € ; score 90.16/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.11211 € ; score 87.73/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 3.0554 € ; score 85.00/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- API3-EUR : 0.25133 € ; score 84.18/100 ; SURVEILLE ; WICK_SETUP
- WOO-EUR : 0.01216 € ; score 84.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.497 | +72.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.103134 | +34.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.38644 | +31.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.00822 | +22.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GNS-EUR | 0.49171 | +16.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0022132 | +14.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.3017 | +14.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEW-EUR | 0.00048059 | +14.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0050332 | +13.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.5602 | +13.39 % | DETECTED_EARLY | NONE | NONE |

Historique : 1827 scans ; 781693 observations ; 1363 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
