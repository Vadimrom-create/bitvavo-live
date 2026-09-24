# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T16:18:54.864011+00:00
État : OK | marchés EUR : 426 | V4 : 385 | données valides : 426
Récupération : 2026-09-24T16:17:48.846440+00:00 | âge ticker : 182.1 s | durée : 182.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, CORRELATED_OR_UNKNOWN_CORRELATION_REQUIRES_REVIEW
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.085009 € | IGNITION | score 84.18/100 | entrée 7.25/10
  Entrée 0.085013 € ; stop 0.081635 € ; TP1 0.091769 € ; TP2 0.095147 € ; montant 250.00 € ; risque théorique 11.65 € ; R/R net 1.55.
  Chase risk : 2.396/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MAVIA-EUR : 0.030413 € ; score 90.55/100 ; SURVEILLE ; SPREAD_RISK
- SXT-EUR : 0.008235 € ; score 90.08/100 ; SURVEILLE ; SPREAD_RISK
- SOL-EUR : 102.855 € ; score 85.37/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ACH-EUR : 0.0053106 € ; score 84.68/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- CC-EUR : 0.09881 € ; score 84.44/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021043 | +41.60 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.34702 | +31.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| POND-EUR | 0.000975 | +26.25 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.457 | +24.94 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 65.662 | +24.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.101366 | +21.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XPL-EUR | 0.089587 | +17.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.22673 | +17.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.51713 | +17.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.035501 | +17.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1367 scans ; 585079 observations ; 721 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
