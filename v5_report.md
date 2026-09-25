# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T05:36:01.981813+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-25T05:35:33.679928+00:00 | âge ticker : 153.6 s | durée : 154.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.26756 € ; score 93.04/100 ; SURVEILLE ; seuil achat non atteint
- EPIC-EUR : 0.43961 € ; score 91.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TIA-EUR : 0.42502 € ; score 89.55/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.66516 € ; score 89.35/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.86746 € ; score 85.40/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 84.669 | +34.10 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.63596 | +28.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.101278 | +27.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.46656 | +23.87 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.038446 | +20.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.087009 | +20.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17438 | +17.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021618 | +16.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0081496 | +15.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAI-EUR | 0.00406 | +14.53 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1420 scans ; 607708 observations ; 811 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
