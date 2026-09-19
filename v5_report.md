# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T17:16:06.516238+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 36
Récupération : 2026-09-19T17:15:40.956167+00:00 | âge ticker : 149.4 s | durée : 151.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 38/427 ; 15 min 89/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- BIGTIME-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- SHIB-EUR : INVALID_5M
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : SELLER_HEAVY_BOOK, INVALID_5M
- WLD-EUR : INVALID_5M
- PEPE-EUR : 3.6377e-06 € | IGNITION | score 81.54/100 | entrée 6.85/10
  Entrée 3.6407e-06 € ; stop 3.3035e-06 € ; TP1 4.3151e-06 € ; TP2 4.6523e-06 € ; montant 120.85 € ; risque théorique 12.00 € ; R/R net 1.79.
  Chase risk : 10/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ADA-EUR : 0.20068 € ; score 88.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 81.172 € ; score 86.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DOGE-EUR : 0.079063 € ; score 83.96/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.75294 € ; score 82.74/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 97.661 € ; score 80.41/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.073671 | +45.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.21 | +37.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.40509 | +27.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31124 | +27.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0095074 | +27.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17741 | +24.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.071156 | +21.59 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 8.4963 | +20.87 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CROSS-EUR | 0.13633 | +19.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.91962 | +19.25 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 907 scans ; 389068 observations ; 211 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
