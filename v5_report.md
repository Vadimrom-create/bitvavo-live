# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T20:57:48.836540+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T20:57:15.886206+00:00 | âge ticker : 148.4 s | durée : 150.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TRB-EUR : 18.95 € ; score 92.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- KSM-EUR : 4.5474 € ; score 85.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- XLM-EUR : 0.2005 € ; score 83.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MLN-EUR : 1.3301 € ; score 82.78/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- WIF-EUR : 0.21696 € ; score 82.68/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.7647 | +68.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35016 | +46.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.42369 | +19.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008014 | +17.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.015942 | +16.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0603291 | +15.03 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PHA-EUR | 0.06864 | +13.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.43953 | +11.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.31585 | +11.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BTT-EUR | 3.5914e-07 | +10.86 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1863 scans ; 797168 observations ; 1420 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
