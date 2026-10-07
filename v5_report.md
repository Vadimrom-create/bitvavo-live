# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-07T21:55:32.043594+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 426
Récupération : 2026-10-07T21:54:22.120409+00:00 | âge ticker : 183.7 s | durée : 185.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SENT-EUR : 0.023221 € ; score 77.27/100 ; SURVEILLE ; WICK_SETUP
- MAGIC-EUR : 0.05791 € ; score 74.89/100 ; SURVEILLE ; seuil achat non atteint
- ESP-EUR : 0.102215 € ; score 74.00/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.032871 € ; score 73.85/100 ; SURVEILLE ; WICK_SETUP
- PARTI-EUR : 0.030351 € ; score 73.80/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0106133 | +77.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.40122 | +36.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SAND-EUR | 0.069838 | +18.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LAPTOP-EUR | 0.07802 | +18.21 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GTC-EUR | 0.157729 | +16.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.010576 | +16.03 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAY-EUR | 2.21424 | +11.83 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8451 | +7.91 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| MOVR-EUR | 1.7505 | +6.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PROM-EUR | 4.8325 | +5.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2103 scans ; 899895 observations ; 1655 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
