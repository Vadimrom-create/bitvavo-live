# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T20:59:00.133317+00:00
État : OK | marchés EUR : 430 | V4 : 380 | données valides : 430
Récupération : 2026-10-01T20:58:28.664326+00:00 | âge ticker : 153.4 s | durée : 154.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 151.11 € ; score 91.83/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.29338 € ; score 88.60/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0054494 € ; score 88.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RUNE-EUR : 0.6864 € ; score 85.26/100 ; SURVEILLE ; WICK_SETUP
- TRAC-EUR : 0.39563 € ; score 84.88/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.0008 | +216.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6345 | +48.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.20333 | +39.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.113559 | +37.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0747229 | +24.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04528 | +23.11 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.42123 | +19.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.52074 | +19.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.166638 | +18.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVE-EUR | 0.009371 | +18.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1932 scans ; 826838 observations ; 1493 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
