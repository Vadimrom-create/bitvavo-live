# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T00:34:19.224858+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-10-01T00:33:46.706614+00:00 | âge ticker : 150.4 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ESP-EUR : 0.094063 € ; score 88.70/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- W-EUR : 0.011875 € ; score 88.03/100 ; SURVEILLE ; seuil achat non atteint
- BIGTIME-EUR : 0.007805 € ; score 84.42/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.92255 € ; score 83.66/100 ; SURVEILLE ; seuil achat non atteint
- ETHFI-EUR : 0.68465 € ; score 83.63/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0052 | +87.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35783 | +49.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008571 | +26.27 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028574 | +21.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.32868 | +18.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.44109 | +18.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.38993 | +17.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0610562 | +15.22 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOM-EUR | 0.0020708 | +11.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOMI-EUR | 0.19692 | +10.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1874 scans ; 801898 observations ; 1429 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
