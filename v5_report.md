# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T23:50:00.088239+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-09-30T23:49:22.725990+00:00 | âge ticker : 156.4 s | durée : 157.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- POL-EUR : 0.100334 € ; score 90.94/100 ; SURVEILLE ; seuil achat non atteint
- LINEA-EUR : 0.0025734 € ; score 89.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KITE-EUR : 0.12568 € ; score 87.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TIA-EUR : 0.39025 € ; score 85.70/100 ; SURVEILLE ; WICK_SETUP
- KSM-EUR : 4.5745 € ; score 83.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.9241 | +76.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3542 | +48.20 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008458 | +23.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.027999 | +18.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.32818 | +17.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.43149 | +17.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0599462 | +13.57 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOMI-EUR | 0.19824 | +13.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0042068 | +11.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0020738 | +11.64 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1872 scans ; 801038 observations ; 1428 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
