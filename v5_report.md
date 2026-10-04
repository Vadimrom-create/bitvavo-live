# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T14:24:55.480861+00:00
État : OK | marchés EUR : 426 | V4 : 354 | données valides : 426
Récupération : 2026-10-04T14:23:53.015778+00:00 | âge ticker : 180.4 s | durée : 181.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.34248 € | IGNITION | score 76.79/100 | entrée 6.25/10
  Entrée 0.34271 € ; stop 0.33065 € ; TP1 0.36683 € ; TP2 0.37889 € ; montant 250.00 € ; risque théorique 10.52 € ; R/R net 1.50.
  Chase risk : 4.154/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FLUID-EUR : 1.5492 € ; score 82.43/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 3.0629 € ; score 82.33/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : 0.0068259 € ; score 80.43/100 ; SURVEILLE ; WICK_SETUP
- ALGO-EUR : 0.117107 € ; score 80.22/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 158.81 € ; score 76.61/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| BEAM-EUR | 0.0024274 | +29.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.049884 | +27.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.114 | +25.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| POND-EUR | 0.0017719 | +23.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.61564 | +18.45 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MIOTA-EUR | 0.055704 | +14.56 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TREAD-EUR | 1.048 | +13.98 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AXS-EUR | 1.2156 | +13.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AKT-EUR | 0.66398 | +13.54 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.002366 | +13.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2057 scans ; 880268 observations ; 1629 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
