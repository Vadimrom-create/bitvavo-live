# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T06:41:14.053778+00:00
État : OK | marchés EUR : 430 | V4 : 365 | données valides : 8
Récupération : 2026-09-18T06:40:41.130766+00:00 | âge ticker : 139.8 s | durée : 140.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 40/430 ; 15 min 55/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- PUMP-EUR : 0.0037174 € ; score 79.63/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.2956 € ; score 77.02/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 210.61 € ; score 75.88/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.014633 | +40.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| COTI-EUR | 0.020795 | +35.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.43423 | +28.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0224 | +28.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18611 | +28.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.151359 | +27.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.3927 | +26.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.21962 | +21.18 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RAY-EUR | 1.49269 | +21.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| G-EUR | 0.0044542 | +20.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 774 scans ; 332214 observations ; 152 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
