# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-09T13:14:40.271965+00:00
État : OK | marchés EUR : 428 | V4 : 373 | données valides : 10
Récupération : 2026-09-09T13:14:11.282065+00:00 | âge ticker : 136.6 s | durée : 139.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 36/428 ; 15 min 85/428.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE
- ALGO-EUR : INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE, STALE_DAILY_PROFILE
- XPL-EUR : INVALID_15M, INVALID_5M
- TAO-EUR : 230.81 € | IGNITION | score 86.04/100 | entrée 7.45/10
  Entrée 230.91 € ; stop 221.08 € ; TP1 250.56 € ; TP2 260.4 € ; montant 242.81 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 2.774/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PUMP-EUR : 0.0039954 € | IGNITION | score 80.46/100 | entrée 7.45/10
  Entrée 0.0039951 € ; stop 0.003721 € ; TP1 0.0045432 € ; TP2 0.0048173 € ; montant 159.22 € ; risque théorique 12.00 € ; R/R net 1.72.
  Chase risk : 5.457/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PHA-EUR : 0.024516 € ; score 79.15/100 ; SURVEILLE ; WICK_SETUP
- BCH-EUR : 223.18 € ; score 76.96/100 ; SURVEILLE ; WICK_SETUP
- XRP-EUR : 1.23292 € ; score 75.21/100 ; SURVEILLE ; seuil achat non atteint
- UNI-EUR : 5.7313 € ; score 74.82/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| IOST-EUR | 0.0010927 | +40.78 % | DETECTED_EARLY |
| VVV-EUR | 22.523 | +36.07 % | EXCLUDED_BEFORE_MOVE |
| KAT-EUR | 0.005119 | +26.33 % | DETECTED_EARLY |
| RAY-EUR | 1.1488 | +24.19 % | DETECTED_EARLY |
| USELESS-EUR | 0.26949 | +20.59 % | EXCLUDED_BEFORE_MOVE |
| LRC-EUR | 0.008425 | +16.05 % | EXCLUDED_BEFORE_MOVE |
| CROSS-EUR | 0.1057 | +14.69 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| NEAR-EUR | 2.2432 | +13.32 % | DETECTED_EARLY |
| XTZ-EUR | 0.22766 | +12.38 % | DETECTED_EARLY |
| ATOM-EUR | 1.6689 | +11.30 % | NO_CONFIRMED_SHORT_TERM_EVENT |

Historique : 53 scans ; 22684 observations ; 17 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
