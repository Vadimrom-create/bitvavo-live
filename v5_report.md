# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T05:25:12.697632+00:00
État : OK | marchés EUR : 427 | V4 : 382 | données valides : 427
Récupération : 2026-09-27T05:24:42.819640+00:00 | âge ticker : 155.1 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RENDER-EUR : 1.7799 € ; score 94.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 136.8 € ; score 92.78/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.5154 € ; score 92.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HOT-EUR : 0.00040985 € ; score 92.21/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ICP-EUR : 2.8088 € ; score 91.77/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 165.702 | +89.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019607 | +48.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.26865 | +46.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006118 | +36.53 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.73352 | +26.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007227 | +25.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AGI-EUR | 0.00631 | +22.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAIKO-EUR | 0.09869 | +21.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.00128 | +21.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.857 | +17.71 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1591 scans ; 680725 observations ; 1084 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
