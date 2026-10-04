# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T13:26:22.215527+00:00
État : OK | marchés EUR : 426 | V4 : 356 | données valides : 426
Récupération : 2026-10-04T13:25:51.687773+00:00 | âge ticker : 151.3 s | durée : 153.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MANA-EUR : 0.095984 € ; score 92.17/100 ; SURVEILLE ; WICK_SETUP
- KSM-EUR : 4.6937 € ; score 91.46/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ILV-EUR : 3.8324 € ; score 90.28/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- PLUME-EUR : 0.0165943 € ; score 86.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- FLUID-EUR : 1.5471 € ; score 86.23/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BEAM-EUR | 0.0024097 | +29.29 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TREAD-EUR | 1.05796 | +29.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.049048 | +24.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.113063 | +24.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.61134 | +16.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AKT-EUR | 0.66849 | +14.63 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AXS-EUR | 1.2229 | +14.00 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FUN-EUR | 0.017521 | +13.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0023384 | +13.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BAT-EUR | 0.09481 | +12.71 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2056 scans ; 879842 observations ; 1629 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
