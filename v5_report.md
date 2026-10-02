# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T13:05:55.263693+00:00
État : OK | marchés EUR : 426 | V4 : 387 | données valides : 426
Récupération : 2026-10-02T13:05:24.355165+00:00 | âge ticker : 150.0 s | durée : 151.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- YFI-EUR : 2292.4 € ; score 88.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AVAX-EUR : 9.9963 € ; score 86.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.457 € ; score 86.13/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ATH-EUR : 0.00566 € ; score 85.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LDO-EUR : 0.41569 € ; score 85.68/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.060619 | +60.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.032574 | +26.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.1101 | +24.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0023781 | +19.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.082211 | +18.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.091451 | +17.55 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.20336 | +17.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.53393 | +15.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.49581 | +15.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MAGIC-EUR | 0.053153 | +14.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1980 scans ; 847466 observations ; 1564 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
