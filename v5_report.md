# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-12T21:53:31.530956+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-10-12T21:52:21.389358+00:00 | âge ticker : 183.9 s | durée : 184.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- STX-EUR : 0.38164 € ; score 79.23/100 ; SURVEILLE ; seuil achat non atteint
- CYBER-EUR : 0.33522 € ; score 75.86/100 ; SURVEILLE ; SPREAD_RISK
- ZK-EUR : 0.013037 € ; score 75.75/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- EDU-EUR : 0.06563 € ; score 72.61/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP
- CHIP-EUR : 0.052267 € ; score 72.40/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.241592 | +52.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OSMO-EUR | 0.045146 | +34.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RSR-EUR | 0.0019575 | +33.09 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SAFE-EUR | 0.123287 | +20.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3237 | +15.60 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AMP-EUR | 0.0006385 | +12.02 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OGN-EUR | 0.032541 | +12.01 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PUFFER-EUR | 0.022375 | +8.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKL-EUR | 0.0048269 | +8.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STX-EUR | 0.38164 | +8.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2150 scans ; 919942 observations ; 1658 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
