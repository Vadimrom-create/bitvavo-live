# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T18:55:12.724296+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-25T18:54:42.577068+00:00 | âge ticker : 145.9 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.12405 € | IGNITION | score 90.43/100 | entrée 6.95/10
  Entrée 0.12411 € ; stop 0.11952 € ; TP1 0.13329 € ; TP2 0.13788 € ; montant 250.00 € ; risque théorique 10.96 € ; R/R net 1.52.
  Chase risk : 3.787/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- JUP-EUR : 0.29315 € | IGNITION | score 86.10/100 | entrée 7.35/10
  Entrée 0.29305 € ; stop 0.27948 € ; TP1 0.32018 € ; TP2 0.33375 € ; montant 225.80 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.104/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 62.451 € ; score 93.99/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RPL-EUR : 1.8429 € ; score 92.33/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- TAO-EUR : 269 € ; score 91.79/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SAFE-EUR : 0.100261 € ; score 91.00/100 ; SURVEILLE ; LOW_LIQUIDITY
- MANTRA-EUR : 0.004166 € ; score 90.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.072836 | +66.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WMTX-EUR | 0.02319 | +54.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.215 | +32.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014826 | +29.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.48853 | +26.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.75639 | +22.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08965 | +20.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.22667 | +18.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.062747 | +17.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.11521 | +16.79 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1464 scans ; 626496 observations ; 879 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
