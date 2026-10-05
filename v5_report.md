# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T15:32:06.086616+00:00
État : OK | marchés EUR : 427 | V4 : 365 | données valides : 426
Récupération : 2026-10-05T15:31:32.912896+00:00 | âge ticker : 156.2 s | durée : 157.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 3.1089 € | IGNITION | score 83.49/100 | entrée 7.50/10
  Entrée 3.1099 € ; stop 2.973 € ; TP1 3.3837 € ; TP2 3.5206 € ; montant 235.91 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 4.606/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WELL-EUR : 0.0021294 € ; score 88.82/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- PLUME-EUR : 0.0175613 € ; score 86.86/100 ; SURVEILLE ; WICK_SETUP
- ZAMA-EUR : 0.074909 € ; score 85.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- YGG-EUR : 0.02574 € ; score 82.44/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- BAT-EUR : 0.09281 € ; score 82.14/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.192955 | +80.32 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.50848 | +57.55 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.070833 | +43.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8677 | +21.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 1.8798 | +19.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046612 | +16.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SCR-EUR | 0.025911 | +16.22 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.091586 | +15.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.027592 | +13.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.0526 | +13.24 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
