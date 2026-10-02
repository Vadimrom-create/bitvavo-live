# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T00:00:23.912183+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T23:59:50.192111+00:00 | âge ticker : 148.6 s | durée : 149.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.45014 € ; score 93.42/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0039525 € ; score 87.41/100 ; SURVEILLE ; seuil achat non atteint
- TOWNS-EUR : 0.0019813 € ; score 87.00/100 ; SURVEILLE ; seuil achat non atteint
- KITE-EUR : 0.13481 € ; score 85.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAITO-EUR : 0.30747 € ; score 85.04/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00057144 | +121.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.125802 | +51.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5951 | +35.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.18692 | +25.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43926 | +21.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.0445 | +20.47 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0024469 | +18.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.163744 | +16.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20562 | +16.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.49552 | +14.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1942 scans ; 831138 observations ; 1511 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
