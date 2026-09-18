# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T19:00:51.085698+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 9
Récupération : 2026-09-18T19:00:20.458841+00:00 | âge ticker : 142.1 s | durée : 142.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 43/427 ; 15 min 87/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- LDO-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- DOT-EUR : 0.9836 € ; score 80.31/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2274.99 € ; score 75.74/100 ; SURVEILLE ; seuil achat non atteint
- LSK-EUR : 0.39067 € ; score 74.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- WLD-EUR : 0.36284 € ; score 73.91/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.006775 | +67.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.036146 | +46.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0038716 | +38.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NEAR-EUR | 3.2642 | +25.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| C-EUR | 0.060698 | +24.52 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.51634 | +23.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.045274 | +22.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.18951 | +21.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.028109 | +20.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ETHFI-EUR | 0.64963 | +19.87 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 820 scans ; 351919 observations ; 178 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
