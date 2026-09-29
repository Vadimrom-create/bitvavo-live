# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T06:11:54.070257+00:00
État : OK | marchés EUR : 428 | V4 : 393 | données valides : 428
Récupération : 2026-09-29T06:10:54.915044+00:00 | âge ticker : 181.3 s | durée : 183.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.4464 € | IGNITION | score 88.13/100 | entrée 7.60/10
  Entrée 9.4491 € ; stop 9.0717 € ; TP1 10.2038 € ; TP2 10.5812 € ; montant 250.00 € ; risque théorique 11.70 € ; R/R net 1.55.
  Chase risk : 1.878/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AAVE-EUR : 135.88 € | IGNITION | score 81.42/100 | entrée 6.80/10
  Entrée 136.34 € ; stop 129 € ; TP1 151.02 € ; TP2 158.36 € ; montant 197.86 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 5.697/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RAY-EUR : 1.66661 € ; score 89.21/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 60.031 € ; score 88.90/100 ; SURVEILLE ; WICK_SETUP
- JASMY-EUR : 0.0044752 € ; score 87.84/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ADA-EUR : 0.21714 € ; score 87.78/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : 0.73716 € ; score 87.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.2783 | +25.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.105182 | +22.16 % | DETECTED_EARLY | NONE | NONE |
| POND-EUR | 0.0015148 | +18.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.26757 | +17.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.34335 | +16.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.118068 | +14.05 % | DETECTED_EARLY | NONE | NONE |
| ARX-EUR | 0.23959 | +12.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.090269 | +9.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0202125 | +9.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.058321 | +9.47 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1750 scans ; 748673 observations ; 1283 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
