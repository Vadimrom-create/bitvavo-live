# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T23:46:05.799963+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-10-02T23:45:38.731531+00:00 | âge ticker : 156.2 s | durée : 157.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.22181 € | IGNITION | score 87.15/100 | entrée 6.80/10
  Entrée 0.22172 € ; stop 0.21247 € ; TP1 0.24022 € ; TP2 0.24947 € ; montant 247.05 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 5.046/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WLD-EUR : 0.4911 € | IGNITION | score 83.31/100 | entrée 7.25/10
  Entrée 0.49117 € ; stop 0.47353 € ; TP1 0.52645 € ; TP2 0.54409 € ; montant 250.00 € ; risque théorique 10.70 € ; R/R net 1.51.
  Chase risk : 3.388/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FLUID-EUR : 1.4175 € ; score 93.89/100 ; SURVEILLE ; WICK_SETUP
- SYRUP-EUR : 0.21503 € ; score 89.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CELO-EUR : 0.089607 € ; score 89.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SPK-EUR : 0.023067 € ; score 87.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAIA-EUR : 0.031932 € ; score 87.89/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.059993 | +49.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023398 | +16.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.08953 | +13.56 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.00587 | +12.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.029788 | +11.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.1473 | +11.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.023067 | +9.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.4911 | +9.55 % | DETECTED_EARLY | NONE | NONE |
| CNPY-EUR | 0.2844 | +8.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.5318 | +8.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2014 scans ; 861950 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
