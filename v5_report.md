# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T16:12:04.129846+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T16:11:32.847213+00:00 | âge ticker : 151.0 s | durée : 151.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.40377 € | IGNITION | score 89.66/100 | entrée 6.80/10
  Entrée 0.40502 € ; stop 0.38428 € ; TP1 0.44649 € ; TP2 0.46723 € ; montant 206.80 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 2.04/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- JUP-EUR : 0.28545 € | IGNITION | score 80.86/100 | entrée 7.15/10
  Entrée 0.28615 € ; stop 0.27521 € ; TP1 0.30803 € ; TP2 0.31897 € ; montant 250.00 € ; risque théorique 11.27 € ; R/R net 1.53.
  Chase risk : 1.008/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- IMX-EUR : 0.1391 € ; score 92.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TIA-EUR : 0.42967 € ; score 91.62/100 ; SURVEILLE ; seuil achat non atteint
- ZK-EUR : 0.011439 € ; score 91.49/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- CELR-EUR : 0.0027251 € ; score 90.91/100 ; SURVEILLE ; STABILITY_HOLD
- PROM-EUR : 4.9 € ; score 87.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.064623 | +46.48 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.20284 | +29.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.65456 | +27.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.01403 | +21.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.22404 | +18.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.086379 | +17.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.020775 | +16.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.037187 | +16.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.43978 | +16.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 84.199 | +15.79 % | DETECTED_EARLY | NONE | NONE |

Historique : 1455 scans ; 622653 observations ; 873 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
