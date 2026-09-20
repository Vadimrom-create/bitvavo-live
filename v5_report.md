# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T20:24:29.896402+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 426
Récupération : 2026-09-20T20:23:58.408422+00:00 | âge ticker : 142.7 s | durée : 144.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0037432 € | IGNITION | score 87.01/100 | entrée 6.90/10
  Entrée 0.0037444 € ; stop 0.0035883 € ; TP1 0.0040566 € ; TP2 0.0042127 € ; montant 247.20 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 6.049/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MERL-EUR : 0.022603 € ; score 92.80/100 ; SURVEILLE ; seuil achat non atteint
- ZIG-EUR : 0.045728 € ; score 90.22/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : 2.2156 € ; score 88.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MANA-EUR : 0.072049 € ; score 88.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 51.111 € ; score 86.55/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.034129 | +58.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.25738 | +40.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007992 | +29.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.035528 | +25.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.05426 | +23.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0031171 | +22.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.043073 | +17.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.8658 | +16.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.5933 | +16.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.027791 | +16.27 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1014 scans ; 434701 observations ; 259 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
