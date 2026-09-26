# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T18:58:59.701966+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T18:58:27.183016+00:00 | âge ticker : 148.5 s | durée : 149.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SNX-EUR : 0.23082 € ; score 93.57/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- LPT-EUR : 1.5523 € ; score 91.31/100 ; SURVEILLE ; seuil achat non atteint
- KAIA-EUR : 0.031161 € ; score 90.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SPK-EUR : 0.022721 € ; score 88.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SKY-EUR : 0.06761 € ; score 88.20/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00186 | +132.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006401 | +44.30 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.126 | +41.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019968 | +35.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.043935 | +21.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 104.922 | +21.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061167 | +19.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KAS-EUR | 0.043237 | +18.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006007 | +17.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.46816 | +15.85 % | DETECTED_EARLY | NONE | NONE |

Historique : 1554 scans ; 664926 observations ; 1023 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
