# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T14:47:03.797372+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 32
Récupération : 2026-09-19T14:46:33.667074+00:00 | âge ticker : 151.8 s | durée : 152.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 34/427 ; 15 min 81/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INVALID_5M
- BCH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INVALID_5M
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- USELESS-EUR : 0.242 € | IGNITION | score 90.91/100 | entrée 7.10/10
  Entrée 0.241961 € ; stop 0.230466 € ; TP1 0.264951 € ; TP2 0.276446 € ; montant 220.83 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.84/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 10.9212 € ; score 89.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.93 € ; score 84.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 124.59 € ; score 81.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 97.41 € ; score 80.51/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 235.34 € ; score 80.17/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.07211 | +44.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.33484 | +40.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.210732 | +34.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.02288 | +26.50 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| STRK-EUR | 0.037951 | +25.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.07127 | +21.35 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| C-EUR | 0.062689 | +20.91 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.0035389 | +20.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17297 | +20.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.38146 | +20.21 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 897 scans ; 384798 observations ; 203 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
