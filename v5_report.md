# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T19:20:01.976995+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 8
Récupération : 2026-09-18T19:19:30.752812+00:00 | âge ticker : 138.6 s | durée : 139.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 43/427 ; 15 min 90/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INVALID_5M, STALE_DAILY_PROFILE
- AVAX-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- ENA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- LDO-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- PHA-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- PUMP-EUR : WICK_SETUP, CHASE_RISK, STALE_DAILY_PROFILE
- VET-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- ETH-EUR : 2292.21 € ; score 79.63/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.39275 € ; score 77.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FET-EUR : 0.16003 € ; score 77.69/100 ; SURVEILLE ; seuil achat non atteint
- XRP-EUR : 1.21958 € ; score 77.32/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0064548 | +58.75 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037306 | +50.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.003878 | +38.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.2755 | +26.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CNPY-EUR | 0.52013 | +25.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.19123 | +24.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.06003 | +23.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.045396 | +22.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZK-EUR | 0.009721 | +22.38 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| S-EUR | 0.028292 | +21.20 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 821 scans ; 352346 observations ; 178 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
