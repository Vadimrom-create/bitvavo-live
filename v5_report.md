# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:48:29.181089+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T20:47:57.311755+00:00 | âge ticker : 150.4 s | durée : 151.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BEAM-EUR : 0.001776 € ; score 93.96/100 ; SURVEILLE ; SPREAD_RISK
- ACE-EUR : 0.15976 € ; score 89.17/100 ; SURVEILLE ; seuil achat non atteint
- TRAC-EUR : 0.32456 € ; score 87.82/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- ZIG-EUR : 0.045972 € ; score 84.54/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- TRUMP-EUR : 1.8577 € ; score 83.93/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.39971 | +38.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0094479 | +37.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.59948 | +32.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44972 | +24.41 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 76.349 | +22.87 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.095 | +21.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.036994 | +20.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16713 | +20.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0019813 | +19.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PLUME-EUR | 0.0162745 | +18.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1388 scans ; 594044 observations ; 759 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
