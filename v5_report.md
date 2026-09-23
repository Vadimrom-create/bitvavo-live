# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T23:58:24.495131+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-22T23:57:57.252549+00:00 | âge ticker : 146.0 s | durée : 146.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BABY-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XPL-EUR : 0.084289 € | IGNITION | score 84.99/100 | entrée 6.90/10
  Entrée 0.084127 € ; stop 0.080952 € ; TP1 0.090476 € ; TP2 0.093651 € ; montant 250.00 € ; risque théorique 11.15 € ; R/R net 1.53.
  Chase risk : 3.45/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HOT-EUR : 0.00038874 € ; score 91.12/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- LIGHTER-EUR : 4.4464 € ; score 90.91/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- AIXBT-EUR : 0.020738 € ; score 89.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- TURBO-EUR : 0.0009659 € ; score 89.81/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, STABILITY_HOLD
- CHZ-EUR : 0.01498 € ; score 88.65/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.020251 | +34.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 301.65 | +29.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.053478 | +28.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.019479 | +25.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| USELESS-EUR | 0.302714 | +24.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.071449 | +19.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.075734 | +18.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2135 | +18.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.4498 | +17.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.28962 | +16.64 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1227 scans ; 525439 observations ; 562 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
