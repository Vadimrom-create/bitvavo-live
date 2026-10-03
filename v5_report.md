# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T09:56:55.683956+00:00
État : OK | marchés EUR : 426 | V4 : 397 | données valides : 426
Récupération : 2026-10-03T09:56:22.163292+00:00 | âge ticker : 151.5 s | durée : 152.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SUI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.22002 € | IGNITION | score 87.70/100 | entrée 6.35/10
  Entrée 0.22062 € ; stop 0.21202 € ; TP1 0.23782 € ; TP2 0.24642 € ; montant 250.00 € ; risque théorique 11.46 € ; R/R net 1.54.
  Chase risk : 2.106/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WLD-EUR : 0.50537 € | IGNITION | score 81.24/100 | entrée 7.40/10
  Entrée 0.50571 € ; stop 0.4866 € ; TP1 0.54393 € ; TP2 0.56304 € ; montant 250.00 € ; risque théorique 11.16 € ; R/R net 1.53.
  Chase risk : 0.476/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CHZ-EUR : 0.015314 € ; score 91.02/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 1.05394 € ; score 88.47/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.8316 € ; score 87.37/100 ; SURVEILLE ; WICK_SETUP
- LDO-EUR : 0.40404 € ; score 86.25/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.22264 € ; score 86.17/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HFT-EUR | 0.006907 | +21.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.067304 | +19.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008936 | +14.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0063014 | +14.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.065308 | +13.23 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 232.493 | +12.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.22002 | +9.21 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.6578 | +7.12 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CAP-EUR | 0.0629901 | +6.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AVA-EUR | 0.24011 | +5.90 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2042 scans ; 873878 observations ; 1608 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
