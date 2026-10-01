# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T02:57:23.278258+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-01T02:56:56.440554+00:00 | âge ticker : 147.0 s | durée : 148.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVAX-EUR : 9.747 € ; score 92.15/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 3.0114 € ; score 92.13/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : 1.4861 € ; score 87.90/100 ; SURVEILLE ; seuil achat non atteint
- LTC-EUR : 59.496 € ; score 86.49/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TNSR-EUR : 0.034566 € ; score 85.67/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0794 | +90.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35573 | +48.84 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.43696 | +28.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008526 | +26.95 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33281 | +21.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028385 | +19.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0185824 | +19.18 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.46305 | +15.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0611812 | +14.34 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ICX-EUR | 0.007322 | +12.63 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1881 scans ; 804908 observations ; 1435 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
