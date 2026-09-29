# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T00:02:36.981256+00:00
État : OK | marchés EUR : 428 | V4 : 399 | données valides : 428
Récupération : 2026-09-29T00:02:05.886917+00:00 | âge ticker : 157.6 s | durée : 158.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.20424 € | IGNITION | score 86.11/100 | entrée 7.50/10
  Entrée 0.20436 € ; stop 0.19559 € ; TP1 0.2219 € ; TP2 0.23067 € ; montant 241.14 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.295/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- VIRTUAL-EUR : 0.72838 € ; score 90.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.7128 € ; score 89.75/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RED-EUR : 0.14406 € ; score 89.00/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- SUPER-EUR : 0.17041 € ; score 88.32/100 ; SURVEILLE ; SPREAD_RISK
- XVG-EUR : 0.0027529 € ; score 87.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.2667 | +34.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.107435 | +27.56 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.11924 | +13.83 % | DETECTED_EARLY | NONE | NONE |
| LINK-EUR | 13.6152 | +10.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.25525 | +10.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.001813 | +8.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| CRV-EUR | 0.33521 | +7.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XLM-EUR | 0.20424 | +7.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.048961 | +7.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.0206338 | +6.45 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1731 scans ; 740541 observations ; 1270 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
