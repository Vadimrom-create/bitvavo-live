# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T13:10:18.082574+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-09-24T13:09:49.498757+00:00 | âge ticker : 146.9 s | durée : 148.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ARB-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : BELOW_EXCHANGE_MINIMUM
- RAY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.17924 € | IGNITION | score 91.57/100 | entrée 7.85/10
  Entrée 0.1793 € ; stop 0.17141 € ; TP1 0.19507 € ; TP2 0.20296 € ; montant 235.99 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 2.511/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ICP-EUR : 2.6771 € | IGNITION | score 88.55/100 | entrée 7.45/10
  Entrée 2.6806 € ; stop 2.5541 € ; TP1 2.9336 € ; TP2 3.0601 € ; montant 222.12 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.652/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ARB-EUR : 0.19025 € ; score 90.63/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : 0.85118 € ; score 90.51/100 ; SURVEILLE ; seuil achat non atteint
- OP-EUR : 0.11068 € ; score 89.50/100 ; SURVEILLE ; WICK_SETUP
- SKY-EUR : 0.062362 € ; score 87.63/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.079981 € ; score 85.69/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.110696 | +39.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0021393 | +37.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.35271 | +26.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.21996 | +18.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0019301 | +12.54 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.034964 | +11.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LTC-EUR | 59.822 | +10.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.085403 | +9.01 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOSO-EUR | 0.28477 | +8.30 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ARK-EUR | 0.15362 | +8.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1357 scans ; 580819 observations ; 716 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
