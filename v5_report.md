# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T22:40:44.667941+00:00
État : OK | marchés EUR : 428 | V4 : 400 | données valides : 428
Récupération : 2026-09-28T22:40:09.617045+00:00 | âge ticker : 154.8 s | durée : 155.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.071134 € ; score 92.70/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.011672 € ; score 88.47/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CELR-EUR : 0.0025893 € ; score 85.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- 0G-EUR : 0.24105 € ; score 83.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TRUST-EUR : 0.054003 € ; score 83.17/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.25 | +37.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.10905 | +32.04 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.118746 | +14.95 % | DETECTED_EARLY | NONE | NONE |
| MIOTA-EUR | 0.04918 | +11.22 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0018131 | +9.13 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.2981 | +8.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016389 | +6.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22602 | +5.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.30208 | +5.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.049574 | +5.63 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1726 scans ; 738401 observations ; 1269 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
