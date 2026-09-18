# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T06:20:03.170236+00:00
État : OK | marchés EUR : 430 | V4 : 364 | données valides : 7
Récupération : 2026-09-18T06:19:27.788011+00:00 | âge ticker : 152.6 s | durée : 155.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 40/430 ; 15 min 56/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NPC-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- PUMP-EUR : 0.0037153 € ; score 76.82/100 ; SURVEILLE ; WICK_SETUP
- LSK-EUR : 0.39319 € ; score 75.14/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- SYRUP-EUR : 0.18402 € ; score 73.94/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2161.61 € ; score 62.87/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.01488 | +43.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.44111 | +31.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.020166 | +31.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0124 | +29.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18367 | +27.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.14939 | +26.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.3984 | +26.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.21797 | +21.24 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAY-EUR | 1.46625 | +20.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CHIP-EUR | 0.03779 | +19.37 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 773 scans ; 331784 observations ; 149 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
