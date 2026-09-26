# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T17:15:59.385850+00:00
État : OK | marchés EUR : 427 | V4 : 388 | données valides : 427
Récupération : 2026-09-26T17:15:27.479395+00:00 | âge ticker : 157.9 s | durée : 159.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- W-EUR : 0.011473 € ; score 93.89/100 ; SURVEILLE ; WICK_SETUP
- SPK-EUR : 0.022395 € ; score 93.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RPL-EUR : 1.8749 € ; score 92.98/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- VTHO-EUR : 0.00072178 € ; score 90.97/100 ; SURVEILLE ; seuil achat non atteint
- AI-EUR : 0.019213 € ; score 89.44/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0016971 | +115.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.1277 | +47.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006526 | +46.36 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019165 | +34.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 108.39 | +25.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006055 | +18.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 2Z-EUR | 0.0605 | +17.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ACE-EUR | 0.19592 | +17.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.65328 | +17.09 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| KAS-EUR | 0.042631 | +16.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1548 scans ; 662364 observations ; 1014 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
