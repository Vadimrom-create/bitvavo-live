# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T07:32:25.987966+00:00
État : OK | marchés EUR : 426 | V4 : 378 | données valides : 426
Récupération : 2026-09-21T07:31:56.687514+00:00 | âge ticker : 150.3 s | durée : 151.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : 0.6733 € | IGNITION | score 83.80/100 | entrée 7.30/10
  Entrée 0.6718 € ; stop 0.6365 € ; TP1 0.7424 € ; TP2 0.7777 € ; montant 202.15 € ; risque théorique 12.00 € ; R/R net 1.65.
  Chase risk : 4.882/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AZTEC-EUR : 0.014456 € ; score 90.96/100 ; SURVEILLE ; LOW_LIQUIDITY
- AVNT-EUR : 0.09948 € ; score 89.76/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.50223 € ; score 86.75/100 ; SURVEILLE ; seuil achat non atteint
- BCH-EUR : 221.87 € ; score 86.45/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.062175 € ; score 86.29/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.056058 | +68.18 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0009307 | +53.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.26227 | +43.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.059321 | +36.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.54133 | +31.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.031293 | +29.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029202 | +24.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7147 | +23.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 29.1981 | +21.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.03648 | +18.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1056 scans ; 452593 observations ; 328 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
