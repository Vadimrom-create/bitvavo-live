# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T08:06:03.101978+00:00
État : OK | marchés EUR : 430 | V4 : 364 | données valides : 8
Récupération : 2026-09-18T08:05:29.933812+00:00 | âge ticker : 148.2 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/430 ; 15 min 68/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- RENDER-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- STX-EUR : WICK_SETUP, CHASE_RISK, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00058633 € ; score 84.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TAO-EUR : 213.43 € ; score 81.37/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.2178e-06 € ; score 75.10/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0062972 | +71.01 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.01513 | +45.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.46882 | +37.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.155391 | +29.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18495 | +28.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0395 | +27.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UNI-EUR | 7.5958 | +27.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.019343 | +19.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.029 | +19.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.22008 | +19.35 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 781 scans ; 335224 observations ; 153 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
