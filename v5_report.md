# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T05:14:17.149474+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T05:13:48.400377+00:00 | âge ticker : 152.2 s | durée : 153.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JTO-EUR : 0.45349 € ; score 88.89/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZORA-EUR : 0.007404 € ; score 88.86/100 ; SURVEILLE ; WICK_SETUP
- PORTAL-EUR : 0.01752 € ; score 87.51/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HNT-EUR : 0.4161 € ; score 86.44/100 ; SURVEILLE ; SPREAD_RISK
- TNSR-EUR : 0.03314 € ; score 86.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0016633 | +114.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.014976 | +72.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.118523 | +49.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.055331 | +37.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.046071 | +37.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.376e-06 | +25.60 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.38599 | +22.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.21301 | +21.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.27139 | +20.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0007867 | +19.31 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1151 scans ; 493063 observations ; 459 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
