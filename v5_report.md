# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T10:45:12.144807+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-23T10:44:39.988640+00:00 | âge ticker : 155.2 s | durée : 156.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- RAY-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- XVG-EUR : 0.0027256 € ; score 89.64/100 ; SURVEILLE ; STABILITY_HOLD
- ILV-EUR : 3.4385 € ; score 82.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 55.099 € ; score 81.99/100 ; SURVEILLE ; WICK_SETUP
- API3-EUR : 0.24616 € ; score 81.28/100 ; SURVEILLE ; seuil achat non atteint
- DOGS-EUR : 4.4472e-05 € ; score 81.20/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MET-EUR | 0.34889 | +37.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.033396 | +36.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.020128 | +33.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 305.41 | +28.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2924 | +26.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.16354 | +24.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.282114 | +24.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.46511 | +22.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.085291 | +22.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.019665 | +20.08 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1263 scans ; 540775 observations ; 638 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
