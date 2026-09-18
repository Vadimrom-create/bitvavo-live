# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T06:46:39.902324+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 6
Récupération : 2026-09-18T06:46:07.487516+00:00 | âge ticker : 148.8 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 40/430 ; 15 min 58/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : SELLER_HEAVY_BOOK, STALE_DAILY_PROFILE
- FET-EUR : EXTENDED_24H, CHASE_RISK, STALE_DAILY_PROFILE
- LDO-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- LINK-EUR : STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 211.73 € ; score 76.29/100 ; SURVEILLE ; seuil achat non atteint
- SYRUP-EUR : 0.18416 € ; score 75.05/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0037141 € ; score 74.34/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.014727 | +42.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.020359 | +31.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.43747 | +29.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18771 | +28.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0216 | +28.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CROSS-EUR | 0.151781 | +27.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.4486 | +26.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0046265 | +25.64 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MET-EUR | 0.21949 | +21.18 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AGI-EUR | 0.004963 | +20.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 775 scans ; 332644 observations ; 152 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
