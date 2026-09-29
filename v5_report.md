# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T07:23:51.308276+00:00
État : OK | marchés EUR : 428 | V4 : 392 | données valides : 428
Récupération : 2026-09-29T07:22:48.489445+00:00 | âge ticker : 186.5 s | durée : 187.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- AVAX-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- GALA-EUR : WICK_SETUP, STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : BELOW_EXCHANGE_MINIMUM
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, BELOW_EXCHANGE_MINIMUM
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.43935 € | IGNITION | score 90.80/100 | entrée 7.80/10
  Entrée 0.43994 € ; stop 0.41329 € ; TP1 0.49324 € ; TP2 0.51989 € ; montant 178.14 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 6.605/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PEAQ-EUR : 0.038016 € | IGNITION | score 90.70/100 | entrée 7.10/10
  Entrée 0.038024 € ; stop 0.036172 € ; TP1 0.041728 € ; TP2 0.04358 € ; montant 216.08 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.28/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- W-EUR : 0.012831 € ; score 92.10/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.72079 € ; score 88.86/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.459 € ; score 88.24/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM
- AZTEC-EUR : 0.016651 € ; score 88.02/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 274.16 € ; score 87.67/100 ; SURVEILLE ; WICK_SETUP, BELOW_EXCHANGE_MINIMUM

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.1522 | +29.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.2546 | +24.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35099 | +21.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| POND-EUR | 0.001534 | +20.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.103346 | +19.70 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.26534 | +18.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.092265 | +15.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.15008 | +15.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 1.9872 | +11.72 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.61502 | +11.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1753 scans ; 749957 observations ; 1284 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
