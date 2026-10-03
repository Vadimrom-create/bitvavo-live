# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T06:52:32.201712+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-10-03T06:51:58.765843+00:00 | âge ticker : 153.5 s | durée : 154.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CRV-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUPER-EUR : 0.21539 € ; score 87.73/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.0793 € ; score 86.42/100 ; SURVEILLE ; seuil achat non atteint
- INIT-EUR : 0.09943 € ; score 86.36/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- LTC-EUR : 61.725 € ; score 84.36/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- COMP-EUR : 21.949 € ; score 84.30/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.069126 | +61.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.095435 | +19.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ENJ-EUR | 0.031268 | +14.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IMX-EUR | 0.1735 | +13.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0023706 | +13.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0059674 | +12.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14781 | +10.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.062324 | +9.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PIXEL-EUR | 0.0056946 | +9.04 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AXS-EUR | 1.116 | +8.50 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2033 scans ; 870044 observations ; 1604 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
