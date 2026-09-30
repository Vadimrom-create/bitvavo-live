# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T18:47:32.424822+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T18:46:51.603379+00:00 | âge ticker : 165.3 s | durée : 166.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XLM-EUR : 0.19923 € ; score 85.39/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TRB-EUR : 18.207 € ; score 82.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- STRK-EUR : 0.037337 € ; score 81.55/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.047176 € ; score 81.02/100 ; SURVEILLE ; SPREAD_RISK
- RED-EUR : 0.1563 € ; score 80.92/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5364 | +53.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34594 | +44.74 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.43749 | +23.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00812 | +21.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| UP-EUR | 0.07 | +14.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.068193 | +14.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MERL-EUR | 0.028832 | +14.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.36983 | +13.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020733 | +11.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOMI-EUR | 0.19625 | +11.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1856 scans ; 794158 observations ; 1416 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
