# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T22:05:55.383685+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T22:05:23.728624+00:00 | âge ticker : 146.2 s | durée : 147.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : 8.5527 € | IGNITION | score 90.56/100 | entrée 7.40/10
  Entrée 8.5633 € ; stop 8.2349 € ; TP1 9.2201 € ; TP2 9.5485 € ; montant 250.00 € ; risque théorique 11.30 € ; R/R net 1.54.
  Chase risk : 3.544/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- RAY-EUR : 1.83791 € | IGNITION | score 80.06/100 | entrée 6.55/10
  Entrée 1.8369 € ; stop 1.75909 € ; TP1 1.99251 € ; TP2 2.07033 € ; montant 243.85 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.762/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ACU-EUR : 0.12187 € ; score 88.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IMX-EUR : 0.14489 € ; score 85.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- USELESS-EUR : 0.255401 € ; score 85.14/100 ; SURVEILLE ; WICK_SETUP
- LIGHTER-EUR : 4.2871 € ; score 84.61/100 ; SURVEILLE ; seuil achat non atteint
- HOT-EUR : 0.00040409 € ; score 84.12/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016911 | +109.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006911 | +55.79 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.125652 | +43.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019289 | +38.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 108.419 | +27.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062608 | +22.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.04382 | +19.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.005988 | +18.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.67111 | +17.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KITE-EUR | 0.13449 | +16.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1566 scans ; 670050 observations ; 1049 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
