# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T16:23:18.770097+00:00
État : OK | marchés EUR : 426 | V4 : 391 | données valides : 426
Récupération : 2026-10-02T16:22:20.936592+00:00 | âge ticker : 177.2 s | durée : 178.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVNT-EUR : 0.11542 € ; score 87.65/100 ; SURVEILLE ; seuil achat non atteint
- RE-EUR : 0.45382 € ; score 86.96/100 ; SURVEILLE ; WICK_SETUP
- DYDX-EUR : 0.13806 € ; score 86.33/100 ; SURVEILLE ; SPREAD_RISK
- RENDER-EUR : 1.7824 € ; score 85.50/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.117007 € ; score 85.10/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.056902 | +46.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.119304 | +28.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0023925 | +19.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.51589 | +19.07 % | DETECTED_EARLY | NONE | NONE |
| ATH-EUR | 0.006028 | +16.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.08359 | +15.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.15026 | +15.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.090399 | +14.71 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SPK-EUR | 0.023989 | +13.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.55188 | +13.16 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1989 scans ; 851300 observations ; 1573 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
