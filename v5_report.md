# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T20:34:04.539892+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 8
Récupération : 2026-09-14T20:33:37.341384+00:00 | âge ticker : 144.1 s | durée : 145.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 66/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : STALE_DAILY_PROFILE
- HBAR-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- SHIB-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- WAL-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- ETH-EUR : 2245.65 € ; score 84.10/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.34447 € ; score 79.07/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.14828 € ; score 78.25/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.18614 € ; score 78.05/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 71.196 € ; score 77.47/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.29373 | +52.77 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.024768 | +42.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0504146 | +24.42 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.28345 | +17.43 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.14522 | +15.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.078032 | +12.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RED-EUR | 0.12258 | +10.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.2329 | +10.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENDLE-EUR | 2.0448 | +10.23 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| T-EUR | 0.0041882 | +9.89 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 499 scans ; 214097 observations ; 82 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
