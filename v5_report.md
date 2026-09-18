# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T17:54:08.125870+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 9
Récupération : 2026-09-18T17:53:35.094313+00:00 | âge ticker : 144.4 s | durée : 145.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 44/427 ; 15 min 86/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- PHA-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- NPC-EUR : 0.0208627 € ; score 84.90/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- DOT-EUR : 0.9903 € ; score 75.66/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.16008 € ; score 75.58/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 216.67 € ; score 75.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- WLD-EUR : 0.36407 € ; score 74.90/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0074033 | +89.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0041006 | +47.83 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.5012 | +43.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.033073 | +33.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.062789 | +27.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.2968 | +24.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.02216 | +23.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19236 | +22.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6078 | +20.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.028169 | +19.72 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 816 scans ; 350211 observations ; 167 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
