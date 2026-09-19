# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T02:18:19.159983+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 19
Récupération : 2026-09-19T02:17:47.457592+00:00 | âge ticker : 151.8 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/427 ; 15 min 64/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, INVALID_5M
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- WLD-EUR : STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE

## SURVEILLE

- ONDO-EUR : 0.35629 € ; score 88.35/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 81.523 € ; score 79.88/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.20028 € ; score 79.53/100 ; SURVEILLE ; WICK_SETUP
- ENA-EUR : 0.1515 € ; score 77.36/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0065412 | +52.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037554 | +46.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.00386 | +35.56 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.199373 | +29.85 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.054998 | +26.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.27263 | +22.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.029568 | +21.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044479 | +21.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6568 | +19.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZK-EUR | 0.009905 | +19.63 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 851 scans ; 365156 observations ; 185 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
