# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T23:59:29.854977+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-10-02T23:58:59.409677+00:00 | âge ticker : 153.3 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- AXS-EUR : 1.1015 € | IGNITION | score 89.73/100 | entrée 7.80/10
  Entrée 1.1016 € ; stop 1.0603 € ; TP1 1.1841 € ; TP2 1.2254 € ; montant 250.00 € ; risque théorique 11.09 € ; R/R net 1.52.
  Chase risk : 4.501/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WIF-EUR : 0.22171 € | IGNITION | score 86.29/100 | entrée 6.35/10
  Entrée 0.22158 € ; stop 0.21247 € ; TP1 0.2398 € ; TP2 0.24891 € ; montant 250.00 € ; risque théorique 11.99 € ; R/R net 1.56.
  Chase risk : 5.046/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MON-EUR : 0.028858 € ; score 93.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IMX-EUR : 0.15685 € ; score 88.60/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SENT-EUR : 0.019111 € ; score 87.60/100 ; SURVEILLE ; seuil achat non atteint
- W-EUR : 0.011856 € ; score 87.10/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.553 € ; score 87.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.061424 | +53.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023692 | +18.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0059474 | +14.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.089105 | +13.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.029942 | +12.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14704 | +11.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.49538 | +10.04 % | DETECTED_EARLY | NONE | NONE |
| SPK-EUR | 0.023067 | +9.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.28679 | +9.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AXS-EUR | 1.1015 | +8.54 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2015 scans ; 862376 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
