# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T20:46:41.360336+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-29T20:46:13.272848+00:00 | âge ticker : 153.0 s | durée : 154.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DEEP-EUR : 0.019316 € ; score 90.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZIG-EUR : 0.046115 € ; score 89.87/100 ; SURVEILLE ; seuil achat non atteint
- LDO-EUR : 0.42203 € ; score 89.72/100 ; SURVEILLE ; seuil achat non atteint
- MMT-EUR : 0.16194 € ; score 89.51/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- ENA-EUR : 0.22223 € ; score 86.63/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017161 | +34.39 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65831 | +30.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.29209 | +22.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.35771 | +20.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021223 | +19.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 1.0085 | +17.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.005225 | +15.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0684 | +14.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FUEL-EUR | 0.000685 | +14.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.089045 | +13.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1792 scans ; 766678 observations ; 1339 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
