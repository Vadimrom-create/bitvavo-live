# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T21:54:12.982847+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-22T21:53:43.770558+00:00 | âge ticker : 146.7 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : 64.838 € | IGNITION | score 86.67/100 | entrée 7.40/10
  Entrée 64.859 € ; stop 62.323 € ; TP1 69.93 € ; TP2 72.466 € ; montant 250.00 € ; risque théorique 11.49 € ; R/R net 1.54.
  Chase risk : 3.504/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- NEO-EUR : 2.3034 € ; score 91.54/100 ; SURVEILLE ; seuil achat non atteint
- WCT-EUR : 0.03945 € ; score 88.89/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.011302 € ; score 86.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ZORA-EUR : 0.007982 € ; score 84.14/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- THE-EUR : 0.07204 € ; score 82.64/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.019884 | +35.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 298.15 | +27.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019783 | +27.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KERNEL-EUR | 0.054001 | +27.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.306295 | +23.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.075523 | +17.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.068823 | +17.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.12121 | +17.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0086875 | +15.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.1858 | +14.96 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1219 scans ; 522031 observations ; 544 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
