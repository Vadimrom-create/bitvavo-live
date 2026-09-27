# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T23:32:49.485761+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-27T23:31:51.238108+00:00 | âge ticker : 176.2 s | durée : 177.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- FIL-EUR : 0.99631 € ; score 89.06/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.8046 € ; score 88.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.019474 € ; score 87.91/100 ; SURVEILLE ; seuil achat non atteint
- ZBT-EUR : 0.07836 € ; score 87.21/100 ; SURVEILLE ; LOW_LIQUIDITY
- TIA-EUR : 0.44461 € ; score 85.41/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 248.334 | +89.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.29679 | +43.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006823 | +32.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.03097 | +27.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.9587 | +23.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013814 | +20.22 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0044652 | +16.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.03028 | +15.27 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IMX-EUR | 0.16452 | +14.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.014917 | +12.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1656 scans ; 708480 observations ; 1206 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
