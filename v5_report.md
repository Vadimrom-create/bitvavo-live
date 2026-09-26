# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T19:32:23.536513+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T19:31:52.064720+00:00 | âge ticker : 154.0 s | durée : 155.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NPC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ACH-EUR : 0.0055585 € ; score 91.75/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- ALICE-EUR : 0.14196 € ; score 91.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WCT-EUR : 0.038477 € ; score 91.31/100 ; SURVEILLE ; seuil achat non atteint
- MAVIA-EUR : 0.03181 € ; score 90.03/100 ; SURVEILLE ; seuil achat non atteint
- EDEN-EUR : 0.054235 € ; score 87.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017095 | +112.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.123464 | +40.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006205 | +39.88 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.02034 | +39.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 108.55 | +26.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062537 | +21.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.043962 | +21.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KAS-EUR | 0.043146 | +17.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006021 | +17.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.65479 | +15.14 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1556 scans ; 665780 observations ; 1036 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
