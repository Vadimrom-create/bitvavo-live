# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T16:54:40.937808+00:00
État : OK | marchés EUR : 429 | V4 : 366 | données valides : 10
Récupération : 2026-09-14T16:54:12.827415+00:00 | âge ticker : 136.4 s | durée : 137.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 29/429 ; 15 min 60/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- JUP-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- LTC-EUR : INVALID_5M, STALE_DAILY_PROFILE
- SUI-EUR : STALE_DAILY_PROFILE
- VET-EUR : INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.0005986 € ; score 88.30/100 ; SURVEILLE ; WICK_SETUP
- PUMP-EUR : 0.0032836 € ; score 86.58/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 203.99 € ; score 82.83/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.22784 € ; score 79.22/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 9.9925 € ; score 78.51/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CNPY-EUR | 0.26048 | +38.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CPOOL-EUR | 0.023821 | +36.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.0492686 | +25.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14732 | +17.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MTL-EUR | 0.28001 | +17.05 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| T-EUR | 0.0043318 | +12.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0199808 | +11.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.013688 | +11.06 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| QKC-EUR | 0.0022781 | +9.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XLM-EUR | 0.16893 | +9.45 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 487 scans ; 208949 observations ; 79 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
