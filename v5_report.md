# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T01:36:44.125592+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T01:36:13.644747+00:00 | âge ticker : 154.6 s | durée : 155.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : 0.0039503 € | IGNITION | score 87.29/100 | entrée 7.65/10
  Entrée 0.0039403 € ; stop 0.0037714 € ; TP1 0.0042781 € ; TP2 0.0044469 € ; montant 241.38 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.092/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DOT-EUR : 1.0505 € ; score 92.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- METIS-EUR : 3.1019 € ; score 90.96/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- SUSHI-EUR : 0.2221 € ; score 89.87/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0051653 € ; score 89.41/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- LISTA-EUR : 0.073194 € ; score 89.29/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014293 | +82.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.015 | +74.01 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KERNEL-EUR | 0.058923 | +59.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.051463 | +50.83 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.112847 | +41.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.3058 | +34.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.04371 | +32.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.0276 | +28.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.4025e-06 | +24.77 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21552 | +23.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1138 scans ; 487525 observations ; 438 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
