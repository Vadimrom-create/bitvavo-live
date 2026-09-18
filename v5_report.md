# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T06:43:50.537266+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 9
Récupération : 2026-09-18T06:43:16.378282+00:00 | âge ticker : 144.1 s | durée : 146.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 40/430 ; 15 min 55/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : SELLER_HEAVY_BOOK, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- PUMP-EUR : 0.0037198 € ; score 80.05/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.2942 € ; score 78.48/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 211.07 € ; score 76.07/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.014498 | +39.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.020801 | +34.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.43878 | +29.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18743 | +29.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.026 | +28.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CROSS-EUR | 0.151781 | +27.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.4163 | +26.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0045107 | +22.50 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MET-EUR | 0.22006 | +21.42 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAY-EUR | 1.4867 | +20.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 774 scans ; 332214 observations ; 152 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
