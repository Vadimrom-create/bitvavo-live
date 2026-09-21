# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T15:31:50.445431+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-21T15:31:21.248445+00:00 | âge ticker : 155.9 s | durée : 156.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : 5.1057e-06 € | IGNITION | score 89.12/100 | entrée 7.00/10
  Entrée 5.1158e-06 € ; stop 4.9175e-06 € ; TP1 5.5124e-06 € ; TP2 5.7107e-06 € ; montant 250.00 € ; risque théorique 11.41 € ; R/R net 1.54.
  Chase risk : 2.973/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- VET-EUR : 0.00777 € | IGNITION | score 81.01/100 | entrée 7.75/10
  Entrée 0.0077866 € ; stop 0.0074495 € ; TP1 0.0084608 € ; TP2 0.0087979 € ; montant 239.33 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 1.899/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CROSS-EUR : 0.127326 € ; score 85.86/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- SENT-EUR : 0.016378 € ; score 84.49/100 ; SURVEILLE ; LOW_LIQUIDITY
- MERL-EUR : 0.024028 € ; score 83.70/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RARE-EUR : 0.011462 € ; score 83.19/100 ; SURVEILLE ; WICK_SETUP
- LDO-EUR : 0.37153 € ; score 83.16/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0023502 | +202.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.053196 | +61.89 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.043376 | +35.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.058688 | +34.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.101619 | +33.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.25514 | +33.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.00093 | +31.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| KMNO-EUR | 0.030625 | +25.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21208 | +23.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUI-EUR | 0.88175 | +21.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1086 scans ; 465373 observations ; 384 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
