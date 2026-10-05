# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T14:09:21.863757+00:00
État : OK | marchés EUR : 427 | V4 : 365 | données valides : 426
Récupération : 2026-10-05T14:08:41.856363+00:00 | âge ticker : 161.7 s | durée : 164.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- C-EUR : 0.095726 € ; score 92.42/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 3.0764 € ; score 90.59/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 63.6 € ; score 87.28/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALICE-EUR : 0.16391 € ; score 85.52/100 ; SURVEILLE ; WICK_SETUP
- ZRO-EUR : 1.7656 € ; score 85.37/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.181291 | +64.18 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.51353 | +58.02 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.072223 | +46.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8748 | +20.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.089501 | +15.57 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.045956 | +14.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZEUS-EUR | 0.0023 | +14.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.027816 | +13.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ADA-EUR | 0.246 | +13.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDU-EUR | 0.05236 | +12.72 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
