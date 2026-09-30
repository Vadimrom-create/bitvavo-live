# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T12:58:10.398014+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T12:57:40.509069+00:00 | âge ticker : 150.5 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : PORTFOLIO_LIMIT
- ENA-EUR : WICK_SETUP, PORTFOLIO_LIMIT
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : PORTFOLIO_LIMIT
- PENGU-EUR : PORTFOLIO_LIMIT
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : PORTFOLIO_LIMIT
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.7512 € | IGNITION | score 92.82/100 | entrée 8.05/10
  Entrée 1.75 € ; stop 1.6882 € ; TP1 1.8736 € ; TP2 1.9354 € ; montant 250.00 € ; risque théorique 10.55 € ; R/R net 1.50.
  Chase risk : 2.321/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.20178 € | IGNITION | score 91.94/100 | entrée 7.55/10
  Entrée 0.20197 € ; stop 0.19126 € ; TP1 0.22339 € ; TP2 0.2341 € ; montant 200.53 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 6.279/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SUI-EUR : 1.04813 € | IGNITION | score 91.67/100 | entrée 7.80/10
  Entrée 1.04885 € ; stop 0.99805 € ; TP1 1.15045 € ; TP2 1.20125 € ; montant 26.28 € ; risque théorique 1.45 € ; R/R net 1.62.
  Chase risk : 6.595/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AAVE-EUR : 145.24 € ; score 94.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 13.0133 € ; score 94.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.20333 € ; score 94.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.983 € ; score 92.93/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : 0.68563 € ; score 92.92/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ARK-EUR | 0.33769 | +57.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 1.4127 | +52.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.33081 | +38.41 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.39112 | +35.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 272.344 | +21.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOMI-EUR | 0.21502 | +20.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008005 | +19.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.084638 | +15.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.088885 | +14.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.065701 | +13.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1840 scans ; 787278 observations ; 1373 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
