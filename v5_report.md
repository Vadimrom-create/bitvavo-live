# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T12:26:09.508141+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 427
Récupération : 2026-09-25T12:25:38.775075+00:00 | âge ticker : 145.5 s | durée : 146.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : EXTENDED_24H, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : 2.4576 € | IGNITION | score 94.41/100 | entrée 6.85/10
  Entrée 2.4549 € ; stop 2.3582 € ; TP1 2.6482 € ; TP2 2.7449 € ; montant 250.00 € ; risque théorique 11.56 € ; R/R net 1.55.
  Chase risk : 5.174/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- UNI-EUR : 8.5869 € | IGNITION | score 87.66/100 | entrée 7.40/10
  Entrée 8.5956 € ; stop 8.0853 € ; TP1 9.6161 € ; TP2 10.1264 € ; montant 181.38 € ; risque théorique 12.00 € ; R/R net 1.68.
  Chase risk : 7.374/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XRP-EUR : 1.40962 € | IGNITION | score 83.09/100 | entrée 7.85/10
  Entrée 1.40952 € ; stop 1.34996 € ; TP1 1.52864 € ; TP2 1.5882 € ; montant 8.90 € ; risque théorique 0.44 € ; R/R net 1.57.
  Chase risk : 4.342/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- INJ-EUR : 7.2288 € ; score 91.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVA-EUR : 0.23617 € ; score 87.41/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- XDC-EUR : 0.026923 € ; score 87.26/100 ; SURVEILLE ; WICK_SETUP
- STX-EUR : 0.28855 € ; score 86.94/100 ; SURVEILLE ; WICK_SETUP
- SENT-EUR : 0.019531 € ; score 86.15/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.67114 | +33.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.20156 | +32.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 84.661 | +30.44 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.060636 | +28.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.098371 | +26.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FET-EUR | 0.21084 | +20.01 % | DETECTED_EARLY | NONE | NONE |
| PIXEL-EUR | 0.0055255 | +19.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.47899 | +19.20 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.039111 | +19.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DEEP-EUR | 0.01959 | +18.89 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1443 scans ; 617529 observations ; 836 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
