# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T09:51:20.330710+00:00
État : OK | marchés EUR : 430 | V4 : 372 | données valides : 11
Récupération : 2026-09-18T09:50:49.119786+00:00 | âge ticker : 146.9 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 37/430 ; 15 min 76/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- KAS-EUR : INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LSK-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- W-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.000604 € ; score 84.14/100 ; SURVEILLE ; SPREAD_RISK
- VET-EUR : 0.0065729 € ; score 79.23/100 ; SURVEILLE ; WICK_SETUP
- CAKE-EUR : 2.2034 € ; score 76.56/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HBAR-EUR : 0.067335 € ; score 76.49/100 ; SURVEILLE ; STABILITY_HOLD
- TAO-EUR : 216.78 € ; score 76.06/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0063855 | +74.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DRIFT-EUR | 0.014318 | +37.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.45529 | +34.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.9079 | +31.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18 | +25.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.030511 | +25.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.033 | +23.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.54477 | +22.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.51332 | +21.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.019073 | +18.34 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 787 scans ; 337804 observations ; 155 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
