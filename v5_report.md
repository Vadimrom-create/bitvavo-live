# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T18:41:03.841538+00:00
État : OK | marchés EUR : 426 | V4 : 386 | données valides : 41
Récupération : 2026-09-20T18:40:33.814994+00:00 | âge ticker : 154.5 s | durée : 157.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 46/426 ; 15 min 83/426.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- BNB-EUR : WICK_SETUP, INVALID_5M
- CAKE-EUR : SELLER_HEAVY_BOOK, INVALID_5M
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M

## SURVEILLE

- XLM-EUR : 0.17026 € ; score 86.97/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.795 € ; score 79.84/100 ; SURVEILLE ; WICK_SETUP
- ENSO-EUR : 0.8836 € ; score 79.02/100 ; SURVEILLE ; WICK_SETUP
- APT-EUR : 0.6439 € ; score 78.31/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.027969 € ; score 77.39/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.031399 | +42.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0031688 | +35.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0007808 | +26.55 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.22886 | +24.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.043587 | +18.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.048534 | +16.04 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVA-EUR | 0.21815 | +15.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.0325 | +14.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.050073 | +14.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.6563 | +13.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1005 scans ; 430867 observations ; 236 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
