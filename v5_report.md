# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T16:43:54.710017+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-09-30T16:43:25.373976+00:00 | âge ticker : 282.8 s | durée : 283.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 1.05178 € | IGNITION | score 90.40/100 | entrée 7.80/10
  Entrée 1.05181 € ; stop 1.0014 € ; TP1 1.15262 € ; TP2 1.20303 € ; montant 219.14 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 3.125/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DOT-EUR : 1.1005 € | IGNITION | score 79.20/100 | entrée 6.30/10
  Entrée 1.1013 € ; stop 1.0594 € ; TP1 1.1851 € ; TP2 1.227 € ; montant 250.00 € ; risque théorique 11.23 € ; R/R net 1.53.
  Chase risk : 2.708/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LPT-EUR : 1.5993 € ; score 91.45/100 ; SURVEILLE ; WICK_SETUP
- WOO-EUR : 0.012155 € ; score 91.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GALA-EUR : 0.0020337 € ; score 91.22/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0165 € ; score 89.38/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7336 € ; score 88.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5616 | +63.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34542 | +44.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0022872 | +28.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.42784 | +24.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007805 | +18.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 265 | +18.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.007559 | +16.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.24999 | +15.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49002 | +14.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0042412 | +13.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1850 scans ; 791578 observations ; 1396 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
