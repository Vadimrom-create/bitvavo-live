# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T00:25:04.529285+00:00
État : OK | marchés EUR : 426 | V4 : 394 | données valides : 426
Récupération : 2026-09-23T00:24:37.032415+00:00 | âge ticker : 143.7 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BABY-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- MOVR-EUR : 0.8234 € ; score 91.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- CAKE-EUR : 2.2542 € ; score 87.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- STO-EUR : 0.03811 € ; score 85.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MIOTA-EUR : 0.042953 € ; score 85.55/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BNB-EUR : 691.33 € ; score 85.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.019395 | +28.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 299.46 | +27.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019 | +22.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.07288 | +21.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.052581 | +20.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.298308 | +20.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2211 | +18.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.293 | +17.98 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TIA-EUR | 0.44882 | +17.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KITE-EUR | 0.12175 | +16.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1228 scans ; 525865 observations ; 564 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
