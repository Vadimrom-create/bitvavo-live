# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T20:23:25.819179+00:00
État : OK | marchés EUR : 426 | V4 : 410 | données valides : 426
Récupération : 2026-09-23T20:22:55.063092+00:00 | âge ticker : 149.1 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- VET-EUR : 0.00777 € ; score 91.51/100 ; SURVEILLE ; WICK_SETUP
- F-EUR : 0.0032673 € ; score 86.85/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 4.9178e-06 € ; score 84.69/100 ; SURVEILLE ; seuil achat non atteint
- BOB-EUR : 0.0047749 € ; score 84.41/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- LTC-EUR : 53.669 € ; score 82.27/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.043331 | +31.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.032085 | +29.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.0862 | +23.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.01798 | +23.72 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| RAY-EUR | 1.84176 | +18.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3394 | +13.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15299 | +13.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LIGHTER-EUR | 4.7885 | +13.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.30084 | +9.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0016403 | +9.56 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1295 scans ; 554407 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
