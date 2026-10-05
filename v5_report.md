# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T12:43:18.014383+00:00
État : OK | marchés EUR : 427 | V4 : 362 | données valides : 426
Récupération : 2026-10-05T12:42:40.920979+00:00 | âge ticker : 164.7 s | durée : 165.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : 2.2986 € | IGNITION | score 75.00/100 | entrée 5.95/10
  Entrée 2.2981 € ; stop 2.2002 € ; TP1 2.4938 € ; TP2 2.5917 € ; montant 242.66 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 4.516/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RSR-EUR : 0.0016318 € ; score 90.33/100 ; SURVEILLE ; seuil achat non atteint
- KAIA-EUR : 0.036091 € ; score 90.03/100 ; SURVEILLE ; seuil achat non atteint
- COMP-EUR : 22.156 € ; score 89.38/100 ; SURVEILLE ; LOW_LIQUIDITY
- ENS-EUR : 6.1672 € ; score 85.79/100 ; SURVEILLE ; seuil achat non atteint
- DRV-EUR : 0.36312 € ; score 84.50/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.196433 | +78.25 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.49302 | +52.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.065466 | +32.81 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| FLUID-EUR | 1.9418 | +26.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UMA-EUR | 0.43045 | +19.64 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SCR-EUR | 0.026088 | +16.27 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046003 | +14.47 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.027457 | +11.43 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ADA-EUR | 0.24242 | +11.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZEUS-EUR | 0.0022539 | +10.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2072 scans ; 886660 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
