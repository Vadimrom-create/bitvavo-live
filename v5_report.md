# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T11:59:38.891355+00:00
État : OK | marchés EUR : 430 | V4 : 375 | données valides : 12
Récupération : 2026-09-18T11:59:04.687012+00:00 | âge ticker : 151.1 s | durée : 151.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 43/430 ; 15 min 79/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- NPC-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 214.85 € ; score 73.93/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0072344 | +97.33 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.47636 | +41.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.6444 | +27.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DRIFT-EUR | 0.013541 | +27.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.17899 | +23.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0555 | +22.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 5.8462 | +20.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.49653 | +19.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.029229 | +19.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.38607 | +18.67 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 795 scans ; 341244 observations ; 157 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
