# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T19:46:19.185140+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 7
Récupération : 2026-09-18T19:45:49.543695+00:00 | âge ticker : 145.1 s | durée : 146.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 44/427 ; 15 min 96/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INVALID_5M, STALE_DAILY_PROFILE
- AVAX-EUR : STALE_DAILY_PROFILE
- ENA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- ICP-EUR : INVALID_5M, STALE_DAILY_PROFILE
- KAS-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- PHA-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- PUMP-EUR : WICK_SETUP, CHASE_RISK, STALE_DAILY_PROFILE
- SEI-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- SUI-EUR : CHASE_RISK, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- XLM-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- XRP-EUR : WICK_SETUP, STALE_DAILY_PROFILE

## SURVEILLE

- PLUME-EUR : 0.0123511 € ; score 83.24/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 10.7572 € ; score 82.90/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0063763 | +57.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.03575 | +45.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.003876 | +38.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARB-EUR | 0.19182 | +25.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.029116 | +24.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| C-EUR | 0.060049 | +23.19 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.045889 | +23.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.2276 | +22.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZAMA-EUR | 0.05239 | +21.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.6124 | +21.05 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 823 scans ; 353200 observations ; 178 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
