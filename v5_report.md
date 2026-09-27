# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T23:16:00.869233+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T23:15:24.429252+00:00 | âge ticker : 161.8 s | durée : 162.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ACE-EUR : 0.17081 € ; score 87.52/100 ; SURVEILLE ; seuil achat non atteint
- FLR-EUR : 0.0062826 € ; score 87.25/100 ; SURVEILLE ; seuil achat non atteint
- AIXBT-EUR : 0.022714 € ; score 85.93/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SNX-EUR : 0.2377 € ; score 85.77/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- MOVR-EUR : 0.9477 € ; score 85.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 265.28 | +104.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.29482 | +43.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.00677 | +31.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.0309 | +27.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.92491 | +22.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013612 | +18.46 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.004486 | +16.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16399 | +13.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.014928 | +13.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006839 | +12.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1655 scans ; 708053 observations ; 1202 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
