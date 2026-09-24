# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T05:23:17.404004+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-24T05:22:24.600552+00:00 | âge ticker : 176.5 s | durée : 177.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AERO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RUNE-EUR : 0.55745 € ; score 92.16/100 ; SURVEILLE ; seuil achat non atteint
- FET-EUR : 0.17586 € ; score 92.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : 3.8829e-06 € ; score 91.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BAT-EUR : 0.07936 € ; score 91.29/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 255.09 € ; score 90.98/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.122106 | +36.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020392 | +33.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.33901 | +25.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.8389 | +15.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018773 | +13.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3672 | +10.44 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVC-EUR | 0.027724 | +10.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMU-EUR | 0.00185 | +9.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOSO-EUR | 0.2866 | +9.06 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ACU-EUR | 0.11495 | +8.35 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1331 scans ; 569743 observations ; 682 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
