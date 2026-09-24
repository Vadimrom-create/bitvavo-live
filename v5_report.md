# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T17:45:31.162980+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-24T17:44:58.274098+00:00 | âge ticker : 150.4 s | durée : 151.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAIKO-EUR : 0.07931 € ; score 91.82/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : 0.045346 € ; score 91.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034993 € ; score 90.17/100 ; SURVEILLE ; seuil achat non atteint
- PENDLE-EUR : 2.2286 € ; score 89.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- DATAIP-EUR : 0.1946 € ; score 88.10/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0098927 | +43.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0020666 | +38.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.35304 | +34.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45886 | +25.58 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.036346 | +21.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.102698 | +20.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LTC-EUR | 64.219 | +20.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22972 | +19.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.5725 | +19.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 74.55 | +18.16 % | DETECTED_EARLY | NONE | NONE |

Historique : 1372 scans ; 587212 observations ; 738 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
