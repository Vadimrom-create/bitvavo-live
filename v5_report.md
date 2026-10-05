# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T12:55:20.827920+00:00
État : OK | marchés EUR : 427 | V4 : 362 | données valides : 426
Récupération : 2026-10-05T12:54:19.378062+00:00 | âge ticker : 178.0 s | durée : 180.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : 234.301 € | IGNITION | score 89.71/100 | entrée 7.50/10
  Entrée 234.526 € ; stop 222.41 € ; TP1 258.758 € ; TP2 270.874 € ; montant 205.20 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 1.731/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- BAT-EUR : 0.09224 € ; score 93.17/100 ; SURVEILLE ; WICK_SETUP
- ORCA-EUR : 1.778 € ; score 90.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.22643 € ; score 89.39/100 ; SURVEILLE ; seuil achat non atteint
- YGG-EUR : 0.025403 € ; score 89.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PEPE-EUR : 3.9891e-06 € ; score 87.85/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.203139 | +78.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.080588 | +63.48 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RLC-EUR | 0.50003 | +54.83 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.98 | +28.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.02695 | +19.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046183 | +14.91 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.8254 | +12.39 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| UMA-EUR | 0.40136 | +11.55 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.027474 | +11.50 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ADA-EUR | 0.24279 | +11.44 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2073 scans ; 887087 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
