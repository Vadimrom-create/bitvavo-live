# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T04:24:33.761085+00:00
État : OK | marchés EUR : 429 | V4 : 391 | données valides : 429
Récupération : 2026-09-30T04:23:57.704582+00:00 | âge ticker : 160.3 s | durée : 161.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.43683 € ; score 87.37/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.029544 € ; score 87.22/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.20579 € ; score 87.19/100 ; SURVEILLE ; seuil achat non atteint
- AZTEC-EUR : 0.015162 € ; score 85.83/100 ; SURVEILLE ; seuil achat non atteint
- KITE-EUR : 0.1206 € ; score 84.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.36135 | +37.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0017148 | +35.97 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.1294 | +35.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0024505 | +28.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00049391 | +20.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.614 | +18.98 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 251.198 | +18.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0050757 | +18.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.090534 | +17.24 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.29963 | +14.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1816 scans ; 776974 observations ; 1354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
