# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T12:20:20.006947+00:00
État : OK | marchés EUR : 426 | V4 : 357 | données valides : 426
Récupération : 2026-10-04T12:19:10.924164+00:00 | âge ticker : 190.9 s | durée : 191.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUID-EUR : 1.5289 € ; score 79.91/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.082446 € ; score 78.61/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 159.66 € ; score 77.15/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NMR-EUR : 10.7719 € ; score 77.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- C-EUR : 0.091715 € ; score 76.47/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BEAM-EUR | 0.0024848 | +33.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TREAD-EUR | 1.05197 | +31.03 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.049173 | +25.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.111666 | +23.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.62243 | +19.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0023642 | +15.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BAT-EUR | 0.09602 | +14.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AXS-EUR | 1.2227 | +13.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FUN-EUR | 0.017516 | +13.44 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AKT-EUR | 0.66028 | +12.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2052 scans ; 878138 observations ; 1628 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
