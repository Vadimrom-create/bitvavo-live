# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T17:14:52.870542+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-22T17:13:56.534307+00:00 | âge ticker : 181.8 s | durée : 182.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WAL-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- TAIKO-EUR : 0.08038 € ; score 93.78/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZEN-EUR : 7.0178 € ; score 91.94/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOMI-EUR : 0.16748 € ; score 90.72/100 ; SURVEILLE ; SPREAD_RISK
- MANA-EUR : 0.0759 € ; score 89.90/100 ; SURVEILLE ; seuil achat non atteint
- RLC-EUR : 0.30719 € ; score 89.47/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CHR-EUR | 0.022 | +45.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.072652 | +31.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.050869 | +23.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 282.47 | +22.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FLOCK-EUR | 0.078668 | +22.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.383 | +19.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2215 | +19.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12089 | +17.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MLN-EUR | 1.4003 | +15.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| S-EUR | 0.038816 | +15.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1200 scans ; 513937 observations ; 520 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
