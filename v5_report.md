# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T23:59:24.256696+00:00
État : OK | marchés EUR : 427 | V4 : 391 | données valides : 24
Récupération : 2026-09-19T23:58:52.013827+00:00 | âge ticker : 147.6 s | durée : 149.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 26/427 ; 15 min 72/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- NPC-EUR : STABILITY_HOLD, INVALID_5M
- PYTH-EUR : WICK_SETUP, INVALID_5M
- STX-EUR : INVALID_5M

## SURVEILLE

- HYPE-EUR : 80.235 € ; score 85.64/100 ; SURVEILLE ; WICK_SETUP
- PEPE-EUR : 3.5861e-06 € ; score 77.83/100 ; SURVEILLE ; seuil achat non atteint
- SOL-EUR : 96.558 € ; score 77.66/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.36645 € ; score 76.99/100 ; SURVEILLE ; WICK_SETUP
- TAO-EUR : 229.23 € ; score 75.62/100 ; SURVEILLE ; NOT_ENTRY_ENRICHED

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CELR-EUR | 0.0028665 | +43.36 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.071817 | +37.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| G-EUR | 0.0090049 | +37.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.075672 | +27.22 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| XTZ-EUR | 0.32193 | +25.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 8.775 | +23.05 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENA-EUR | 0.17765 | +21.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INJ-EUR | 6.8947 | +18.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOLV-EUR | 0.0039322 | +15.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKL-EUR | 0.0039793 | +15.10 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 935 scans ; 401024 observations ; 223 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
