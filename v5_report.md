# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T08:57:15.700595+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T08:56:46.098051+00:00 | âge ticker : 154.8 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- MEGA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : 0.045399 € | IGNITION | score 90.12/100 | entrée 6.75/10
  Entrée 0.045402 € ; stop 0.043107 € ; TP1 0.049991 € ; TP2 0.052286 € ; montant 209.16 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.376/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZBT-EUR : 0.080633 € ; score 93.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LDO-EUR : 0.37099 € ; score 89.90/100 ; SURVEILLE ; seuil achat non atteint
- AI-EUR : 0.018617 € ; score 88.29/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BREV-EUR : 0.07855 € ; score 88.26/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- SAPIEN-EUR : 0.070229 € ; score 86.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.036384 | +47.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 311.86 | +32.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.32322 | +30.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.16973 | +26.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.01911 | +23.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.085564 | +23.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.256 | +20.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALLO-EUR | 0.275534 | +19.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0094398 | +17.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UP-EUR | 0.063036 | +17.35 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1257 scans ; 538219 observations ; 629 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
