# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T02:01:41.353406+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-28T02:01:09.155209+00:00 | âge ticker : 145.9 s | durée : 147.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : NOT_ENTRY_ENRICHED, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- APE-EUR : 0.14169 € ; score 87.99/100 ; SURVEILLE ; seuil achat non atteint
- AEVO-EUR : 0.023312 € ; score 87.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FLUX-EUR : 0.06527 € ; score 85.48/100 ; SURVEILLE ; SPREAD_RISK
- CFG-EUR : 0.145874 € ; score 83.74/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ETHFI-EUR : 0.61679 € ; score 82.13/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 227.001 | +43.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.27131 | +30.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.07999 | +30.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030667 | +27.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.017982 | +23.02 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| INX-EUR | 0.006112 | +17.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.0736 | +15.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.004493 | +15.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRUST-EUR | 0.059933 | +11.98 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| IMX-EUR | 0.16438 | +11.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1664 scans ; 711896 observations ; 1216 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
