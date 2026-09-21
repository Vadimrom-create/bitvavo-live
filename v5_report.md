# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T16:40:45.317278+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-21T16:40:11.426923+00:00 | âge ticker : 154.8 s | durée : 156.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- API3-EUR : 0.22714 € ; score 88.24/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- IOST-EUR : 0.0007829 € ; score 88.03/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- HOT-EUR : 0.00036671 € ; score 84.84/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KAS-EUR : 0.037276 € ; score 83.98/100 ; SURVEILLE ; WICK_SETUP
- GMT-EUR : 0.007197 € ; score 82.17/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0031564 | +306.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.031 | +267.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.052083 | +55.78 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.043269 | +38.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30739 | +37.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008326 | +28.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.000955 | +24.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.032935 | +24.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.055785 | +24.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.097111 | +23.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1090 scans ; 467077 observations ; 392 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
