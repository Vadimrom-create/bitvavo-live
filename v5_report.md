# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T13:14:43.938473+00:00
État : OK | marchés EUR : 426 | V4 : 355 | données valides : 426
Récupération : 2026-10-04T13:14:11.543844+00:00 | âge ticker : 154.2 s | durée : 155.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WIF-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- VIRTUAL-EUR : 0.70632 € ; score 86.86/100 ; SURVEILLE ; seuil achat non atteint
- ILV-EUR : 3.7988 € ; score 83.22/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ACU-EUR : 0.12309 € ; score 82.94/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GALA-EUR : 0.0022562 € ; score 82.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PUMP-EUR : 0.005585 € ; score 81.93/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 1.05655 | +31.41 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BEAM-EUR | 0.0024035 | +28.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.049351 | +25.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.111917 | +23.30 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.61055 | +16.41 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AKT-EUR | 0.67088 | +15.21 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0023487 | +13.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AXS-EUR | 1.2172 | +13.47 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BAT-EUR | 0.09502 | +12.96 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FUN-EUR | 0.017296 | +12.02 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2055 scans ; 879416 observations ; 1629 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
