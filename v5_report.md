# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T19:41:12.862906+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 7
Récupération : 2026-09-14T19:40:40.116920+00:00 | âge ticker : 140.7 s | durée : 141.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 28/429 ; 15 min 69/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE
- VET-EUR : WICK_SETUP, STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.37052 € ; score 77.01/100 ; SURVEILLE ; SPREAD_RISK
- NEAR-EUR : 2.1767 € ; score 74.89/100 ; SURVEILLE ; seuil achat non atteint
- USELESS-EUR : 0.184816 € ; score 74.35/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.33757 € ; score 73.70/100 ; SURVEILLE ; STABILITY_HOLD
- LINK-EUR : 10.1262 € ; score 71.68/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.02385 | +37.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.25837 | +36.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0491553 | +21.21 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14338 | +16.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SENT-EUR | 0.014424 | +15.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MTL-EUR | 0.2774 | +15.66 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0287 | +10.08 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ACX-EUR | 0.0369 | +9.11 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| T-EUR | 0.0041711 | +8.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.1767 | +8.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 496 scans ; 212810 observations ; 81 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
