# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T07:14:38.865047+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-02T07:14:03.795346+00:00 | âge ticker : 162.2 s | durée : 163.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.116774 € | IGNITION | score 87.07/100 | entrée 6.20/10
  Entrée 0.116769 € ; stop 0.111608 € ; TP1 0.127091 € ; TP2 0.132251 € ; montant 235.09 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RECALL-EUR : 0.042731 € ; score 88.26/100 ; SURVEILLE ; seuil achat non atteint
- SOLV-EUR : 0.0037949 € ; score 87.74/100 ; SURVEILLE ; LOW_LIQUIDITY
- W-EUR : 0.012203 € ; score 87.71/100 ; SURVEILLE ; seuil achat non atteint
- AXS-EUR : 1.0481 € ; score 87.28/100 ; SURVEILLE ; WICK_SETUP
- MANA-EUR : 0.082747 € ; score 86.45/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00070064 | +170.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.122049 | +43.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.51085 | +43.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.83 | +31.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAND-EUR | 0.04774 | +22.10 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SCR-EUR | 0.026663 | +14.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.6885 | +11.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AAVE-EUR | 164.61 | +10.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.19838 | +10.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVX-EUR | 2.1067 | +10.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1963 scans ; 840168 observations ; 1539 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
