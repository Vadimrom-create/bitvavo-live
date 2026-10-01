# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T19:25:18.685052+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-01T19:24:42.977200+00:00 | âge ticker : 152.0 s | durée : 153.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- HUMA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NMR-EUR : 10.0572 € ; score 89.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- EIGEN-EUR : 0.22216 € ; score 89.24/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 9.7833 € ; score 82.29/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 12.8274 € ; score 80.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 148.75 € ; score 80.93/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00061216 | +137.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6627 | +73.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04763 | +29.85 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.0766283 | +28.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.18259 | +28.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.101778 | +22.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.030792 | +21.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.170927 | +19.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.53072 | +19.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.002448 | +17.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1927 scans ; 824688 observations ; 1490 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
