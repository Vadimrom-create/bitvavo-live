# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T01:47:31.159297+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T01:47:00.364020+00:00 | âge ticker : 150.6 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.111842 € ; score 93.87/100 ; SURVEILLE ; WICK_SETUP
- 2Z-EUR : 0.057947 € ; score 89.16/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- SUI-EUR : 1.02669 € ; score 88.62/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XVG-EUR : 0.0028186 € ; score 87.27/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.038635 € ; score 86.70/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.35957 | +40.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.126 | +35.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 244.465 | +31.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| POND-EUR | 0.0016227 | +31.32 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65619 | +29.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0052221 | +23.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.5625 | +18.39 % | DETECTED_EARLY | NONE | NONE |
| INIT-EUR | 0.090013 | +18.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.2978 | +17.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEW-EUR | 0.00047245 | +16.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1808 scans ; 773542 observations ; 1352 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
