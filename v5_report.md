# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T19:06:25.941427+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T19:05:49.672459+00:00 | âge ticker : 151.0 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 250 € | IGNITION | score 84.05/100 | entrée 6.80/10
  Entrée 250.18 € ; stop 240.67 € ; TP1 269.2 € ; TP2 278.71 € ; montant 250.00 € ; risque théorique 11.22 € ; R/R net 1.53.
  Chase risk : 2.002/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ATH-EUR : 0.0048025 € ; score 92.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XTZ-EUR : 0.30455 € ; score 90.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MERL-EUR : 0.023782 € ; score 82.24/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- SUPER-EUR : 0.12944 € ; score 80.36/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0078051 € ; score 79.89/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0016168 | +110.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0134 | +58.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053333 | +58.46 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.3144 | +40.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.044218 | +38.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010117 | +31.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008257 | +27.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.098645 | +25.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3299e-06 | +23.93 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.22855 | +23.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1103 scans ; 472615 observations ; 402 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
