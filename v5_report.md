# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T21:45:10.377256+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T21:44:38.856711+00:00 | âge ticker : 154.1 s | durée : 155.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.056102 € ; score 93.38/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 54.365 € ; score 89.38/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.17393 € ; score 88.72/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0016922 € ; score 86.45/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 100.644 € ; score 84.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.043993 | +28.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018171 | +25.03 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| CPOOL-EUR | 0.031436 | +24.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.085352 | +24.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.00178 | +19.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.77904 | +15.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0463763 | +13.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.30853 | +12.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15261 | +11.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.306 | +10.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1300 scans ; 556537 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
