# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T04:39:49.132362+00:00
État : OK | marchés EUR : 426 | V4 : 373 | données valides : 426
Récupération : 2026-09-21T04:38:54.445092+00:00 | âge ticker : 169.5 s | durée : 170.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- 0G-EUR : 0.19669 € ; score 91.92/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- KERNEL-EUR : 0.038622 € ; score 90.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HBAR-EUR : 0.075949 € ; score 89.64/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : 0.095303 € ; score 89.59/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.028487 € ; score 89.44/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0011495 | +87.00 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZETA-EUR | 0.055392 | +64.48 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FTT-EUR | 0.25356 | +38.95 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030945 | +29.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.8611 | +27.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.054708 | +24.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.5491 | +22.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46697 | +19.34 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.9689 | +18.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.03395 | +18.43 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1047 scans ; 448759 observations ; 314 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
