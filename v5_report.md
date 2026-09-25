# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T22:19:32.121819+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T22:18:59.062334+00:00 | âge ticker : 157.1 s | durée : 158.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUX-EUR : 0.061045 € ; score 92.50/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- CHIP-EUR : 0.043616 € ; score 91.02/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.2007 € ; score 90.13/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- S-EUR : 0.03602 € ; score 89.68/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- KITE-EUR : 0.11592 € ; score 87.25/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.085744 | +91.12 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21056 | +24.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.74297 | +22.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013828 | +21.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.065783 | +20.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.232 | +19.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 1.04736 | +18.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DEEP-EUR | 0.02042 | +17.95 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.45555 | +16.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JTO-EUR | 0.50044 | +16.29 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1477 scans ; 632047 observations ; 893 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
