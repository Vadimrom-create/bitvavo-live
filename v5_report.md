# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T15:39:42.981349+00:00
État : OK | marchés EUR : 426 | V4 : 388 | données valides : 426
Récupération : 2026-10-02T15:39:06.959608+00:00 | âge ticker : 156.0 s | durée : 156.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GLMR-EUR : 0.007808 € ; score 82.53/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- MOVE-EUR : 0.009218 € ; score 82.24/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AAVE-EUR : 162.18 € ; score 81.96/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.116132 € ; score 81.11/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NOM-EUR : 0.0023362 € ; score 79.91/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.05606 | +44.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.112847 | +22.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MAGIC-EUR | 0.056686 | +18.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.08286 | +16.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.56389 | +15.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.15175 | +15.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.7427 | +15.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.50446 | +15.41 % | DETECTED_EARLY | NONE | NONE |
| SCR-EUR | 0.025051 | +14.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006487 | +13.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1987 scans ; 850448 observations ; 1572 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
