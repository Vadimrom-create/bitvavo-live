# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T01:11:18.374068+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-28T01:10:47.837596+00:00 | âge ticker : 157.4 s | durée : 158.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- EIGEN-EUR : 0.24488 € ; score 92.41/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.085496 € ; score 91.68/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HUMA-EUR : 0.025397 € ; score 90.48/100 ; SURVEILLE ; SPREAD_RISK
- ICP-EUR : 2.7515 € ; score 88.61/100 ; SURVEILLE ; WICK_SETUP
- ACU-EUR : 0.11783 € ; score 87.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 232.248 | +62.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.2876 | +36.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.06 | +28.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INX-EUR | 0.006628 | +28.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030213 | +26.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.017359 | +18.76 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SEI-EUR | 0.073839 | +17.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0045062 | +16.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013611 | +15.29 % | DETECTED_EARLY | NONE | NONE |
| IMX-EUR | 0.16593 | +14.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1661 scans ; 710615 observations ; 1210 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
