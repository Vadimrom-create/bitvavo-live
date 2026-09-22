# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T12:47:11.344546+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T12:46:17.129277+00:00 | âge ticker : 176.9 s | durée : 177.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ZORA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUSHI-EUR : 0.22185 € ; score 90.39/100 ; SURVEILLE ; WICK_SETUP
- TURBO-EUR : 0.0009379 € ; score 90.22/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ZRO-EUR : 1.051 € ; score 89.73/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.87431 € ; score 88.89/100 ; SURVEILLE ; seuil achat non atteint
- AI-EUR : 0.018373 € ; score 88.25/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016998 | +93.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.001414 | +79.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.054253 | +31.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XMN-EUR | 0.000548 | +31.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.071375 | +24.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.119503 | +24.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28495 | +21.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.2305 | +19.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.37969 | +17.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BTT-EUR | 3.4385e-07 | +16.45 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1185 scans ; 507547 observations ; 494 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
