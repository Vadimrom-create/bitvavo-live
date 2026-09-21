# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T21:58:05.572295+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T21:57:35.493723+00:00 | âge ticker : 145.3 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.054638 € ; score 91.07/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0016568 € ; score 89.32/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0051688 € ; score 89.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAITO-EUR : 0.29982 € ; score 88.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- THE-EUR : 0.07074 € ; score 85.74/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015001 | +91.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0162 | +88.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.05211 | +51.25 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SWELL-EUR | 0.0009372 | +44.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.31492 | +40.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.108937 | +36.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.043461 | +34.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010713 | +32.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.38878 | +23.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUFFER-EUR | 0.025882 | +23.12 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1122 scans ; 480709 observations ; 405 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
