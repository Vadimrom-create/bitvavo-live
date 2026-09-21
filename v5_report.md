# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T11:21:15.861449+00:00
État : OK | marchés EUR : 426 | V4 : 386 | données valides : 426
Récupération : 2026-09-21T11:20:45.988508+00:00 | âge ticker : 145.1 s | durée : 146.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KSM-EUR : 4.0569 € ; score 91.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BCH-EUR : 231.15 € ; score 89.47/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MERL-EUR : 0.02395 € ; score 88.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- HOT-EUR : 0.00035999 € ; score 88.12/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- IOST-EUR : 0.0007746 € ; score 88.11/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.054088 | +75.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.056648 | +70.20 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PTB-EUR | 0.0010074 | +57.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SEI-EUR | 0.055341 | +34.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.031096 | +32.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.056112 | +30.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.23258 | +27.14 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEAQ-EUR | 0.031998 | +25.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUI-EUR | 0.88909 | +25.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.51609 | +22.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1071 scans ; 458983 observations ; 354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
