# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T07:54:57.441318+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-28T07:54:25.814091+00:00 | âge ticker : 143.7 s | durée : 145.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GRAM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RED-EUR : 0.14169 € ; score 88.49/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK
- SENT-EUR : 0.018461 € ; score 86.46/100 ; SURVEILLE ; seuil achat non atteint
- APE-EUR : 0.14123 € ; score 85.97/100 ; SURVEILLE ; WICK_SETUP
- ACE-EUR : 0.16659 € ; score 85.65/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.024935 € ; score 85.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 238.793 | +60.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.0564 | +30.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.015683 | +19.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.027808 | +12.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.029594 | +10.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.004267 | +9.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016338 | +9.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28114 | +6.37 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| MON-EUR | 0.024935 | +6.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.20734 | +6.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1681 scans ; 719155 observations ; 1237 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
