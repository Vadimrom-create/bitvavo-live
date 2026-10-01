# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T16:22:18.742308+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-01T16:21:19.972992+00:00 | âge ticker : 184.2 s | durée : 185.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.5599 € ; score 85.18/100 ; SURVEILLE ; WICK_SETUP
- KAIA-EUR : 0.033336 € ; score 84.28/100 ; SURVEILLE ; WICK_SETUP
- TRX-EUR : 0.29769 € ; score 83.15/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : 0.049974 € ; score 82.88/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KSM-EUR : 4.6325 € ; score 82.77/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00056854 | +118.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.8552 | +86.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0737281 | +28.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.1809 | +24.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.42652 | +24.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NOS-EUR | 0.48715 | +20.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04526 | +20.28 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.176616 | +19.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.029261 | +18.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0024808 | +14.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1918 scans ; 820818 observations ; 1483 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
