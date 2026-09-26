# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T21:22:22.657949+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-26T21:21:47.451255+00:00 | âge ticker : 151.3 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- REZ-EUR : 0.0038023 € ; score 91.71/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ETC-EUR : 8.2337 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP
- APE-EUR : 0.1355 € ; score 88.75/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 8.4427 € ; score 87.44/100 ; SURVEILLE ; seuil achat non atteint
- STX-EUR : 0.29519 € ; score 85.30/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00177 | +119.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.000706 | +59.15 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.133 | +51.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019128 | +29.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 108.014 | +26.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006167 | +21.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.04388 | +21.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061298 | +19.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.66091 | +17.00 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TREAD-EUR | 0.75 | +15.87 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1563 scans ; 668769 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
