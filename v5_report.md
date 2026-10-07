# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-07T19:32:00.318829+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 426
Récupération : 2026-10-07T19:30:54.325069+00:00 | âge ticker : 179.8 s | durée : 180.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RENDER-EUR : 1.8325 € ; score 80.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.032854 € ; score 78.51/100 ; SURVEILLE ; seuil achat non atteint
- MAGIC-EUR : 0.056677 € ; score 78.00/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.9605 € ; score 74.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ESP-EUR : 0.101144 € ; score 74.04/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0124 | +143.61 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.38299 | +29.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SAND-EUR | 0.070671 | +21.44 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LAPTOP-EUR | 0.07867 | +19.27 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAY-EUR | 2.15888 | +11.11 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.010414 | +9.74 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GTC-EUR | 0.150363 | +8.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLUID-EUR | 1.8317 | +8.22 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| POND-EUR | 0.0015152 | +7.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDGE-EUR | 0.106346 | +7.23 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2102 scans ; 899469 observations ; 1655 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
