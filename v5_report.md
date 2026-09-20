# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T01:36:10.763556+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 22
Récupération : 2026-09-20T01:35:37.497918+00:00 | âge ticker : 157.8 s | durée : 158.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 25/427 ; 15 min 66/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- POL-EUR : INVALID_5M, MISSING_LATEST_CLOSED_CANDLE
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- UNI-EUR : WICK_SETUP, CHASE_RISK, INVALID_5M

## SURVEILLE

- ONDO-EUR : 0.35548 € ; score 79.37/100 ; SURVEILLE ; WICK_SETUP
- VET-EUR : 0.0074627 € ; score 74.57/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 230.03 € ; score 74.03/100 ; SURVEILLE ; STABILITY_HOLD
- SOL-EUR : 95.836 € ; score 72.02/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0037774 | +89.39 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| G-EUR | 0.0095011 | +50.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.071168 | +31.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.18158 | +22.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKL-EUR | 0.0041848 | +20.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.074699 | +20.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| INJ-EUR | 6.95 | +18.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 8.5713 | +18.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOLV-EUR | 0.0039926 | +16.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XTZ-EUR | 0.30252 | +16.35 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 940 scans ; 403159 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
