# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T03:20:15.246064+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T03:19:43.590480+00:00 | âge ticker : 149.1 s | durée : 150.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.103276 € ; score 91.44/100 ; SURVEILLE ; WICK_SETUP
- MANTRA-EUR : 0.004194 € ; score 90.22/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AVNT-EUR : 0.10977 € ; score 89.08/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- SYRUP-EUR : 0.19284 € ; score 87.43/100 ; SURVEILLE ; STABILITY_HOLD
- POL-EUR : 0.10445 € ; score 87.24/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.076829 | +75.02 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| POND-EUR | 0.0011776 | +52.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.23536 | +40.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.77838 | +27.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.73397 | +23.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.106971 | +23.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RARE-EUR | 0.01343 | +18.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.23284 | +18.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.064353 | +16.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.021313 | +16.57 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1498 scans ; 641014 observations ; 937 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
