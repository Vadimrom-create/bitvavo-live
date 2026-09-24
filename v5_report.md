# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T01:54:01.791999+00:00
État : OK | marchés EUR : 426 | V4 : 406 | données valides : 426
Récupération : 2026-09-24T01:53:34.497588+00:00 | âge ticker : 146.4 s | durée : 147.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KMNO-EUR : 0.032215 € ; score 93.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PEAQ-EUR : 0.03066 € ; score 91.02/100 ; SURVEILLE ; seuil achat non atteint
- SYN-EUR : 0.19413 € ; score 84.85/100 ; SURVEILLE ; WICK_SETUP
- LIGHTER-EUR : 4.8365 € ; score 83.02/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- POPCAT-EUR : 0.049693 € ; score 81.89/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.111671 | +44.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0021854 | +42.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.0020593 | +22.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAGA-EUR | 0.041558 | +18.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018123 | +16.88 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CPOOL-EUR | 0.030005 | +16.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.065 | +15.75 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| LSK-EUR | 0.30985 | +11.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.3425 | +10.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.045762 | +10.52 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1319 scans ; 564631 observations ; 674 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
