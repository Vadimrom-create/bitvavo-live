# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T18:22:06.622604+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 36
Récupération : 2026-09-19T18:21:28.938132+00:00 | âge ticker : 157.3 s | durée : 158.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 37/427 ; 15 min 100/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_5M
- ICP-EUR : INVALID_5M
- KAS-EUR : INVALID_5M
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : STABILITY_HOLD, INVALID_5M
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.6568e-06 € | IGNITION | score 80.57/100 | entrée 6.90/10
  Entrée 3.6695e-06 € ; stop 3.3634e-06 € ; TP1 4.2817e-06 € ; TP2 4.5878e-06 € ; montant 133.15 € ; risque théorique 12.00 € ; R/R net 1.77.
  Chase risk : 9.789/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HYPE-EUR : 80.21 € ; score 76.49/100 ; SURVEILLE ; STABILITY_HOLD
- VET-EUR : 0.0074712 € ; score 75.98/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 96.642 € ; score 75.12/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 228.57 € ; score 74.52/100 ; SURVEILLE ; STABILITY_HOLD
- SUI-EUR : 0.75022 € ; score 74.23/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.074923 | +44.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.43467 | +36.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.207928 | +36.49 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.31539 | +28.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 0.97324 | +25.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.071763 | +22.63 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17185 | +19.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.4933 | +19.23 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| G-EUR | 0.0084489 | +18.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.135627 | +16.39 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 912 scans ; 391203 observations ; 213 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
