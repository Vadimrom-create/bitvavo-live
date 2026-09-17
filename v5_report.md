# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T08:24:33.083221+00:00
État : OK | marchés EUR : 430 | V4 : 375 | données valides : 8
Récupération : 2026-09-17T08:24:02.391788+00:00 | âge ticker : 143.9 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 19/430 ; 15 min 46/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- HYPE-EUR : STALE_DAILY_PROFILE
- TAO-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- UNI-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- ONDO-EUR : 0.30792 € ; score 84.62/100 ; SURVEILLE ; WICK_SETUP
- LSK-EUR : 0.4355 € ; score 75.83/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- FET-EUR : 0.13724 € ; score 74.97/100 ; SURVEILLE ; seuil achat non atteint
- LAPTOP-EUR : 0.11501 € ; score 74.03/100 ; SURVEILLE ; WICK_SETUP
- LINK-EUR : 9.7696 € ; score 73.51/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| AVA-EUR | 0.20909 | +55.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.060534 | +35.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HNT-EUR | 0.4213 | +24.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QUID-EUR | 0.060405 | +21.78 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PEAQ-EUR | 0.02432 | +18.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.3788 | +18.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RAY-EUR | 1.30546 | +17.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 4.2787 | +16.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.30643 | +15.56 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| CNPY-EUR | 0.34447 | +14.98 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 697 scans ; 299104 observations ; 118 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
