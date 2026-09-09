# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-09T11:51:57.359590+00:00
État : OK | marchés EUR : 428 | V4 : 368 | données valides : 14
Récupération : 2026-09-09T11:51:25.863392+00:00 | âge ticker : 137.8 s | durée : 138.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 39/428 ; 15 min 80/428.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : WICK_SETUP, INVALID_5M, STALE_DAILY_PROFILE
- KAS-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- RENDER-EUR : WICK_SETUP, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- TAO-EUR : 229.42 € | IGNITION | score 91.10/100 | entrée 7.50/10
  Entrée 229.57 € ; stop 220.19 € ; TP1 248.32 € ; TP2 257.71 € ; montant 250.00 € ; risque théorique 11.93 € ; R/R net 1.56.
  Chase risk : 2.85/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AAVE-EUR : 111.22 € ; score 86.57/100 ; SURVEILLE ; seuil achat non atteint
- AVAX-EUR : 6.8425 € ; score 79.19/100 ; SURVEILLE ; seuil achat non atteint
- DOGE-EUR : 0.077946 € ; score 78.82/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.38592 € ; score 76.33/100 ; SURVEILLE ; WICK_SETUP
- UNI-EUR : 5.7398 € ; score 74.52/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| VVV-EUR | 23.007 | +44.58 % | EXCLUDED_BEFORE_MOVE |
| IOST-EUR | 0.0010038 | +27.02 % | DETECTED_EARLY |
| RAY-EUR | 1.12556 | +21.62 % | DETECTED_EARLY |
| KAT-EUR | 0.004993 | +21.28 % | EXCLUDED_BEFORE_MOVE |
| USELESS-EUR | 0.266542 | +16.85 % | EXCLUDED_BEFORE_MOVE |
| XTZ-EUR | 0.23237 | +14.71 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| LRC-EUR | 0.008302 | +13.90 % | EXCLUDED_BEFORE_MOVE |
| NPC-EUR | 0.017762 | +13.68 % | DETECTED_EARLY |
| ATOM-EUR | 1.6462 | +13.16 % | DETECTED_EARLY |
| CHIP-EUR | 0.05076 | +12.48 % | DETECTED_EARLY |

Historique : 49 scans ; 20972 observations ; 17 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
