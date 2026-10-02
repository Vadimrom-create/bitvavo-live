# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T14:33:59.474494+00:00
État : OK | marchés EUR : 426 | V4 : 386 | données valides : 426
Récupération : 2026-10-02T14:33:20.605600+00:00 | âge ticker : 162.9 s | durée : 163.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- EIGEN-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- KAIA-EUR : 0.033141 € ; score 89.78/100 ; SURVEILLE ; seuil achat non atteint
- STRK-EUR : 0.039617 € ; score 87.12/100 ; SURVEILLE ; seuil achat non atteint
- ZIG-EUR : 0.051569 € ; score 85.61/100 ; SURVEILLE ; WICK_SETUP
- NOM-EUR : 0.00234 € ; score 85.08/100 ; SURVEILLE ; WICK_SETUP
- RLC-EUR : 0.34227 € ; score 84.20/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.057365 | +51.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.11212 | +26.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.15538 | +19.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.030218 | +17.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.09148 | +17.63 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SKY-EUR | 0.08303 | +17.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.7326 | +17.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0023399 | +16.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.54319 | +16.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.089903 | +15.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1984 scans ; 849170 observations ; 1567 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
