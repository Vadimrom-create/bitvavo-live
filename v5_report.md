# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T15:47:40.432696+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T15:47:11.076520+00:00 | âge ticker : 152.3 s | durée : 153.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- MEGA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.39928 € | IGNITION | score 74.38/100 | entrée 6.90/10
  Entrée 0.39986 € ; stop 0.38566 € ; TP1 0.42826 € ; TP2 0.44245 € ; montant 250.00 € ; risque théorique 10.60 € ; R/R net 1.50.
  Chase risk : 2.218/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ROSE-EUR : 0.006664 € ; score 89.38/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- VELO-EUR : 0.0042527 € ; score 86.86/100 ; SURVEILLE ; seuil achat non atteint
- ALLO-EUR : 0.227971 € ; score 86.42/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- MERL-EUR : 0.025775 € ; score 86.17/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ACH-EUR : 0.0052787 € ; score 84.84/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0167 | +90.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FLOCK-EUR | 0.08351 | +33.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.07299 | +27.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 287.35 | +24.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050824 | +22.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.033235 | +16.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CHR-EUR | 0.017544 | +15.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KITE-EUR | 0.12 | +15.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46237 | +14.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.34687 | +13.84 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1196 scans ; 512233 observations ; 509 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
