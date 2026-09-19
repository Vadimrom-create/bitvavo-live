# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T17:21:16.615207+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 35
Récupération : 2026-09-19T17:20:50.407769+00:00 | âge ticker : 141.7 s | durée : 144.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 38/427 ; 15 min 89/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INVALID_5M
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BIGTIME-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, INVALID_5M
- SHIB-EUR : INVALID_5M
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : SELLER_HEAVY_BOOK, INVALID_5M
- WLD-EUR : INVALID_5M

## SURVEILLE

- SUI-EUR : 0.75271 € ; score 91.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.2006 € ; score 87.74/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 80.837 € ; score 79.86/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : 97.524 € ; score 79.14/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0036343 € ; score 78.56/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZAMA-EUR | 0.072044 | +41.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.208155 | +36.71 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.41131 | +29.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.31123 | +27.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.17893 | +25.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FIL-EUR | 0.94198 | +22.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.071298 | +21.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 8.5015 | +21.06 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| G-EUR | 0.0090153 | +19.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CROSS-EUR | 0.134744 | +18.02 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 908 scans ; 389495 observations ; 211 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
