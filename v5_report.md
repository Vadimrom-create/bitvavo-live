# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T20:23:50.780755+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-24T20:22:51.759768+00:00 | âge ticker : 174.3 s | durée : 175.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VVV-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TAIKO-EUR : 0.07982 € ; score 90.71/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MMT-EUR : 0.15087 € ; score 90.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.059562 € ; score 84.98/100 ; SURVEILLE ; WICK_SETUP
- SNX-EUR : 0.2231 € ; score 83.35/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- TAO-EUR : 260.25 € ; score 83.24/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| LSK-EUR | 0.3921 | +39.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XAI-EUR | 0.0094253 | +37.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.63218 | +37.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.44978 | +24.44 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 76.551 | +23.27 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.095 | +22.37 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.037003 | +20.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0161749 | +19.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0019886 | +19.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.16489 | +18.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1385 scans ; 592763 observations ; 759 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
