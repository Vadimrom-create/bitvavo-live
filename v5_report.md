# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T02:55:56.753714+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T02:55:25.793394+00:00 | âge ticker : 152.9 s | durée : 153.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SOMI-EUR : 0.16719 € ; score 90.72/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AEVO-EUR : 0.021731 € ; score 84.91/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- MERL-EUR : 0.024022 € ; score 84.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CTSI-EUR : 0.025908 € ; score 82.95/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- PORTAL-EUR : 0.017332 € ; score 81.56/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016027 | +85.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013826 | +76.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.055767 | +60.28 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| KERNEL-EUR | 0.058034 | +55.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.047194 | +42.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.111795 | +40.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.29383 | +29.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEPE-EUR | 4.3782e-06 | +25.44 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21725 | +23.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.33862 | +22.03 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1143 scans ; 489655 observations ; 445 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
