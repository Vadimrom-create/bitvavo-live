# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T17:28:39.377090+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T17:28:08.340900+00:00 | âge ticker : 148.8 s | durée : 149.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BONK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BONK-EUR : 3.2126e-06 € ; score 91.86/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : 0.07934 € ; score 90.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- W-EUR : 0.010365 € ; score 89.17/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AMP-EUR : 0.0004454 € ; score 88.89/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- DATAIP-EUR : 0.1947 € ; score 87.57/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021038 | +40.00 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.35159 | +34.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.46074 | +26.31 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 65.046 | +22.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10509 | +22.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.57499 | +20.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.036099 | +20.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 75.685 | +20.31 % | DETECTED_EARLY | NONE | NONE |
| ARX-EUR | 0.22917 | +19.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0162832 | +18.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1371 scans ; 586785 observations ; 731 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
