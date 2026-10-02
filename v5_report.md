# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T23:11:27.202446+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-02T23:10:56.961971+00:00 | âge ticker : 152.3 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AXS-EUR : INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- FLUID-EUR : 1.4199 € ; score 93.29/100 ; SURVEILLE ; WICK_SETUP
- IMX-EUR : 0.15687 € ; score 92.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- BCH-EUR : 274.84 € ; score 86.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HUMA-EUR : 0.029834 € ; score 86.34/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.545 € ; score 86.29/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.058357 | +46.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023249 | +15.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0058714 | +12.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.088398 | +12.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.029493 | +10.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14549 | +10.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.53631 | +9.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SPK-EUR | 0.022728 | +8.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.4791 | +8.03 % | DETECTED_EARLY | NONE | NONE |
| INIT-EUR | 0.100073 | +7.76 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2012 scans ; 861098 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
