# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T12:24:58.182351+00:00
État : OK | marchés EUR : 427 | V4 : 373 | données valides : 11
Récupération : 2026-09-18T12:24:22.635350+00:00 | âge ticker : 146.8 s | durée : 148.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 39/427 ; 15 min 79/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- NPC-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.41058 € ; score 81.23/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 6.9636 € ; score 69.57/100 ; SURVEILLE ; STABILITY_HOLD
- DOGE-EUR : 0.074402 € ; score 68.89/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0073646 | +94.13 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.48377 | +43.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.6386 | +27.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.013409 | +26.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18058 | +25.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.028376 | +22.75 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NEAR-EUR | 3.0614 | +21.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.49253 | +19.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.029074 | +19.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APT-EUR | 0.5921 | +18.00 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 796 scans ; 341671 observations ; 157 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
