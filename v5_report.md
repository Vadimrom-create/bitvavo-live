# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T22:55:15.213262+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T22:54:44.838456+00:00 | âge ticker : 152.4 s | durée : 153.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.3421 € | IGNITION | score 78.31/100 | entrée 7.45/10
  Entrée 4.3457 € ; stop 4.1458 € ; TP1 4.7454 € ; TP2 4.9453 € ; montant 227.11 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 2.122/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CC-EUR : 0.11952 € ; score 94.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : 0.104796 € ; score 91.54/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- C-EUR : 0.080177 € ; score 90.73/100 ; SURVEILLE ; seuil achat non atteint
- KSM-EUR : 4.1934 € ; score 89.05/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- FARTCOIN-EUR : 0.16816 € ; score 88.18/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016 | +95.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006652 | +49.95 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.129002 | +48.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 125.56 | +46.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019326 | +37.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063526 | +24.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.044324 | +21.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.005964 | +15.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.65993 | +14.57 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.52648 | +14.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1569 scans ; 671331 observations ; 1052 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
