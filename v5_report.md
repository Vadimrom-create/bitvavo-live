# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-07T00:33:47.307128+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-10-07T00:32:40.274710+00:00 | âge ticker : 182.3 s | durée : 183.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- WAL-EUR : 0.033208 € ; score 78.88/100 ; SURVEILLE ; seuil achat non atteint
- PARTI-EUR : 0.029007 € ; score 76.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RENDER-EUR : 1.9179 € ; score 76.57/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ESP-EUR : 0.104579 € ; score 76.27/100 ; SURVEILLE ; seuil achat non atteint
- C-EUR : 0.089924 € ; score 75.36/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.005831 | +92.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.85746 | +38.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 14.3722 | +34.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0791534 | +21.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| POND-EUR | 0.001729 | +19.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MAGIC-EUR | 0.06363 | +15.35 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29091 | +12.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 19.969 | +12.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WELL-EUR | 0.0023711 | +11.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.020392 | +11.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2097 scans ; 897335 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
