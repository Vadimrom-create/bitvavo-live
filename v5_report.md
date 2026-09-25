# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T09:41:15.833829+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T09:40:51.916332+00:00 | âge ticker : 144.2 s | durée : 145.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- W-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XRP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : 7.154 € | IGNITION | score 82.40/100 | entrée 6.85/10
  Entrée 7.1313 € ; stop 6.8487 € ; TP1 7.6965 € ; TP2 7.9791 € ; montant 250.00 € ; risque théorique 11.62 € ; R/R net 1.55.
  Chase risk : 3.397/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COMP-EUR : 20.971 € ; score 93.11/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.4041 € ; score 90.99/100 ; SURVEILLE ; seuil achat non atteint
- RAY-EUR : 1.82506 € ; score 89.98/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DUSK-EUR : 0.077306 € ; score 89.15/100 ; SURVEILLE ; WICK_SETUP
- FARTCOIN-EUR : 0.16712 € ; score 88.77/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.72357 | +45.02 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 84.798 | +36.43 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.102727 | +33.33 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.041544 | +31.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.49194 | +31.30 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.051151 | +22.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.18291 | +21.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20689 | +20.15 % | DETECTED_EARLY | NONE | NONE |
| DBR-EUR | 0.021149 | +19.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WAXP-EUR | 0.0056112 | +18.15 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1434 scans ; 613686 observations ; 825 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
