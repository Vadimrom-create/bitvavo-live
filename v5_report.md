# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T22:34:05.717798+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T22:33:35.083038+00:00 | âge ticker : 144.4 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SLX-EUR : 0.0639 € ; score 89.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BEAM-EUR : 0.0017031 € ; score 86.06/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.564 € ; score 85.87/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.20738 € ; score 85.19/100 ; SURVEILLE ; WICK_SETUP
- MOVR-EUR : 0.761 € ; score 83.41/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.099687 | +45.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.032085 | +26.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018033 | +23.51 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SAGA-EUR | 0.043234 | +22.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.77092 | +13.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0455939 | +10.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0016745 | +10.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.1527 | +10.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LIGHTER-EUR | 4.707 | +10.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.05992 | +8.95 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1304 scans ; 558241 observations ; 667 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
