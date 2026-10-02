# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T05:43:55.935373+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T05:43:25.103129+00:00 | âge ticker : 151.3 s | durée : 152.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 161.17 € | IGNITION | score 82.34/100 | entrée 7.40/10
  Entrée 161.33 € ; stop 154.15 € ; TP1 175.69 € ; TP2 182.87 € ; montant 233.69 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 4.288/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAIA-EUR : 0.033171 € ; score 92.42/100 ; SURVEILLE ; seuil achat non atteint
- KITE-EUR : 0.13173 € ; score 89.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- W-EUR : 0.012055 € ; score 87.58/100 ; SURVEILLE ; seuil achat non atteint
- DUSK-EUR : 0.0788 € ; score 86.68/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- SEI-EUR : 0.063384 € ; score 86.60/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00063662 | +145.44 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.132679 | +55.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.030285 | +35.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.45737 | +33.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04726 | +18.86 % | DETECTED_EARLY | NONE | NONE |
| ALICE-EUR | 0.1697 | +14.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20694 | +13.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.158652 | +11.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.825 | +11.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.50995 | +11.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1959 scans ; 838448 observations ; 1526 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
