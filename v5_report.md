# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T13:51:06.821026+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T13:50:34.262533+00:00 | âge ticker : 147.3 s | durée : 148.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.48833 € | IGNITION | score 93.06/100 | entrée 7.85/10
  Entrée 0.48901 € ; stop 0.47005 € ; TP1 0.52692 € ; TP2 0.54589 € ; montant 250.00 € ; risque théorique 11.41 € ; R/R net 1.54.
  Chase risk : 1.231/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TNSR-EUR : 0.036431 € ; score 88.44/100 ; SURVEILLE ; seuil achat non atteint
- STO-EUR : 0.039631 € ; score 87.08/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- CFG-EUR : 0.146469 € ; score 87.04/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ENJ-EUR : 0.027048 € ; score 83.39/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- MAGIC-EUR : 0.047633 € ; score 82.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 1.14631 | +58.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 141.178 | +52.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008638 | +46.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.017584 | +37.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.25648 | +33.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.25 | +24.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.54689 | +20.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.00646 | +18.27 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| WLD-EUR | 0.5102 | +18.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006133 | +17.92 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1620 scans ; 693108 observations ; 1142 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
