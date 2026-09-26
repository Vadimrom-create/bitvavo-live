# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T15:19:05.518456+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-26T15:18:13.042979+00:00 | âge ticker : 168.7 s | durée : 169.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, PORTFOLIO_LIMIT
- LDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : PORTFOLIO_LIMIT
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : PORTFOLIO_LIMIT
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.7179 € | IGNITION | score 92.84/100 | entrée 8.05/10
  Entrée 9.7243 € ; stop 9.3623 € ; TP1 10.4483 € ; TP2 10.8103 € ; montant 250.00 € ; risque théorique 11.02 € ; R/R net 1.52.
  Chase risk : 2.872/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DOT-EUR : 1.1122 € | IGNITION | score 90.75/100 | entrée 7.40/10
  Entrée 1.1147 € ; stop 1.0662 € ; TP1 1.2117 € ; TP2 1.2602 € ; montant 238.30 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.26/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WIF-EUR : 0.22335 € | IGNITION | score 88.99/100 | entrée 6.90/10
  Entrée 0.22366 € ; stop 0.21537 € ; TP1 0.24023 € ; TP2 0.24852 € ; montant 22.21 € ; risque théorique 0.98 € ; R/R net 1.52.
  Chase risk : 3.27/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- VET-EUR : 0.0084188 € ; score 92.10/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CHZ-EUR : 0.014899 € ; score 91.65/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.22752 € ; score 91.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EGLD-EUR : 4.223 € ; score 91.35/100 ; SURVEILLE ; SPREAD_RISK
- HOT-EUR : 0.00039803 € ; score 91.13/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019382 | +132.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020434 | +62.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.115999 | +32.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005699 | +28.94 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.063453 | +28.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.23353 | +19.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FIL-EUR | 1.0552 | +18.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.46728 | +17.93 % | DETECTED_EARLY | NONE | NONE |
| HUMA-EUR | 0.026017 | +17.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.65521 | +16.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1541 scans ; 659375 observations ; 1006 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
