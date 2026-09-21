# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T22:16:55.383736+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-21T22:16:21.423984+00:00 | âge ticker : 155.3 s | durée : 156.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MANTA-EUR : 0.061097 € ; score 90.51/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- THE-EUR : 0.07074 € ; score 89.51/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.062873 € ; score 89.38/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.029598 € ; score 84.95/100 ; SURVEILLE ; seuil achat non atteint
- COW-EUR : 0.13708 € ; score 84.32/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0014875 | +90.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.0162 | +88.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.13 | +59.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZETA-EUR | 0.052199 | +51.51 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FORM-EUR | 0.31449 | +39.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043522 | +34.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PTB-EUR | 0.0010656 | +32.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008439 | +31.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUFFER-EUR | 0.026178 | +24.40 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SYN-EUR | 0.227676 | +22.37 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1124 scans ; 481561 observations ; 406 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
