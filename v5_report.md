# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T02:47:51.016716+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T02:47:18.155097+00:00 | âge ticker : 149.1 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FIL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.29986 € ; score 93.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TNSR-EUR : 0.035876 € ; score 93.06/100 ; SURVEILLE ; seuil achat non atteint
- AKT-EUR : 0.61587 € ; score 92.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FIL-EUR : 1.00446 € ; score 90.17/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZIL-EUR : 0.0032869 € ; score 89.24/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 147.383 | +67.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006216 | +38.72 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.24056 | +36.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.01718 | +28.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.0065 | +24.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.061462 | +20.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.69847 | +20.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.042106 | +14.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.120037 | +14.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.84 | +13.94 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1582 scans ; 676882 observations ; 1068 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
