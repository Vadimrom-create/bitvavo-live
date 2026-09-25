# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T12:49:08.739239+00:00
État : OK | marchés EUR : 427 | V4 : 396 | données valides : 427
Récupération : 2026-09-25T12:48:33.049623+00:00 | âge ticker : 153.4 s | durée : 154.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : 2.471 € | IGNITION | score 89.44/100 | entrée 6.60/10
  Entrée 2.46 € ; stop 2.3631 € ; TP1 2.6537 € ; TP2 2.7506 € ; montant 250.00 € ; risque théorique 11.56 € ; R/R net 1.55.
  Chase risk : 3.419/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- INJ-EUR : 7.2645 € | IGNITION | score 85.24/100 | entrée 6.90/10
  Entrée 7.2789 € ; stop 7.0232 € ; TP1 7.7903 € ; TP2 8.046 € ; montant 250.00 € ; risque théorique 10.50 € ; R/R net 1.50.
  Chase risk : 4.001/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XRP-EUR : 1.41857 € | IGNITION | score 82.19/100 | entrée 7.60/10
  Entrée 1.41729 € ; stop 1.35743 € ; TP1 1.53701 € ; TP2 1.59687 € ; montant 39.43 € ; risque théorique 1.94 € ; R/R net 1.57.
  Chase risk : 4.842/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COMP-EUR : 21.128 € ; score 86.00/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.10542 € ; score 85.86/100 ; SURVEILLE ; seuil achat non atteint
- ZK-EUR : 0.010959 € ; score 85.25/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, STABILITY_HOLD
- SENT-EUR : 0.019659 € ; score 84.51/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : 0.016139 € ; score 83.94/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.062287 | +35.78 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.68472 | +34.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.20625 | +33.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 83.83 | +27.92 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.098657 | +25.95 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48137 | +21.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.21228 | +21.55 % | DETECTED_EARLY | NONE | NONE |
| PIXEL-EUR | 0.0056743 | +21.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HUMA-EUR | 0.025366 | +21.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DEEP-EUR | 0.01977 | +19.88 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1444 scans ; 617956 observations ; 840 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
