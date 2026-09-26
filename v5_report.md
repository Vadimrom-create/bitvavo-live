# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T10:37:22.238638+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T10:36:52.419027+00:00 | âge ticker : 144.9 s | durée : 145.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.104233 € | IGNITION | score 82.54/100 | entrée 6.90/10
  Entrée 0.104337 € ; stop 0.099271 € ; TP1 0.114469 € ; TP2 0.119535 € ; montant 216.67 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 4.844/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WAL-EUR : 0.033331 € ; score 93.77/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.42823 € ; score 93.42/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FLR-EUR : 0.0064592 € ; score 89.21/100 ; SURVEILLE ; seuil achat non atteint
- ZK-EUR : 0.01146 € ; score 89.16/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- TURBO-EUR : 0.0009496 € ; score 88.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.002045 | +159.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020428 | +73.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.064756 | +33.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.070037 | +30.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24156 | +25.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.24882 | +24.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.7922 | +16.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.5307 | +14.23 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WAXP-EUR | 0.0060915 | +13.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CC-EUR | 0.11848 | +13.23 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1524 scans ; 652116 observations ; 975 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
