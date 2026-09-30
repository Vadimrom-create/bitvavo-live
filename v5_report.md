# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T13:44:17.289914+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 429
Récupération : 2026-09-30T13:43:36.000367+00:00 | âge ticker : 202.2 s | durée : 203.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ETHFI-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.19804 € | IGNITION | score 80.77/100 | entrée 7.55/10
  Entrée 0.19827 € ; stop 0.1912 € ; TP1 0.21241 € ; TP2 0.21947 € ; montant 250.00 € ; risque théorique 10.63 € ; R/R net 1.51.
  Chase risk : 4.405/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SUI-EUR : 1.03043 € | IGNITION | score 78.62/100 | entrée 7.85/10
  Entrée 1.03379 € ; stop 0.99702 € ; TP1 1.10733 € ; TP2 1.1441 € ; montant 250.00 € ; risque théorique 10.61 € ; R/R net 1.51.
  Chase risk : 4.73/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ACH-EUR : 0.0054328 € ; score 90.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ENS-EUR : 6.1996 € ; score 89.22/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- ESP-EUR : 0.090268 € ; score 88.67/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- WAL-EUR : 0.03007 € ; score 88.44/100 ; SURVEILLE ; LOW_LIQUIDITY
- ZRO-EUR : 1.5663 € ; score 87.50/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ARK-EUR | 0.33428 | +55.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 1.3685 | +49.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.32696 | +36.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.40917 | +35.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0021426 | +18.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007908 | +17.94 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 262.497 | +15.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PROM-EUR | 5.7559 | +14.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOMI-EUR | 0.201 | +12.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.086401 | +11.86 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1842 scans ; 788138 observations ; 1378 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
