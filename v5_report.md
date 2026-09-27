# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T22:24:58.117799+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T22:24:29.276772+00:00 | âge ticker : 144.3 s | durée : 145.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MAGIC-EUR : 0.047756 € ; score 92.39/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AAVE-EUR : 135.29 € ; score 91.84/100 ; SURVEILLE ; seuil achat non atteint
- ETHFI-EUR : 0.62315 € ; score 88.32/100 ; SURVEILLE ; WICK_SETUP
- RE-EUR : 0.42706 € ; score 87.48/100 ; SURVEILLE ; STABILITY_HOLD
- JUP-EUR : 0.32637 € ; score 84.66/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 200.917 | +75.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28728 | +41.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006979 | +36.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.969 | +28.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030043 | +23.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013653 | +19.94 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0021509 | +17.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.015171 | +16.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006922 | +15.29 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0044289 | +15.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1651 scans ; 706345 observations ; 1186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
