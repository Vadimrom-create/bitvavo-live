# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T23:47:09.958196+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-27T23:46:36.534110+00:00 | âge ticker : 154.0 s | durée : 154.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SENT-EUR : 0.01962 € ; score 92.28/100 ; SURVEILLE ; seuil achat non atteint
- NEO-EUR : 2.357 € ; score 90.39/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.74018 € ; score 89.97/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7961 € ; score 87.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AIXBT-EUR : 0.02252 € ; score 85.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 255.042 | +90.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.29486 | +44.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006744 | +30.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.031241 | +28.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.95262 | +22.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013835 | +20.40 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0044783 | +16.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.030329 | +15.87 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IMX-EUR | 0.16484 | +14.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.014895 | +13.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1657 scans ; 708907 observations ; 1206 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
