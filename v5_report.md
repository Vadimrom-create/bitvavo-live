# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T22:37:08.003914+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-02T22:36:35.588567+00:00 | âge ticker : 146.5 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GALA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- STX-EUR : 0.32412 € ; score 91.34/100 ; SURVEILLE ; seuil achat non atteint
- ARB-EUR : 0.17243 € ; score 84.35/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.069102 € ; score 83.34/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 160.95 € ; score 83.06/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.1137 € ; score 82.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.057681 | +45.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023017 | +14.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0058594 | +13.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.087848 | +11.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.47475 | +11.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.145 | +10.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.025548 | +9.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.02892 | +9.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.48172 | +8.52 % | DETECTED_EARLY | NONE | NONE |
| SPK-EUR | 0.022728 | +8.21 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2010 scans ; 860246 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
