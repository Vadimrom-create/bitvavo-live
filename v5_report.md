# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T09:35:55.293261+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-23T09:35:21.479914+00:00 | âge ticker : 154.6 s | durée : 155.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MOVR-EUR : 0.8342 € ; score 87.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PARTI-EUR : 0.023567 € ; score 86.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.059174 € ; score 83.52/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ARPA-EUR : 0.0103179 € ; score 83.33/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- MEME-EUR : 0.00057013 € ; score 82.82/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MET-EUR | 0.34858 | +39.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.034 | +38.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 313.71 | +34.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.17158 | +29.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019723 | +28.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALLO-EUR | 0.289147 | +25.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2762 | +24.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TIA-EUR | 0.46675 | +21.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PENGU-EUR | 0.0096714 | +21.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.019914 | +19.04 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1259 scans ; 539071 observations ; 633 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
