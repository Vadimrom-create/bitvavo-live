# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T03:42:08.459164+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-10-01T03:41:08.414986+00:00 | âge ticker : 187.5 s | durée : 189.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.114725 € | IGNITION | score 92.94/100 | entrée 6.90/10
  Entrée 0.11488 € ; stop 0.109036 € ; TP1 0.126568 € ; TP2 0.132412 € ; montant 208.00 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 3.665/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVAX-EUR : 9.8139 € ; score 88.91/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.20454 € ; score 88.44/100 ; SURVEILLE ; WICK_SETUP
- PEPE-EUR : 3.8418e-06 € ; score 88.12/100 ; SURVEILLE ; WICK_SETUP
- KMNO-EUR : 0.038765 € ; score 87.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DOGE-EUR : 0.084289 € ; score 86.38/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0871 | +89.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34699 | +45.18 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.009178 | +35.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.42396 | +24.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33912 | +22.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028446 | +21.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0186508 | +19.07 % | DETECTED_EARLY | NONE | NONE |
| SOON-EUR | 0.4175 | +16.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0617425 | +16.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ESP-EUR | 0.098487 | +13.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1883 scans ; 805768 observations ; 1438 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
