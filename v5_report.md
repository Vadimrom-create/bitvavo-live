# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T08:30:28.392736+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-22T08:29:29.877852+00:00 | âge ticker : 175.0 s | durée : 175.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HYPE-EUR : 82.509 € ; score 89.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.86514 € ; score 87.89/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.0426 € ; score 87.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ESP-EUR : 0.083055 € ; score 84.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BCH-EUR : 233.06 € ; score 84.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.018478 | +114.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014799 | +88.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.120722 | +46.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057262 | +38.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39678 | +24.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3936e-06 | +23.86 % | DETECTED_EARLY | NONE | NONE |
| USELESS-EUR | 0.259614 | +21.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21757 | +21.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CARV-EUR | 0.040242 | +17.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FORM-EUR | 0.27135 | +17.58 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1167 scans ; 499879 observations ; 469 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
