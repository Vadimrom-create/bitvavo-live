# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T22:55:14.839815+00:00
État : OK | marchés EUR : 430 | V4 : 382 | données valides : 430
Récupération : 2026-10-01T22:54:11.570248+00:00 | âge ticker : 180.6 s | durée : 181.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 152.23 € ; score 94.97/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.1131 € ; score 86.80/100 ; SURVEILLE ; STABILITY_HOLD
- INJ-EUR : 6.5061 € ; score 86.33/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.049164 € ; score 85.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NMR-EUR : 10.07 € ; score 84.89/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000636 | +145.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.123536 | +47.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5861 | +38.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.18709 | +26.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04566 | +23.71 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.43421 | +22.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0024399 | +18.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.50123 | +18.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.164768 | +16.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.0054427 | +15.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1938 scans ; 829418 observations ; 1507 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
