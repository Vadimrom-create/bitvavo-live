# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T06:48:42.977720+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T06:47:43.782681+00:00 | âge ticker : 175.4 s | durée : 176.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KAS-EUR : 0.038021 € ; score 92.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : 0.00778 € ; score 91.90/100 ; SURVEILLE ; LOW_LIQUIDITY
- ROSE-EUR : 0.007479 € ; score 91.44/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- FIL-EUR : 0.9496 € ; score 90.48/100 ; SURVEILLE ; seuil achat non atteint
- MOODENG-EUR : 0.04347 € ; score 90.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00155 | +98.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017266 | +49.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.25082 | +44.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.068403 | +40.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.060428 | +27.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AERO-EUR | 0.7957 | +26.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.2342 | +21.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0040144 | +17.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.12036 | +17.41 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KMNO-EUR | 0.03803 | +16.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1510 scans ; 646138 observations ; 955 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
