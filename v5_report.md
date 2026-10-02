# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T01:53:04.247517+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T01:52:31.980454+00:00 | âge ticker : 146.3 s | durée : 147.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 155.92 € ; score 88.92/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.20687 € ; score 88.33/100 ; SURVEILLE ; WICK_SETUP
- ZRO-EUR : 1.6219 € ; score 85.26/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- IMX-EUR : 0.15404 € ; score 83.36/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LDO-EUR : 0.38847 € ; score 82.94/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00057853 | +124.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.153051 | +87.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.028863 | +34.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.6351 | +33.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04714 | +24.28 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.166253 | +19.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.17536 | +18.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0024216 | +17.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.42535 | +15.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.19756 | +12.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1947 scans ; 833288 observations ; 1514 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
