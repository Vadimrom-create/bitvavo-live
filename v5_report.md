# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-09T07:39:40.266194+00:00
État : OK | marchés EUR : 428 | V4 : 367 | données valides : 10
Récupération : 2026-09-09T07:39:08.535013+00:00 | âge ticker : 146.6 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 34/428 ; 15 min 63/428.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, INVALID_15M, INVALID_5M
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : STABILITY_HOLD, INVALID_5M
- VET-EUR : STABILITY_HOLD, INVALID_5M
- WAL-EUR : STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- NEAR-EUR : 2.0855 € | IGNITION | score 78.29/100 | entrée 7.20/10
  Entrée 2.087 € ; stop 1.9802 € ; TP1 2.3006 € ; TP2 2.4074 € ; montant 206.92 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.893/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 10.8064 € ; score 85.36/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.068403 € ; score 80.33/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.19032 € ; score 78.87/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.1542 € ; score 77.25/100 ; SURVEILLE ; seuil achat non atteint
- ETH-EUR : 2159.71 € ; score 76.49/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | État historique |
|---|---:|---:|---|
| VVV-EUR | 25.0269 | +64.53 % | INSUFFICIENT_HISTORY |
| USELESS-EUR | 0.275523 | +37.44 % | DETECTED_EARLY |
| RAY-EUR | 1.1582 | +23.75 % | DETECTED_EARLY |
| ICX-EUR | 0.013091 | +20.77 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| IOST-EUR | 0.0009898 | +19.11 % | DETECTED_EARLY |
| LIGHTER-EUR | 4.6023 | +16.35 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| NPC-EUR | 0.0169935 | +15.66 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| KAT-EUR | 0.004704 | +15.46 % | DETECTED_EARLY |
| ATOM-EUR | 1.6214 | +14.16 % | NO_CONFIRMED_SHORT_TERM_EVENT |
| CHIP-EUR | 0.048835 | +11.30 % | NO_CONFIRMED_SHORT_TERM_EVENT |

Historique : 35 scans ; 14980 observations ; 6 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
