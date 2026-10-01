# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T13:28:42.666107+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-01T13:28:07.374112+00:00 | âge ticker : 148.1 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WIF-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- C-EUR : 0.08156 € ; score 86.63/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- ZRO-EUR : 1.4934 € ; score 85.10/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 144.44 € ; score 83.69/100 ; SURVEILLE ; WICK_SETUP
- MOVE-EUR : 0.008959 € ; score 81.94/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK
- PROM-EUR : 5.7896 € ; score 81.94/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00054 | +110.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.4775 | +80.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.45756 | +36.59 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AUDIO-EUR | 0.016786 | +23.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.068678 | +23.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0024348 | +17.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.028645 | +14.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0051684 | +13.62 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| STX-EUR | 0.3309 | +12.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.136892 | +11.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1910 scans ; 817378 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
