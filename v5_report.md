# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T18:52:44.754378+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T18:52:11.165994+00:00 | âge ticker : 157.4 s | durée : 158.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ATH-EUR : 0.0048165 € ; score 91.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- COTI-EUR : 0.01505 € ; score 86.83/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 248.97 € ; score 82.92/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WCT-EUR : 0.036282 € ; score 82.63/100 ; SURVEILLE ; STABILITY_HOLD
- SUPER-EUR : 0.13019 € ; score 82.06/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0016942 | +120.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.015769 | +87.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053819 | +59.90 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31927 | +43.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.0445 | +39.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010248 | +29.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008251 | +26.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.326e-06 | +24.67 % | DETECTED_EARLY | NONE | NONE |
| AIOZ-EUR | 0.098101 | +23.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.256099 | +20.77 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1101 scans ; 471763 observations ; 401 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
