# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T20:52:04.596796+00:00
État : OK | marchés EUR : 430 | V4 : 357 | données valides : 5
Récupération : 2026-09-17T20:51:34.598080+00:00 | âge ticker : 138.8 s | durée : 140.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/430 ; 15 min 71/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- SUI-EUR : 0.64061 € ; score 82.18/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 112 € ; score 73.89/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 72.364 € ; score 64.78/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.24838 | +86.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.45876 | +42.18 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CROSS-EUR | 0.1578 | +40.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.019827 | +33.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.46578 | +32.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.005105 | +29.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| UNI-EUR | 6.6585 | +18.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.024775 | +18.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DRIFT-EUR | 0.011978 | +17.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QUID-EUR | 0.057096 | +17.48 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |

Historique : 739 scans ; 317164 observations ; 135 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
