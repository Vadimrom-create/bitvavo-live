# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T00:05:53.379614+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T00:04:54.883053+00:00 | âge ticker : 183.9 s | durée : 184.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KMNO-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.22163 € | IGNITION | score 85.85/100 | entrée 7.50/10
  Entrée 0.22182 € ; stop 0.21282 € ; TP1 0.23981 € ; TP2 0.24881 € ; montant 250.00 € ; risque théorique 11.86 € ; R/R net 1.56.
  Chase risk : 3.555/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 12.2556 € ; score 94.67/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : 1.4692 € ; score 93.57/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.00191 € ; score 92.50/100 ; SURVEILLE ; seuil achat non atteint
- MTL-EUR : 0.30915 € ; score 91.46/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, VERY_SELLER_HEAVY_BOOK
- RPL-EUR : 1.8654 € ; score 90.51/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.075262 | +67.25 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0011899 | +50.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.22412 | +29.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.74761 | +21.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.065964 | +19.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.23705 | +19.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.4596 | +18.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022543 | +18.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.013463 | +17.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.71796 | +17.20 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1487 scans ; 636317 observations ; 907 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
