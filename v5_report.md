# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-15T06:21:25.143751+00:00
État : OK | marchés EUR : 429 | V4 : 364 | données valides : 6
Récupération : 2026-09-15T06:20:54.617587+00:00 | âge ticker : 145.0 s | durée : 146.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/429 ; 15 min 44/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- ZORA-EUR : WICK_SETUP, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00063452 € ; score 78.96/100 ; SURVEILLE ; VERTICAL_SHORT_TERM
- LSK-EUR : 0.37428 € ; score 77.21/100 ; SURVEILLE ; SPREAD_RISK, VERTICAL_SHORT_TERM, STABILITY_HOLD
- TAO-EUR : 201.56 € ; score 75.09/100 ; SURVEILLE ; WICK_SETUP
- NPC-EUR : 0.0191159 € ; score 72.67/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 2.1064 € ; score 72.40/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PUFFER-EUR | 0.023205 | +38.37 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0542486 | +31.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.2653 | +21.27 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AXL-EUR | 0.045484 | +16.74 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CTR-EUR | 0.010584 | +15.42 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ACX-EUR | 0.0369 | +11.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ASTR-EUR | 0.0060175 | +10.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.0606 | +7.60 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MIRA-EUR | 0.043501 | +6.61 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOT-EUR | 0.00040513 | +6.50 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 531 scans ; 227825 observations ; 93 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
