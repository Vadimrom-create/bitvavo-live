# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T03:58:38.971509+00:00
État : OK | marchés EUR : 426 | V4 : 372 | données valides : 426
Récupération : 2026-09-21T03:58:10.107559+00:00 | âge ticker : 151.2 s | durée : 152.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- OP-EUR : 0.11027 € | IGNITION | score 82.51/100 | entrée 7.10/10
  Entrée 0.11102 € ; stop 0.10681 € ; TP1 0.11943 € ; TP2 0.12364 € ; montant 250.00 € ; risque théorique 11.20 € ; R/R net 1.53.
  Chase risk : 0.869/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MERL-EUR : 0.023098 € ; score 94.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZK-EUR : 0.0105 € ; score 89.24/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- GALA-EUR : 0.0017367 € ; score 86.52/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- CC-EUR : 0.09769 € ; score 85.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SKL-EUR : 0.0040028 € ; score 85.32/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0012145 | +97.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZETA-EUR | 0.049869 | +48.08 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FTT-EUR | 0.25849 | +41.65 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030789 | +30.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.8149 | +25.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.054285 | +21.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.0696 | +21.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.47254 | +20.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49654 | +20.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.029547 | +20.01 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1045 scans ; 447907 observations ; 301 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
