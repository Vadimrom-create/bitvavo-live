# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T15:16:58.339178+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-01T15:16:25.387002+00:00 | âge ticker : 150.8 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MMT-EUR : 0.16305 € ; score 89.74/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- CC-EUR : 0.10843 € ; score 86.64/100 ; SURVEILLE ; seuil achat non atteint
- ILV-EUR : 3.3764 € ; score 86.13/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- ETC-EUR : 7.8148 € ; score 85.11/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 147.36 € ; score 83.27/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00046972 | +79.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.2399 | +52.15 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ALICE-EUR | 0.20592 | +43.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.074562 | +31.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.40399 | +23.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SYN-EUR | 0.174934 | +19.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.47812 | +19.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.028511 | +17.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.40398 | +13.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33863 | +12.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1915 scans ; 819528 observations ; 1479 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
