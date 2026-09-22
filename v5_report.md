# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T05:32:23.091223+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T05:31:49.802149+00:00 | âge ticker : 154.5 s | durée : 155.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PORTAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AXL-EUR : 0.045139 € ; score 91.18/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- PORTAL-EUR : 0.017623 € ; score 88.50/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.02419 € ; score 87.95/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- SSV-EUR : 2.8436 € ; score 84.27/100 ; SURVEILLE ; WICK_SETUP
- ETHFI-EUR : 0.60209 € ; score 82.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015586 | +100.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.016727 | +92.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.127301 | +60.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.045521 | +33.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056689 | +28.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3462e-06 | +24.16 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.38153 | +20.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.26955 | +19.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.035466 | +17.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SWELL-EUR | 0.0007771 | +17.85 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1152 scans ; 493489 observations ; 460 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
