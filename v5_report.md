# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T00:49:54.813739+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T00:49:24.090914+00:00 | âge ticker : 146.6 s | durée : 147.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.41164 € | IGNITION | score 81.56/100 | entrée 7.65/10
  Entrée 0.4114 € ; stop 0.39533 € ; TP1 0.44353 € ; TP2 0.4596 € ; montant 250.00 € ; risque théorique 11.48 € ; R/R net 1.54.
  Chase risk : 6.128/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GRT-EUR : 0.020695 € ; score 91.17/100 ; SURVEILLE ; seuil achat non atteint
- TAIKO-EUR : 0.08192 € ; score 87.81/100 ; SURVEILLE ; seuil achat non atteint
- MOODENG-EUR : 0.042204 € ; score 87.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PUMP-EUR : 0.0039049 € ; score 87.54/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SPK-EUR : 0.018986 € ; score 87.18/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.018 | +109.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014355 | +83.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.11984 | +49.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.050451 | +46.43 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.04481 | +35.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30577 | +34.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.001097 | +33.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008655 | +31.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.383e-06 | +24.02 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21765 | +22.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1135 scans ; 486247 observations ; 434 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
