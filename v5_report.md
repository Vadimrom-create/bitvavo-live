# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T01:27:45.498425+00:00
État : OK | marchés EUR : 429 | V4 : 394 | données valides : 429
Récupération : 2026-09-30T01:26:46.845252+00:00 | âge ticker : 175.1 s | durée : 176.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.72924 € | IGNITION | score 86.82/100 | entrée 7.45/10
  Entrée 1.72664 € ; stop 1.66578 € ; TP1 1.84835 € ; TP2 1.90921 € ; montant 250.00 € ; risque théorique 10.53 € ; R/R net 1.50.
  Chase risk : 2.349/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ALGO-EUR : 0.112096 € ; score 93.25/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 1.03706 € ; score 91.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.14323 € ; score 90.77/100 ; SURVEILLE ; LOW_LIQUIDITY
- PEAQ-EUR : 0.037417 € ; score 90.30/100 ; SURVEILLE ; WICK_SETUP
- XVG-EUR : 0.0028202 € ; score 89.14/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.37097 | +46.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.1313 | +36.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016309 | +30.47 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65287 | +26.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0052729 | +24.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 238.245 | +23.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.30455 | +22.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEW-EUR | 0.00047697 | +18.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.5616 | +17.29 % | DETECTED_EARLY | NONE | NONE |
| ZBCN-EUR | 0.0022453 | +16.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1807 scans ; 773113 observations ; 1350 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
