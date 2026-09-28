# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T08:56:48.071038+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 427
Récupération : 2026-09-28T08:56:11.485107+00:00 | âge ticker : 150.7 s | durée : 151.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GRAM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : 0.10795 € | IGNITION | score 92.29/100 | entrée 5.85/10
  Entrée 0.108066 € ; stop 0.100606 € ; TP1 0.122985 € ; TP2 0.130445 € ; montant 158.33 € ; risque théorique 12.00 € ; R/R net 1.72.
  Chase risk : 3.687/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TNSR-EUR : 0.03455 € ; score 89.18/100 ; SURVEILLE ; seuil achat non atteint
- ZKJ-EUR : 0.0056 € ; score 82.71/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- GRAM-EUR : 1.432 € ; score 82.21/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0077489 € ; score 82.01/100 ; SURVEILLE ; seuil achat non atteint
- GLMR-EUR : 0.00705 € ; score 80.51/100 ; SURVEILLE ; SPREAD_RISK, VERY_SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 1.133 | +42.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 213.384 | +33.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.097755 | +16.79 % | DETECTED_EARLY | NONE | NONE |
| AUDIO-EUR | 0.015132 | +16.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.030076 | +12.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.02743 | +11.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0042972 | +10.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016099 | +7.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.5337 | +6.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.28997 | +5.88 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1684 scans ; 720436 observations ; 1237 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
