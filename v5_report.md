# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T18:38:03.595330+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-25T18:37:33.061789+00:00 | âge ticker : 152.5 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.12384 € | IGNITION | score 91.46/100 | entrée 7.60/10
  Entrée 0.12396 € ; stop 0.11952 € ; TP1 0.13284 € ; TP2 0.13728 € ; montant 250.00 € ; risque théorique 10.67 € ; R/R net 1.51.
  Chase risk : 2.674/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FLUX-EUR : 0.060449 € ; score 92.77/100 ; SURVEILLE ; LOW_LIQUIDITY
- PENGU-EUR : 0.0087971 € ; score 87.83/100 ; SURVEILLE ; seuil achat non atteint
- SUSHI-EUR : 0.23271 € ; score 87.69/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 62.269 € ; score 86.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.28821 € ; score 86.05/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| WMTX-EUR | 0.02489 | +70.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.072565 | +67.53 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21006 | +30.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.48801 | +26.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014298 | +24.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.08885 | +22.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.75334 | +21.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22871 | +20.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.062891 | +17.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.11419 | +15.96 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1463 scans ; 626069 observations ; 878 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
