# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T17:46:44.814496+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 33
Récupération : 2026-09-19T17:46:12.301176+00:00 | âge ticker : 159.3 s | durée : 160.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 35/427 ; 15 min 94/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : STABILITY_HOLD, INVALID_5M
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- WIF-EUR : STABILITY_HOLD, INVALID_5M
- PEPE-EUR : 3.5988e-06 € | IGNITION | score 81.20/100 | entrée 7.15/10
  Entrée 3.6007e-06 € ; stop 3.3096e-06 € ; TP1 4.1829e-06 € ; TP2 4.474e-06 € ; montant 137.05 € ; risque théorique 12.00 € ; R/R net 1.76.
  Chase risk : 8.873/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- FET-EUR : 0.15685 € ; score 90.28/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.74584 € ; score 87.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.034711 € ; score 80.98/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.383 € ; score 79.55/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 97.118 € ; score 74.80/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.07242 | +40.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.208707 | +35.10 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.42304 | +33.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31526 | +29.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.071367 | +21.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17376 | +21.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CROSS-EUR | 0.135208 | +20.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.94005 | +20.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 8.465 | +19.98 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| STRK-EUR | 0.038881 | +17.38 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 910 scans ; 390349 observations ; 212 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
