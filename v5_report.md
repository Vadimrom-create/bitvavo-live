# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T10:13:53.228701+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 30
Récupération : 2026-09-19T10:12:55.603305+00:00 | âge ticker : 174.6 s | durée : 175.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 33/427 ; 15 min 78/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- AERO-EUR : INVALID_15M, INVALID_5M
- APT-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, INVALID_5M
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : CHASE_RISK, INVALID_5M
- QNT-EUR : INVALID_15M, INVALID_5M
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- TAO-EUR : 229.9 € | IGNITION | score 87.25/100 | entrée 7.20/10
  Entrée 229.53 € ; stop 217.98 € ; TP1 252.63 € ; TP2 264.18 € ; montant 210.00 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 4.946/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.35318 € | IGNITION | score 80.40/100 | entrée 7.55/10
  Entrée 0.35377 € ; stop 0.34129 € ; TP1 0.37872 € ; TP2 0.3912 € ; montant 250.00 € ; risque théorique 10.54 € ; R/R net 1.50.
  Chase risk : 2.275/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 10.883 € ; score 87.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.15806 € ; score 82.34/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.6464 € ; score 79.67/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0073584 € ; score 78.23/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.01 € ; score 77.74/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| EDGE-EUR | 0.085499 | +48.16 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SYN-EUR | 0.209503 | +35.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.065763 | +31.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.14723 | +29.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0036895 | +28.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.02404 | +27.96 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| XTZ-EUR | 0.29434 | +26.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.037197 | +25.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.046776 | +23.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0076818 | +23.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 880 scans ; 377539 observations ; 192 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
