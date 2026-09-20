# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T23:52:41.078665+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T23:52:08.844241+00:00 | âge ticker : 150.6 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25929 € | IGNITION | score 80.18/100 | entrée 7.05/10
  Entrée 0.25945 € ; stop 0.24589 € ; TP1 0.28657 € ; TP2 0.30013 € ; montant 203.11 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 7.239/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NPC-EUR : 0.0213105 € | IGNITION | score 79.67/100 | entrée 7.20/10
  Entrée 0.0213221 € ; stop 0.0204529 € ; TP1 0.0230605 € ; TP2 0.0239297 € ; montant 250.00 € ; risque théorique 11.91 € ; R/R net 1.56.
  Chase risk : 2.362/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- STX-EUR : 0.28862 € ; score 92.73/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 119.98 € ; score 87.82/100 ; SURVEILLE ; seuil achat non atteint
- PROVE-EUR : 0.19965 € ; score 86.96/100 ; SURVEILLE ; SPREAD_RISK
- FIDA-EUR : 0.018273 € ; score 84.96/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, SELLER_HEAVY_BOOK
- COW-EUR : 0.13725 € ; score 83.97/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.0327 | +49.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008166 | +33.56 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.2428 | +31.58 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.054101 | +23.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49075 | +22.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.050428 | +20.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.034441 | +18.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.028312 | +17.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6445 | +16.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.125749 | +15.77 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1031 scans ; 441943 observations ; 278 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
