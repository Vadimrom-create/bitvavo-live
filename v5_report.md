# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T04:44:49.358212+00:00
État : OK | marchés EUR : 429 | V4 : 391 | données valides : 429
Récupération : 2026-09-30T04:44:19.265532+00:00 | âge ticker : 146.6 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.43767 € ; score 92.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- IMX-EUR : 0.14682 € ; score 90.39/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SPK-EUR : 0.020971 € ; score 88.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ALGO-EUR : 0.110879 € ; score 87.17/100 ; SURVEILLE ; seuil achat non atteint
- OP-EUR : 0.11526 € ; score 87.16/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.36987 | +41.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.123 | +34.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0017142 | +33.74 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0024241 | +29.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.6427 | +23.46 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 254.567 | +20.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00049196 | +20.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0050563 | +18.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.063379 | +17.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.090817 | +16.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1817 scans ; 777403 observations ; 1354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
