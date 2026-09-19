# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T10:57:49.476246+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 33
Récupération : 2026-09-19T10:57:19.698432+00:00 | âge ticker : 144.9 s | durée : 145.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 35/427 ; 15 min 83/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- HBAR-EUR : INVALID_5M
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : WICK_SETUP, INVALID_5M
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M
- QNT-EUR : INVALID_5M
- SYRUP-EUR : WICK_SETUP, INVALID_5M
- TAO-EUR : BELOW_EXCHANGE_MINIMUM
- VET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- WIF-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- SUI-EUR : 0.743 € | IGNITION | score 88.33/100 | entrée 7.75/10
  Entrée 0.74328 € ; stop 0.71243 € ; TP1 0.80498 € ; TP2 0.83583 € ; montant 248.14 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 5.546/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- APT-EUR : 0.6392 € | IGNITION | score 83.52/100 | entrée 6.60/10
  Entrée 0.6408 € ; stop 0.6148 € ; TP1 0.6928 € ; TP2 0.7188 € ; montant 250.00 € ; risque théorique 11.86 € ; R/R net 1.56.
  Chase risk : 3.257/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 10.9064 € ; score 87.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.35434 € ; score 81.53/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0126491 € ; score 80.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HYPE-EUR : 79.713 € ; score 80.17/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- TAO-EUR : 232.46 € ; score 80.13/100 ; SURVEILLE ; BELOW_EXCHANGE_MINIMUM

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.071853 | +46.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.219255 | +43.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.024505 | +34.74 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.03883 | +30.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.075 | +29.97 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0036556 | +27.43 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.145566 | +27.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.29245 | +25.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046686 | +24.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0026618 | +24.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 883 scans ; 378820 observations ; 192 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
