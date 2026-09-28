# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T08:16:25.522322+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 427
Récupération : 2026-09-28T08:15:51.721729+00:00 | âge ticker : 153.8 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XDC-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- GRAM-EUR : 1.4407 € | IGNITION | score 83.65/100 | entrée 7.20/10
  Entrée 1.4416 € ; stop 1.386 € ; TP1 1.5528 € ; TP2 1.6084 € ; montant 250.00 € ; risque théorique 11.36 € ; R/R net 1.54.
  Chase risk : 2.354/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ENA-EUR : 0.23418 € ; score 91.55/100 ; SURVEILLE ; WICK_SETUP
- NMR-EUR : 8.7839 € ; score 87.89/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- TAO-EUR : 267.56 € ; score 86.61/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.3413 € ; score 86.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HUMA-EUR : 0.02439 € ; score 85.88/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 230.806 | +53.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.0799 | +37.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.015441 | +18.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.028242 | +15.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.030007 | +11.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0043325 | +10.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016274 | +9.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.54551 | +8.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.2855 | +8.02 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SEI-EUR | 0.07122 | +7.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1682 scans ; 719582 observations ; 1237 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
