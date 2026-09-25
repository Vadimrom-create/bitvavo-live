# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T00:18:14.105731+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T00:17:42.809620+00:00 | âge ticker : 154.2 s | durée : 155.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- KMNO-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2062 € | IGNITION | score 91.40/100 | entrée 7.40/10
  Entrée 0.2058 € ; stop 0.1894 € ; TP1 0.2386 € ; TP2 0.255 € ; montant 138.87 € ; risque théorique 12.00 € ; R/R net 1.76.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XLM-EUR : 0.19356 € | IGNITION | score 85.15/100 | entrée 7.60/10
  Entrée 0.19363 € ; stop 0.18612 € ; TP1 0.20864 € ; TP2 0.21615 € ; montant 250.00 € ; risque théorique 11.41 € ; R/R net 1.54.
  Chase risk : 4.496/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.035316 € ; score 91.39/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0082794 € ; score 90.58/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 130 € ; score 88.86/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.100146 € ; score 85.66/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DRIFT-EUR : 0.016544 € ; score 82.31/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.066992 | +61.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 78.722 | +27.23 % | DETECTED_EARLY | NONE | NONE |
| ONDO-EUR | 0.46118 | +27.08 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.100533 | +26.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.61406 | +25.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.17189 | +24.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.037106 | +21.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.008405 | +21.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FET-EUR | 0.2034 | +19.53 % | DETECTED_EARLY | NONE | NONE |
| DBR-EUR | 0.021835 | +18.96 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1402 scans ; 600022 observations ; 789 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
