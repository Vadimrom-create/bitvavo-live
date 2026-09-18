# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T15:19:59.522388+00:00
État : OK | marchés EUR : 427 | V4 : 377 | données valides : 10
Récupération : 2026-09-18T15:19:25.208257+00:00 | âge ticker : 150.4 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 45/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- PYTH-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- XPL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- XRP-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- LTC-EUR : 48.868 € ; score 75.53/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 10.617 € ; score 73.15/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 96.268 € ; score 72.77/100 ; SURVEILLE ; STABILITY_HOLD
- ETH-EUR : 2252.06 € ; score 70.85/100 ; SURVEILLE ; STABILITY_HOLD
- HBAR-EUR : 0.069035 € ; score 70.38/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0078431 | +103.52 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.004211 | +50.92 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CNPY-EUR | 0.47785 | +41.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.2845 | +32.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18121 | +27.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.030684 | +26.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044213 | +20.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.027856 | +20.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.5052 | +20.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.061288 | +18.82 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 806 scans ; 345941 observations ; 166 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
