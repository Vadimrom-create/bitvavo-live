# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T14:56:37.641739+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-21T14:56:05.009818+00:00 | âge ticker : 150.9 s | durée : 152.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0077374 € | IGNITION | score 81.45/100 | entrée 7.10/10
  Entrée 0.0077506 € ; stop 0.0074505 € ; TP1 0.0083508 € ; TP2 0.0086509 € ; montant 250.00 € ; risque théorique 11.40 € ; R/R net 1.54.
  Chase risk : 2.026/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- STX-EUR : 0.29501 € ; score 93.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GRASS-EUR : 0.32888 € ; score 89.01/100 ; SURVEILLE ; WICK_SETUP
- KAS-EUR : 0.036371 € ; score 86.88/100 ; SURVEILLE ; WICK_SETUP
- ONG-EUR : 0.077917 € ; score 86.65/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- EUL-EUR : 1.26056 € ; score 86.10/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.054399 | +66.23 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.047737 | +50.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0009665 | +34.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.102064 | +32.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.23827 | +30.28 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.057107 | +30.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.031275 | +29.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.052585 | +26.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.90491 | +26.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROVE-EUR | 0.24025 | +24.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1084 scans ; 464521 observations ; 381 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
