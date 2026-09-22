# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T07:49:37.918012+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T07:49:07.890024+00:00 | âge ticker : 153.9 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- JASMY-EUR : 0.0038396 € ; score 88.50/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- PORTAL-EUR : 0.017778 € ; score 87.52/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOGS-EUR : 4.4438e-05 € ; score 87.06/100 ; SURVEILLE ; seuil achat non atteint
- MANA-EUR : 0.0753 € ; score 85.27/100 ; SURVEILLE ; seuil achat non atteint
- ALIGN-EUR : 0.005945 € ; score 84.18/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017299 | +102.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.00154 | +98.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.120051 | +47.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.058175 | +43.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.486e-06 | +28.38 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21691 | +22.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39001 | +22.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.065697 | +19.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FARTCOIN-EUR | 0.17782 | +19.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.27364 | +19.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1163 scans ; 498175 observations ; 466 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
