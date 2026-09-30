# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T10:46:19.220236+00:00
État : OK | marchés EUR : 430 | V4 : 393 | données valides : 429
Récupération : 2026-09-30T10:45:46.012862+00:00 | âge ticker : 153.2 s | durée : 154.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ALGO-EUR : 0.110346 € ; score 93.72/100 ; SURVEILLE ; WICK_SETUP
- MMT-EUR : 0.16816 € ; score 92.43/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- RUNE-EUR : 0.68846 € ; score 91.62/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- NEAR-EUR : 4.5779 € ; score 91.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.29307 € ; score 91.20/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.6022 | +80.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.33778 | +41.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.40655 | +32.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.008564 | +26.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.097492 | +26.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.26659 | +22.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.068449 | +21.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.39 | +16.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 259.568 | +14.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.5554 | +13.29 % | DETECTED_EARLY | NONE | NONE |

Historique : 1834 scans ; 784698 observations ; 1368 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
