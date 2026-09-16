# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-16T20:41:09.214369+00:00
État : OK | marchés EUR : 430 | V4 : 378 | données valides : 10
Récupération : 2026-09-16T20:40:40.178275+00:00 | âge ticker : 136.9 s | durée : 137.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 36/430 ; 15 min 62/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- ONDO-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- XLM-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- VET-EUR : 0.0061611 € ; score 93.72/100 ; SURVEILLE ; WICK_SETUP
- AVAX-EUR : 6.4148 € ; score 80.58/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.13461 € ; score 78.72/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.61851 € ; score 77.86/100 ; SURVEILLE ; STABILITY_HOLD
- UNI-EUR : 5.6446 € ; score 76.86/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.167689 | +137.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.6119 | +80.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.127084 | +30.50 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FOLD-EUR | 0.046088 | +21.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HNT-EUR | 0.41958 | +20.49 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IOST-EUR | 0.0007264 | +13.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.20863 | +12.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.35694 | +12.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 3.9376 | +12.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.2345 | +11.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 658 scans ; 282334 observations ; 103 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
