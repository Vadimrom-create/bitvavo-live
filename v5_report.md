# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T01:58:13.379874+00:00
État : OK | marchés EUR : 429 | V4 : 371 | données valides : 2
Récupération : 2026-09-14T01:57:46.107372+00:00 | âge ticker : 144.0 s | durée : 145.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 16/429 ; 15 min 41/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VET-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- WAL-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE


## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.74666 | +61.09 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVC-EUR | 0.027912 | +27.24 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FIL-EUR | 0.85353 | +21.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VTHO-EUR | 0.00071472 | +19.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZKJ-EUR | 0.006103 | +18.37 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IQ-EUR | 0.0008131 | +13.62 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| SOLV-EUR | 0.0045893 | +11.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.019328 | +11.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.28681 | +9.24 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIL-EUR | 0.0025871 | +8.80 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 441 scans ; 189215 observations ; 63 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
