# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T04:17:37.057767+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T04:16:42.058802+00:00 | âge ticker : 173.4 s | durée : 174.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MOVR-EUR : 0.8679 € ; score 92.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HUMA-EUR : 0.025676 € ; score 91.98/100 ; SURVEILLE ; WICK_SETUP
- JUP-EUR : 0.30173 € ; score 91.81/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RLC-EUR : 0.31688 € ; score 89.61/100 ; SURVEILLE ; SPREAD_RISK
- SCR-EUR : 0.022394 € ; score 89.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 157 | +80.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.26152 | +45.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006292 | +40.42 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017013 | +26.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.71745 | +22.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006241 | +20.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRC-EUR | 0.0012534 | +19.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.060019 | +19.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GLMR-EUR | 0.006822 | +17.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.50847 | +15.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1587 scans ; 679017 observations ; 1078 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
