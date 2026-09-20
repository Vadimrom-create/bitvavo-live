# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T14:11:48.521919+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 34
Récupération : 2026-09-20T14:11:16.910248+00:00 | âge ticker : 149.2 s | durée : 150.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 35/426 ; 15 min 78/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_5M
- STRK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- ALGO-EUR : 0.093004 € | IGNITION | score 80.91/100 | entrée 7.55/10
  Entrée 0.093008 € ; stop 0.088639 € ; TP1 0.101745 € ; TP2 0.106114 € ; montant 223.01 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 3.845/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- HBAR-EUR : 0.076083 € | IGNITION | score 79.92/100 | entrée 6.40/10
  Entrée 0.076088 € ; stop 0.070268 € ; TP1 0.087728 € ; TP2 0.093548 € ; montant 144.19 € ; risque théorique 12.00 € ; R/R net 1.75.
  Chase risk : 8.286/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- VET-EUR : 0.00709 € ; score 84.19/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.027271 € ; score 79.18/100 ; SURVEILLE ; WICK_SETUP
- ETH-EUR : 2248.48 € ; score 75.15/100 ; SURVEILLE ; STABILITY_HOLD
- HYPE-EUR : 79.224 € ; score 74.15/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0037994 | +82.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.46718 | +24.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.3466 | +15.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| C-EUR | 0.06923 | +15.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTSI-EUR | 0.025303 | +10.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.081082 | +10.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0006667 | +10.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HBAR-EUR | 0.076083 | +8.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.041094 | +7.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.030274 | +7.48 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 986 scans ; 422773 observations ; 230 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
