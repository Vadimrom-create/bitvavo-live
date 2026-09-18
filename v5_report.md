# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T05:42:56.243231+00:00
État : OK | marchés EUR : 430 | V4 : 364 | données valides : 7
Récupération : 2026-09-18T05:42:26.566774+00:00 | âge ticker : 146.1 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 39/430 ; 15 min 49/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : STALE_DAILY_PROFILE
- LTC-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- USDC-EUR : 0.8708 € ; score 81.09/100 ; SURVEILLE ; WICK_SETUP
- SYRUP-EUR : 0.18458 € ; score 76.21/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 210.25 € ; score 75.76/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.013702 | +32.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.0209 | +30.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| COTI-EUR | 0.019914 | +28.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.152003 | +28.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.42528 | +26.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.4199 | +25.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVA-EUR | 0.23628 | +23.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARB-EUR | 0.18305 | +22.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.57499 | +20.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.21635 | +20.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 771 scans ; 330924 observations ; 148 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
