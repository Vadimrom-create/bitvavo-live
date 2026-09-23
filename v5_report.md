# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T21:29:37.429894+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T21:29:06.746900+00:00 | âge ticker : 148.7 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KITE-EUR : 0.11502 € ; score 90.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PLUME-EUR : 0.013752 € ; score 87.37/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0016922 € ; score 86.08/100 ; SURVEILLE ; SPREAD_RISK
- NPC-EUR : 0.0202096 € ; score 85.35/100 ; SURVEILLE ; WICK_SETUP
- SYN-EUR : 0.18665 € ; score 82.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.043316 | +28.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.0319 | +25.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.01813 | +24.75 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NOM-EUR | 0.0018371 | +22.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.0839 | +20.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.7976 | +15.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15322 | +12.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.30495 | +11.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0455069 | +11.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.30386 | +10.62 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1299 scans ; 556111 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
