# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T17:01:13.509350+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-09-30T17:00:07.080532+00:00 | âge ticker : 195.4 s | durée : 196.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 1.05777 € | IGNITION | score 84.42/100 | entrée 7.25/10
  Entrée 1.05681 € ; stop 1.00267 € ; TP1 1.16509 € ; TP2 1.21923 € ; montant 206.72 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 3.251/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PLUME-EUR : 0.0167044 € ; score 93.06/100 ; SURVEILLE ; seuil achat non atteint
- SEI-EUR : 0.065576 € ; score 91.17/100 ; SURVEILLE ; WICK_SETUP
- ZIG-EUR : 0.047502 € ; score 91.14/100 ; SURVEILLE ; seuil achat non atteint
- RSR-EUR : 0.0015235 € ; score 89.01/100 ; SURVEILLE ; STABILITY_HOLD
- ZRO-EUR : 1.5451 € ; score 87.32/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.564 | +65.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35999 | +50.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.002231 | +24.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008135 | +23.07 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 265.009 | +21.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.41909 | +15.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RED-EUR | 0.16158 | +14.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.48909 | +14.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MERL-EUR | 0.028 | +13.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DEEP-EUR | 0.021124 | +13.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1851 scans ; 792008 observations ; 1410 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
