# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T03:22:37.193263+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-09-27T03:22:02.852972+00:00 | âge ticker : 148.3 s | durée : 148.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AEVO-EUR : 0.023877 € ; score 94.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- AVNT-EUR : 0.11174 € ; score 91.52/100 ; SURVEILLE ; seuil achat non atteint
- ALLO-EUR : 0.266828 € ; score 91.46/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- TAIKO-EUR : 0.08364 € ; score 90.99/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 5.1613e-06 € ; score 89.44/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 151.47 | +72.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006288 | +40.33 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.24857 | +40.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017159 | +28.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.00641 | +23.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.061351 | +21.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.70122 | +20.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.50816 | +16.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0013638 | +15.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.012373 | +15.13 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1584 scans ; 677736 observations ; 1072 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
