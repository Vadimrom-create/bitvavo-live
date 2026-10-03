# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T09:21:41.370288+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T09:21:05.017205+00:00 | âge ticker : 146.3 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.505 € | IGNITION | score 81.28/100 | entrée 7.05/10
  Entrée 0.50495 € ; stop 0.48665 € ; TP1 0.54155 € ; TP2 0.55985 € ; montant 250.00 € ; risque théorique 10.78 € ; R/R net 1.51.
  Chase risk : 0.963/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AAVE-EUR : 161 € ; score 83.97/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.21552 € ; score 83.70/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : 0.39863 € ; score 83.13/100 ; SURVEILLE ; seuil achat non atteint
- IMX-EUR : 0.1685 € ; score 83.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FLUID-EUR : 1.4702 € ; score 80.53/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.065488 | +16.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.0062551 | +13.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.065062 | +12.79 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 233.293 | +11.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.006198 | +11.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0636159 | +7.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.1668 | +7.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.21552 | +7.61 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| WLD-EUR | 0.505 | +6.31 % | DETECTED_EARLY | NONE | NONE |
| IMX-EUR | 0.1685 | +6.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2040 scans ; 873026 observations ; 1607 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
