# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T01:58:03.455911+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 430
Récupération : 2026-10-01T01:57:29.439751+00:00 | âge ticker : 155.8 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.9701 € ; score 92.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.34917 € ; score 90.24/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ATOM-EUR : 1.5475 € ; score 87.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- INJ-EUR : 6.518 € ; score 85.78/100 ; SURVEILLE ; STABILITY_HOLD
- INIT-EUR : 0.092742 € ; score 85.77/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.0136 | +83.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3691 | +54.44 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRAC-EUR | 0.43126 | +29.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.4432 | +27.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008375 | +24.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| STX-EUR | 0.33025 | +18.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.027984 | +17.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0025423 | +14.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0606011 | +14.19 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ICX-EUR | 0.0076 | +12.23 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1878 scans ; 803618 observations ; 1430 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
