# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T19:44:23.085418+00:00
État : OK | marchés EUR : 430 | V4 : 383 | données valides : 430
Récupération : 2026-10-01T19:43:49.154594+00:00 | âge ticker : 165.7 s | durée : 167.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KSM-EUR : 4.5433 € ; score 87.16/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- STX-EUR : 0.33356 € ; score 83.19/100 ; SURVEILLE ; WICK_SETUP
- TRAC-EUR : 0.39358 € ; score 82.81/100 ; SURVEILLE ; WIDE_SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- AAVE-EUR : 149.04 € ; score 82.57/100 ; SURVEILLE ; seuil achat non atteint
- EDEN-EUR : 0.052046 € ; score 82.45/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000603 | +133.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.658 | +70.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.19225 | +34.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0768109 | +27.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04669 | +26.63 % | DETECTED_EARLY | NONE | NONE |
| GTC-EUR | 0.103197 | +24.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.03111 | +21.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0056499 | +20.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.171524 | +19.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVE-EUR | 0.00947 | +18.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1928 scans ; 825118 observations ; 1491 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
