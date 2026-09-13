# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-13T20:01:13.944773+00:00
État : OK | marchés EUR : 429 | V4 : 367 | données valides : 8
Récupération : 2026-09-13T20:00:41.650421+00:00 | âge ticker : 146.2 s | durée : 147.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 21/429 ; 15 min 46/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NPC-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- VET-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- FET-EUR : 0.14801 € ; score 74.95/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 202.22 € ; score 72.94/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 9.8396 € ; score 66.66/100 ; SURVEILLE ; STABILITY_HOLD
- ONDO-EUR : 0.30201 € ; score 59.44/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.84 | +280.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVC-EUR | 0.031184 | +59.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| REZ-EUR | 0.0042203 | +24.74 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FIL-EUR | 0.84644 | +22.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.0006933 | +19.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZIL-EUR | 0.0027643 | +18.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.12298 | +17.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.25394 | +14.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOLV-EUR | 0.0044681 | +13.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| POWR-EUR | 0.053374 | +12.88 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 420 scans ; 180206 observations ; 58 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
