# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-18T16:24:52.552596+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 8
Récupération : 2026-09-18T16:24:21.422162+00:00 | âge ticker : 145.0 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 48/427 ; 15 min 86/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, STALE_DAILY_PROFILE
- ICP-EUR : CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE
- LDO-EUR : CHASE_RISK, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- ENSO-EUR : 0.8503 € ; score 81.87/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.0068376 € ; score 80.12/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.003771 € ; score 78.81/100 ; SURVEILLE ; WICK_SETUP
- DOT-EUR : 0.9907 € ; score 78.17/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0073432 | +84.75 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.51614 | +52.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0042297 | +51.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.070584 | +43.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.032721 | +33.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.0465 | +26.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.1767 | +25.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARB-EUR | 0.18925 | +23.33 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| S-EUR | 0.028879 | +22.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| UNI-EUR | 7.7221 | +22.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 810 scans ; 347649 observations ; 166 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
