# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T08:41:24.016978+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-23T08:40:54.266793+00:00 | âge ticker : 149.0 s | durée : 149.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : 0.045184 € | IGNITION | score 90.45/100 | entrée 7.25/10
  Entrée 0.045184 € ; stop 0.043125 € ; TP1 0.049302 € ; TP2 0.051361 € ; montant 228.97 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 4.468/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NPC-EUR : 0.022 € | IGNITION | score 84.13/100 | entrée 7.20/10
  Entrée 0.022 € ; stop 0.0207854 € ; TP1 0.0244291 € ; TP2 0.0256437 € ; montant 193.50 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 5.726/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MOVR-EUR : 0.8294 € ; score 92.87/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- BEAM-EUR : 0.001763 € ; score 92.79/100 ; SURVEILLE ; SPREAD_RISK
- JASMY-EUR : 0.0040874 € ; score 88.38/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- PROMPT-EUR : 0.020054 € ; score 87.51/100 ; SURVEILLE ; seuil achat non atteint
- TRAC-EUR : 0.31046 € ; score 85.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.035 | +42.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 315.82 | +34.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.088489 | +31.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.32212 | +31.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.1723 | +29.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019561 | +26.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.282091 | +22.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2633 | +20.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.00961 | +20.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.020048 | +19.55 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1256 scans ; 537793 observations ; 629 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
