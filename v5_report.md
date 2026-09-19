# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T03:21:42.794589+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 19
Récupération : 2026-09-19T03:21:15.104775+00:00 | âge ticker : 146.9 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 19/427 ; 15 min 59/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_15M, INVALID_5M
- NPC-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- PUMP-EUR : INVALID_5M
- PYTH-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- UNI-EUR : CHASE_RISK, INVALID_5M
- TAO-EUR : 224.43 € | IGNITION | score 86.54/100 | entrée 7.20/10
  Entrée 223.78 € ; stop 215.57 € ; TP1 240.2 € ; TP2 248.41 € ; montant 250.00 € ; risque théorique 10.89 € ; R/R net 1.52.
  Chase risk : 3.92/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HYPE-EUR : 81.888 € ; score 81.30/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.20119 € ; score 78.92/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 98.614 € ; score 75.73/100 ; SURVEILLE ; WICK_SETUP
- ONDO-EUR : 0.35507 € ; score 73.84/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0071446 | +74.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037591 | +40.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0038282 | +34.45 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.28013 | +24.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0025712 | +23.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.192 | +22.60 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FOLD-EUR | 0.060582 | +20.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.053415 | +20.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.029518 | +19.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.044388 | +19.84 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 855 scans ; 366864 observations ; 186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
