# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T18:00:42.671077+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 9
Récupération : 2026-09-14T18:00:14.108407+00:00 | âge ticker : 140.7 s | durée : 142.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 25/429 ; 15 min 67/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE
- INJ-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- TAO-EUR : 204.62 € ; score 85.87/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.24064 € ; score 83.31/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 10.0431 € ; score 78.63/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.14786 € ; score 75.82/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.023318 | +33.16 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.24835 | +31.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0494315 | +22.86 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.014454 | +15.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MTL-EUR | 0.274 | +13.97 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.14249 | +13.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NPC-EUR | 0.0201162 | +11.71 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0023172 | +11.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NOT-EUR | 0.0004136 | +10.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NEAR-EUR | 2.2317 | +10.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 491 scans ; 210665 observations ; 80 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
