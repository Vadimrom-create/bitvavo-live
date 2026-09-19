# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T14:34:16.653836+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 33
Récupération : 2026-09-19T14:33:13.980081+00:00 | âge ticker : 184.0 s | durée : 184.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 35/427 ; 15 min 82/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_5M
- BCH-EUR : WICK_SETUP, INVALID_5M
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- USELESS-EUR : 0.242 € | IGNITION | score 90.63/100 | entrée 7.60/10
  Entrée 0.242 € ; stop 0.230478 € ; TP1 0.265044 € ; TP2 0.276566 € ; montant 220.41 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 5.011/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SOL-EUR : 97.603 € ; score 82.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.688 € ; score 80.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 233.28 € ; score 79.10/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0074331 € ; score 78.94/100 ; SURVEILLE ; seuil achat non atteint
- PEPE-EUR : 3.3338e-06 € ; score 78.09/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.072634 | +45.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.33224 | +38.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.21345 | +36.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.02292 | +27.63 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.038279 | +27.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0035712 | +22.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.175 | +21.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.080406 | +21.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.070512 | +20.06 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.37839 | +19.34 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 896 scans ; 384371 observations ; 201 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
