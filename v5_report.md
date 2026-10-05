# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T13:06:40.793708+00:00
État : OK | marchés EUR : 427 | V4 : 363 | données valides : 426
Récupération : 2026-10-05T13:06:07.459930+00:00 | âge ticker : 153.1 s | durée : 153.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : 231.042 € | IGNITION | score 87.33/100 | entrée 7.25/10
  Entrée 231.12 € ; stop 222.237 € ; TP1 248.886 € ; TP2 257.769 € ; montant 250.00 € ; risque théorique 11.33 € ; R/R net 1.54.
  Chase risk : 5.485/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AAVE-EUR : 164.37 € ; score 93.83/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYN-EUR : 0.16545 € ; score 88.15/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.7265 € ; score 87.08/100 ; SURVEILLE ; seuil achat non atteint
- DRIFT-EUR : 0.01778 € ; score 87.00/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- YGG-EUR : 0.025502 € ; score 86.07/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.213307 | +93.84 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.088 | +78.52 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RLC-EUR | 0.50076 | +55.06 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.965 | +27.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.026836 | +19.29 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05445 | +17.22 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046553 | +15.96 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.086815 | +12.70 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ADA-EUR | 0.2441 | +12.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UMA-EUR | 0.40166 | +11.63 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2074 scans ; 887514 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
