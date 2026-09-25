# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T21:44:41.460257+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T21:44:06.509739+00:00 | âge ticker : 151.3 s | durée : 152.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BONK-EUR : 3.2074e-06 € ; score 91.89/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.064662 € ; score 87.42/100 ; SURVEILLE ; WICK_SETUP
- MOVR-EUR : 0.8578 € ; score 87.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WAL-EUR : 0.032489 € ; score 83.67/100 ; SURVEILLE ; WICK_SETUP
- OP-EUR : 0.1237 € ; score 82.54/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.075484 | +69.12 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21261 | +26.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014142 | +23.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.74458 | +21.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.45356 | +17.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22885 | +16.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.064026 | +16.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.65744 | +16.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.086852 | +15.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DEEP-EUR | 0.020036 | +15.73 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1474 scans ; 630766 observations ; 888 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
