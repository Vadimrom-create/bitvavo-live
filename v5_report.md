# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T00:27:47.203138+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T00:27:15.569466+00:00 | âge ticker : 155.2 s | durée : 156.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- MEGA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUPER-EUR : 0.13296 € ; score 91.42/100 ; SURVEILLE ; seuil achat non atteint
- TAIKO-EUR : 0.08188 € ; score 89.12/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0038631 € ; score 88.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : 5.3154e-06 € ; score 85.76/100 ; SURVEILLE ; WICK_SETUP
- MOVR-EUR : 0.788 € ; score 85.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0174 | +102.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014134 | +80.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.124278 | +54.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.050924 | +47.81 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SWELL-EUR | 0.0009002 | +40.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0011184 | +36.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.31027 | +36.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043502 | +32.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUFFER-EUR | 0.026162 | +23.55 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PEPE-EUR | 4.3024e-06 | +21.24 % | DETECTED_EARLY | NONE | NONE |

Historique : 1134 scans ; 485821 observations ; 422 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
