# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-11T14:52:16.581790+00:00
État : OK | marchés EUR : 429 | V4 : 364 | données valides : 19
Récupération : 2026-09-11T14:51:45.117134+00:00 | âge ticker : 149.0 s | durée : 150.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 44/429 ; 15 min 62/429.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- W-EUR : SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.0005159 € ; score 88.98/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0064678 € ; score 83.40/100 ; SURVEILLE ; WICK_SETUP
- KAS-EUR : 0.031189 € ; score 78.64/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.35991 € ; score 77.97/100 ; SURVEILLE ; STABILITY_HOLD
- SYRUP-EUR : 0.19562 € ; score 77.65/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| RAY-EUR | 1.41726 | +24.78 % | EXCLUDED_BEFORE_MOVE |
| PUFFER-EUR | 0.017557 | +23.71 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| MET-EUR | 0.22709 | +21.65 % | EXCLUDED_BEFORE_MOVE |
| CNPY-EUR | 0.21121 | +20.11 % | EXCLUDED_BEFORE_MOVE |
| DOGS-EUR | 4.5996e-05 | +17.94 % | DETECTED_EARLY |
| BLUR-EUR | 0.01623 | +16.16 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| LSK-EUR | 0.1064 | +11.66 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| NEAR-EUR | 2.2981 | +11.37 % | DETECTED_EARLY |
| EIGEN-EUR | 0.193 | +11.35 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| VVV-EUR | 22.309 | +10.86 % | DETECTED_EARLY |

Historique : 223 scans ; 95693 observations ; 40 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
