# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T09:45:38.432939+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T09:45:05.077470+00:00 | âge ticker : 147.3 s | durée : 148.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : 0.0209678 € | IGNITION | score 87.93/100 | entrée 7.05/10
  Entrée 0.0210135 € ; stop 0.0199968 € ; TP1 0.0230469 € ; TP2 0.0240636 € ; montant 217.34 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.264/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WIF-EUR : 0.22516 € | IGNITION | score 78.93/100 | entrée 6.60/10
  Entrée 0.22357 € ; stop 0.20805 € ; TP1 0.2546 € ; TP2 0.27012 € ; montant 157.53 € ; risque théorique 12.00 € ; R/R net 1.72.
  Chase risk : 8.354/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- YFI-EUR : 1988.5 € ; score 85.62/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RECALL-EUR : 0.040249 € ; score 85.56/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0018073 € ; score 85.17/100 ; SURVEILLE ; seuil achat non atteint
- TAIKO-EUR : 0.08118 € ; score 84.28/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INIT-EUR : 0.074813 € ; score 83.38/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017551 | +101.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015041 | +94.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.119134 | +41.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057549 | +37.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46156 | +23.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.22516 | +21.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39463 | +21.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.072321 | +21.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CARV-EUR | 0.040717 | +18.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEPE-EUR | 4.3473e-06 | +18.47 % | DETECTED_EARLY | NONE | NONE |

Historique : 1172 scans ; 502009 observations ; 471 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
