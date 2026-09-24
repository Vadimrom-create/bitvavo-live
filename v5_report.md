# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T19:35:47.893823+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T19:35:16.847156+00:00 | âge ticker : 149.3 s | durée : 150.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 262.71 € | IGNITION | score 88.13/100 | entrée 7.65/10
  Entrée 262.58 € ; stop 253.31 € ; TP1 281.11 € ; TP2 290.38 € ; montant 250.00 € ; risque théorique 10.54 € ; R/R net 1.50.
  Chase risk : 2.059/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VVV-EUR : 27.9275 € | IGNITION | score 81.94/100 | entrée 6.10/10
  Entrée 27.8596 € ; stop 26.3367 € ; TP1 30.9054 € ; TP2 32.4283 € ; montant 195.21 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 5.571/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GMT-EUR : 0.007726 € ; score 91.06/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BICO-EUR : 0.019929 € ; score 89.21/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MANA-EUR : 0.078026 € ; score 88.87/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- ARB-EUR : 0.19505 € ; score 85.55/100 ; SURVEILLE ; WICK_SETUP
- TNSR-EUR : 0.033557 € ; score 85.21/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.0099445 | +43.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.38336 | +34.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0019876 | +27.11 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ONDO-EUR | 0.4526 | +24.77 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.58 | +24.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.095687 | +22.95 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 75.58 | +21.22 % | DETECTED_EARLY | NONE | NONE |
| PLUME-EUR | 0.0164326 | +20.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.037308 | +20.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.101535 | +16.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1380 scans ; 590628 observations ; 757 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
