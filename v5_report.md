# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T22:05:55.030054+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T22:05:22.755406+00:00 | âge ticker : 156.3 s | durée : 158.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DATAIP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WAL-EUR : 0.032949 € ; score 93.26/100 ; SURVEILLE ; seuil achat non atteint
- WOO-EUR : 0.012473 € ; score 88.67/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- VIRTUAL-EUR : 0.72249 € ; score 88.34/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PROM-EUR : 5.5696 € ; score 86.26/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ATH-EUR : 0.0056055 € ; score 84.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 198.344 | +83.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28893 | +42.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006725 | +31.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030046 | +23.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013524 | +19.43 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.89099 | +18.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.00702 | +17.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0044086 | +14.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020216 | +13.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22304 | +13.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1650 scans ; 705918 observations ; 1179 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
