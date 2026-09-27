# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T03:41:23.921505+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-09-27T03:40:52.861760+00:00 | âge ticker : 145.8 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LPT-EUR : 1.6 € ; score 93.06/100 ; SURVEILLE ; seuil achat non atteint
- ACU-EUR : 0.11958 € ; score 90.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- WLD-EUR : 0.46383 € ; score 89.31/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.4226 € ; score 88.80/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- IMX-EUR : 0.14762 € ; score 88.63/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 150.666 | +71.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.25171 | +41.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006249 | +39.46 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017229 | +30.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006337 | +22.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.060691 | +20.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.70527 | +20.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.5063 | +15.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.012296 | +14.41 % | DETECTED_EARLY | NONE | NONE |
| EDGE-EUR | 0.119742 | +13.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1585 scans ; 678163 observations ; 1073 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
