# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T12:00:00.888713+00:00
État : OK | marchés EUR : 429 | V4 : 396 | données valides : 428
Récupération : 2026-09-29T11:59:35.072872+00:00 | âge ticker : 154.9 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.3332 € | IGNITION | score 90.77/100 | entrée 7.85/10
  Entrée 4.3226 € ; stop 4.1551 € ; TP1 4.6576 € ; TP2 4.8251 € ; montant 250.00 € ; risque théorique 11.40 € ; R/R net 1.54.
  Chase risk : 4.33/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XPL-EUR : 0.089521 € | IGNITION | score 87.50/100 | entrée 7.35/10
  Entrée 0.089575 € ; stop 0.086414 € ; TP1 0.095897 € ; TP2 0.099058 € ; montant 250.00 € ; risque théorique 10.54 € ; R/R net 1.50.
  Chase risk : 2.246/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.104165 € ; score 92.33/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.72995 € ; score 91.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.70547 € ; score 89.61/100 ; SURVEILLE ; seuil achat non atteint
- ACH-EUR : 0.0054837 € ; score 89.18/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SEI-EUR : 0.066836 € ; score 88.83/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00194 | +54.63 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| 0G-EUR | 0.28795 | +30.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.101987 | +27.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZBCN-EUR | 0.002166 | +22.65 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.61086 | +22.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.34586 | +19.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.22022 | +18.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.0652 | +16.89 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AAVE-EUR | 151.25 | +16.40 % | DETECTED_EARLY | NONE | NONE |
| INIT-EUR | 0.087612 | +13.74 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1767 scans ; 755953 observations ; 1311 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
