# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T13:27:44.531641+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-21T13:27:14.344276+00:00 | âge ticker : 149.7 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 54.457 € | IGNITION | score 88.98/100 | entrée 7.50/10
  Entrée 54.533 € ; stop 52.053 € ; TP1 59.493 € ; TP2 61.973 € ; montant 229.37 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 7.712/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- IOST-EUR : 0.0007762 € ; score 89.27/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- KAS-EUR : 0.036384 € ; score 87.46/100 ; SURVEILLE ; WICK_SETUP
- RAY-EUR : 1.5397 € ; score 86.86/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONG-EUR : 0.078226 € ; score 85.87/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- PEPE-EUR : 3.7379e-06 € ; score 84.88/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZETA-EUR | 0.055704 | +68.71 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.051064 | +63.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010085 | +46.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AIOZ-EUR | 0.108915 | +44.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.057319 | +31.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.05346 | +30.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030856 | +28.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.91071 | +27.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FTT-EUR | 0.23164 | +26.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| DUSK-EUR | 0.077691 | +24.13 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1079 scans ; 462391 observations ; 374 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
