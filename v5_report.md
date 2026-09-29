# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T10:02:50.839197+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T10:02:19.479091+00:00 | âge ticker : 151.9 s | durée : 153.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ENA-EUR : 0.22317 € ; score 91.55/100 ; SURVEILLE ; WICK_SETUP
- LINEA-EUR : 0.0026066 € ; score 89.27/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, STABILITY_HOLD
- SKY-EUR : 0.072644 € ; score 88.37/100 ; SURVEILLE ; WICK_SETUP
- DIA-EUR : 0.14444 € ; score 87.38/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RED-EUR : 0.14268 € ; score 87.09/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019205 | +55.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 11.3459 | +28.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 232.195 | +23.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.61861 | +23.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.34898 | +21.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21804 | +20.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.2638 | +18.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVX-EUR | 2.0541 | +16.68 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.087368 | +15.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.30546 | +15.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1761 scans ; 753381 observations ; 1291 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
