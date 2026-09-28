# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T11:41:52.761296+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 427
Récupération : 2026-09-28T11:41:21.661735+00:00 | âge ticker : 146.9 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : 12.3791 € | IGNITION | score 80.87/100 | entrée 7.15/10
  Entrée 12.3668 € ; stop 11.8277 € ; TP1 13.4449 € ; TP2 13.984 € ; montant 237.91 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.067/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.10962 € ; score 90.65/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2344.79 € ; score 84.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KSM-EUR : 4.0006 € ; score 83.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IMX-EUR : 0.15713 € ; score 83.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- TRIA-EUR : 0.003756 € ; score 83.35/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 221.558 | +53.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.103331 | +24.29 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 10.0047 | +16.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0019 | +15.26 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| GRT-EUR | 0.027948 | +14.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0044137 | +12.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.27225 | +11.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.014627 | +11.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.114331 | +10.92 % | DETECTED_EARLY | NONE | NONE |
| XDC-EUR | 0.030072 | +9.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1692 scans ; 723852 observations ; 1243 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
