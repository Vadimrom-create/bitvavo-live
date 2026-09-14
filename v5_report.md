# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-14T21:03:47.032897+00:00
État : OK | marchés EUR : 429 | V4 : 366 | données valides : 5
Récupération : 2026-09-14T21:03:16.900170+00:00 | âge ticker : 139.6 s | durée : 141.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 27/429 ; 15 min 66/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- AVAX-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- ETH-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- SYRUP-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- LSK-EUR : 0.35574 € ; score 75.70/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HBAR-EUR : 0.067831 € ; score 64.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.025453 | +46.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.29053 | +45.37 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CAP-EUR | 0.05115 | +25.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARK-EUR | 0.14951 | +21.88 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| BOB-EUR | 0.004518 | +19.91 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MTL-EUR | 0.27993 | +15.97 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| SYN-EUR | 0.077609 | +12.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENDLE-EUR | 2.0689 | +12.02 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RED-EUR | 0.12279 | +10.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.013703 | +10.70 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 501 scans ; 214955 observations ; 84 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
