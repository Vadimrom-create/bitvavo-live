# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T19:23:43.787458+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 35
Récupération : 2026-09-19T19:23:10.736801+00:00 | âge ticker : 148.7 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 35/427 ; 15 min 98/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- JUP-EUR : STABILITY_HOLD, INVALID_5M
- VET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XLM-EUR : 0.17369 € ; score 89.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.245 € ; score 82.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.7528 € ; score 81.17/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.20008 € ; score 76.85/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 228.12 € ; score 74.29/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.080296 | +53.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.212712 | +40.51 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.45996 | +39.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0087566 | +34.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.32148 | +31.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.070878 | +21.12 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ENA-EUR | 0.17452 | +20.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.9 | +19.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.4462 | +16.45 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CELR-EUR | 0.0023156 | +16.20 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 916 scans ; 392911 observations ; 216 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
