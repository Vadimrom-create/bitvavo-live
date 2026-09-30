# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T20:42:37.026057+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T20:42:04.545603+00:00 | âge ticker : 159.9 s | durée : 161.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- IMX-EUR : 0.14684 € ; score 91.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KAS-EUR : 0.038707 € ; score 90.69/100 ; SURVEILLE ; WICK_SETUP
- XLM-EUR : 0.20068 € ; score 90.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DYDX-EUR : 0.1277 € ; score 89.98/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- YFI-EUR : 2161.4 € ; score 87.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.6031 | +58.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35343 | +47.88 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AUDIO-EUR | 0.016736 | +22.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.42109 | +18.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007807 | +16.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0616358 | +16.59 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| PHA-EUR | 0.06955 | +14.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.43863 | +11.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BTT-EUR | 3.6005e-07 | +11.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.31449 | +10.62 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1862 scans ; 796738 observations ; 1419 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
