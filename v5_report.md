# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T23:02:22.874844+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 30
Récupération : 2026-09-19T23:01:19.778363+00:00 | âge ticker : 180.9 s | durée : 181.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 31/427 ; 15 min 75/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : INVALID_5M
- STRK-EUR : CHASE_RISK, INVALID_5M
- STX-EUR : STABILITY_HOLD, INVALID_5M

## SURVEILLE

- PEPE-EUR : 3.5751e-06 € ; score 82.44/100 ; SURVEILLE ; WICK_SETUP
- ONDO-EUR : 0.3663 € ; score 81.25/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.75105 € ; score 79.89/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 79.586 € ; score 79.64/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 230.44 € ; score 77.29/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.00316 | +58.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.072361 | +40.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0084672 | +25.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31366 | +25.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 7.1095 | +24.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.073135 | +23.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17594 | +20.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.5052 | +19.16 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SKL-EUR | 0.0041122 | +18.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RON-EUR | 0.052416 | +12.70 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 931 scans ; 399316 observations ; 222 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
