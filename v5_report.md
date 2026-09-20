# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T00:49:51.597882+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 21
Récupération : 2026-09-20T00:49:18.567818+00:00 | âge ticker : 155.6 s | durée : 156.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 22/427 ; 15 min 67/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : INVALID_15M, INVALID_5M
- HBAR-EUR : WICK_SETUP, INVALID_5M
- HYPE-EUR : STABILITY_HOLD, INVALID_5M
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- POL-EUR : WICK_SETUP, INVALID_5M
- PUMP-EUR : STABILITY_HOLD, INVALID_5M
- PYTH-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INVALID_15M, INVALID_5M

## SURVEILLE

- TAO-EUR : 233.14 € ; score 80.50/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 0.75572 € ; score 80.34/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.36706 € ; score 79.67/100 ; SURVEILLE ; WICK_SETUP
- FET-EUR : 0.15458 € ; score 79.47/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.007575 € ; score 78.43/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0036611 | +83.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0093641 | +48.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.072125 | +29.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.2298 | +27.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.18106 | +22.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XTZ-EUR | 0.31325 | +21.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZIL-EUR | 0.0032315 | +19.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INJ-EUR | 7.0485 | +19.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.0040319 | +16.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.072112 | +16.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 937 scans ; 401878 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
