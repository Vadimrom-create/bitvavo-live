# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T18:24:47.110430+00:00
État : OK | marchés EUR : 429 | V4 : 369 | données valides : 7
Récupération : 2026-09-14T18:24:19.122446+00:00 | âge ticker : 140.9 s | durée : 141.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 69/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- ALGO-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- FET-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- HYPE-EUR : STALE_DAILY_PROFILE
- INJ-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- SOL-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- TAO-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- XRP-EUR : 1.25074 € ; score 84.98/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 10.0794 € ; score 78.28/100 ; SURVEILLE ; WICK_SETUP
- PEPE-EUR : 3.0554e-06 € ; score 76.67/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.003233 € ; score 72.37/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 6.571 € ; score 68.22/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.2516 | +33.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.022701 | +29.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0497073 | +22.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14314 | +15.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.014238 | +14.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MTL-EUR | 0.27449 | +13.64 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NOT-EUR | 0.00041586 | +11.04 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NPC-EUR | 0.0200088 | +10.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.2288 | +9.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RON-EUR | 0.051288 | +9.67 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 492 scans ; 211094 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
