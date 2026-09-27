# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T00:48:10.786477+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-27T00:47:37.366193+00:00 | âge ticker : 149.9 s | durée : 150.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- TNSR-EUR : 0.036357 € ; score 93.55/100 ; SURVEILLE ; WICK_SETUP
- KAIA-EUR : 0.032261 € ; score 87.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WAL-EUR : 0.03245 € ; score 86.81/100 ; SURVEILLE ; WICK_SETUP
- RENDER-EUR : 1.75 € ; score 84.08/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.12598 € ; score 83.41/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 138.32 | +60.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006973 | +57.19 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019567 | +47.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.007109 | +28.69 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| 2Z-EUR | 0.061379 | +21.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.68355 | +19.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KMNO-EUR | 0.042628 | +16.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| COW-EUR | 0.15301 | +15.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.00597 | +15.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.81402 | +14.79 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1575 scans ; 673893 observations ; 1058 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
