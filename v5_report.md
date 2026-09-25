# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T21:07:49.558782+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-25T21:07:16.985419+00:00 | âge ticker : 154.8 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GALA-EUR : 0.0019028 € ; score 90.68/100 ; SURVEILLE ; WICK_SETUP
- FLR-EUR : 0.0064149 € ; score 88.89/100 ; SURVEILLE ; seuil achat non atteint
- INJ-EUR : 7.2074 € ; score 88.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ALT-EUR : 0.00704 € ; score 88.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- FLOKI-EUR : 2.531e-05 € ; score 87.94/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.075246 | +69.13 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21263 | +26.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013939 | +21.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.73003 | +19.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22988 | +18.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DEEP-EUR | 0.020348 | +17.54 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| EDGE-EUR | 0.088007 | +17.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.45186 | +17.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.063847 | +15.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JTO-EUR | 0.49948 | +14.64 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1472 scans ; 629912 observations ; 886 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
