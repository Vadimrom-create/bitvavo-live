# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T01:02:39.111192+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T01:02:04.456833+00:00 | âge ticker : 148.3 s | durée : 149.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GALA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- DYDX-EUR : 0.12556 € ; score 91.12/100 ; SURVEILLE ; SPREAD_RISK
- SPK-EUR : 0.02165 € ; score 86.91/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- HYPE-EUR : 81.53 € ; score 85.60/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.12598 € ; score 83.95/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7517 € ; score 83.95/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 141.113 | +62.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006949 | +56.65 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.007759 | +40.46 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| RARE-EUR | 0.017522 | +32.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.060379 | +19.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.67697 | +18.18 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.209 | +17.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.81993 | +16.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.04215 | +15.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| COW-EUR | 0.15324 | +15.65 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1576 scans ; 674320 observations ; 1058 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
