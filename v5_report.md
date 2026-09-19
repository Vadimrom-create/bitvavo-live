# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T09:55:08.016257+00:00
État : OK | marchés EUR : 427 | V4 : 393 | données valides : 31
Récupération : 2026-09-19T09:54:36.808664+00:00 | âge ticker : 148.3 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 35/427 ; 15 min 76/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- AERO-EUR : INVALID_15M, INVALID_5M
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- KAS-EUR : STABILITY_HOLD, INVALID_5M
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- TAO-EUR : 231.57 € | IGNITION | score 87.07/100 | entrée 6.95/10
  Entrée 231.84 € ; stop 217.97 € ; TP1 259.58 € ; TP2 273.45 € ; montant 180.14 € ; risque théorique 12.00 € ; R/R net 1.68.
  Chase risk : 5.803/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- FET-EUR : 0.15839 € | IGNITION | score 86.00/100 | entrée 7.40/10
  Entrée 0.15834 € ; stop 0.15253 € ; TP1 0.16996 € ; TP2 0.17577 € ; montant 250.00 € ; risque théorique 10.89 € ; R/R net 1.52.
  Chase risk : 2.893/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ONDO-EUR : 0.35328 € ; score 91.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : 1.64115 € ; score 77.64/100 ; SURVEILLE ; seuil achat non atteint
- HYPE-EUR : 80 € ; score 77.45/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 97.255 € ; score 74.80/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED
- LINK-EUR : 10.8464 € ; score 74.71/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.212376 | +36.32 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| HEI-EUR | 0.152073 | +33.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.065897 | +32.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.076 | +31.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| F-EUR | 0.003774 | +31.02 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.023881 | +28.21 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| XTZ-EUR | 0.29647 | +26.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIG-EUR | 0.047062 | +26.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0076787 | +25.76 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.037084 | +25.07 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 879 scans ; 377112 observations ; 192 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
