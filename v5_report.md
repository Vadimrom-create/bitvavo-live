# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T08:14:19.095665+00:00
État : OK | marchés EUR : 426 | V4 : 377 | données valides : 426
Récupération : 2026-09-21T08:13:49.434494+00:00 | âge ticker : 148.0 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MERL-EUR : 0.023445 € ; score 94.09/100 ; SURVEILLE ; seuil achat non atteint
- PENDLE-EUR : 2.3323 € ; score 92.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 237.72 € ; score 92.50/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.016266 € ; score 91.78/100 ; SURVEILLE ; LOW_LIQUIDITY
- SOL-EUR : 98.266 € ; score 91.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056032 | +68.74 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009393 | +55.26 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.032971 | +36.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.24768 | +35.34 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.056688 | +32.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.029389 | +24.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 29.9629 | +24.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.50714 | +23.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.7127 | +20.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.049465 | +18.87 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1059 scans ; 453871 observations ; 330 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
