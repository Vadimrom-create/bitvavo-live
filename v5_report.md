# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T04:43:19.950644+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-23T04:42:53.028568+00:00 | âge ticker : 139.0 s | durée : 140.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XRP-EUR : 1.44341 € | IGNITION | score 89.46/100 | entrée 7.95/10
  Entrée 1.44341 € ; stop 1.38126 € ; TP1 1.56771 € ; TP2 1.62986 € ; montant 240.45 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.419/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.037264 € ; score 92.91/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : 0.9968 € ; score 92.31/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.00531 € ; score 92.13/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HYPE-EUR : 85.396 € ; score 89.74/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RPL-EUR : 1.7499 € ; score 89.40/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| USELESS-EUR | 0.308794 | +35.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.081659 | +34.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 297.97 | +29.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31032 | +29.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.01928 | +24.08 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FLOCK-EUR | 0.076901 | +21.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2418 | +21.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.49398 | +20.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.15899 | +19.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.019704 | +18.59 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1243 scans ; 532255 observations ; 592 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
