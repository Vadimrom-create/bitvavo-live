# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T16:40:16.159890+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-01T16:39:43.895124+00:00 | âge ticker : 149.3 s | durée : 150.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DRIFT-EUR : 0.018496 € ; score 91.18/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- BABY-EUR : 0.012068 € ; score 89.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RECALL-EUR : 0.042974 € ; score 85.57/100 ; SURVEILLE ; seuil achat non atteint
- KAIA-EUR : 0.03355 € ; score 84.88/100 ; SURVEILLE ; WICK_SETUP
- ZRO-EUR : 1.5651 € ; score 84.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000608 | +135.26 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.807 | +80.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0753266 | +30.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.17914 | +23.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.48956 | +21.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.41875 | +20.95 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.178053 | +20.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04546 | +19.92 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.029032 | +16.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.009515 | +14.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1919 scans ; 821248 observations ; 1485 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
