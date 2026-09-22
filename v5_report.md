# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T02:23:34.455619+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T02:23:04.027986+00:00 | âge ticker : 144.7 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TRX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SSV-EUR : 2.9523 € ; score 90.68/100 ; SURVEILLE ; seuil achat non atteint
- ACE-EUR : 0.15081 € ; score 84.01/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- CTSI-EUR : 0.025673 € ; score 83.73/100 ; SURVEILLE ; SPREAD_RISK
- MERL-EUR : 0.0239 € ; score 82.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- THE-EUR : 0.0714 € ; score 81.99/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016605 | +92.63 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013138 | +67.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.060572 | +64.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.050211 | +47.16 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.109085 | +37.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30661 | +34.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.043821 | +31.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3834e-06 | +24.97 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.21492 | +23.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.33836 | +21.93 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1141 scans ; 488803 observations ; 442 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
