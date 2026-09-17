# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T02:31:48.461435+00:00
État : OK | marchés EUR : 430 | V4 : 377 | données valides : 10
Récupération : 2026-09-17T02:31:16.585596+00:00 | âge ticker : 141.2 s | durée : 142.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 20/430 ; 15 min 38/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- USELESS-EUR : 0.206784 € ; score 76.25/100 ; SURVEILLE ; STABILITY_HOLD
- TAO-EUR : 194.22 € ; score 76.03/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 68.692 € ; score 72.61/100 ; SURVEILLE ; STABILITY_HOLD
- UNI-EUR : 5.8186 € ; score 70.83/100 ; SURVEILLE ; STABILITY_HOLD
- PEPE-EUR : 2.9991e-06 € ; score 68.05/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.137216 | +59.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.43266 | +31.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FOLD-EUR | 0.054954 | +25.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AVA-EUR | 0.16702 | +22.44 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| IOST-EUR | 0.0007912 | +21.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.31995 | +19.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AGI-EUR | 0.004139 | +18.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QUID-EUR | 0.058018 | +17.44 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RAY-EUR | 1.26731 | +16.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HNT-EUR | 0.40492 | +15.66 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 678 scans ; 290934 observations ; 112 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
