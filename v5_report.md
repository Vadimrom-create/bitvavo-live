# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T16:07:01.095746+00:00
État : OK | marchés EUR : 427 | V4 : 367 | données valides : 426
Récupération : 2026-10-05T16:06:29.936001+00:00 | âge ticker : 150.9 s | durée : 151.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HOT-EUR : 0.00040537 € ; score 85.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CNPY-EUR : 0.256 € ; score 83.80/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.8402 € ; score 83.22/100 ; SURVEILLE ; WICK_SETUP
- ICP-EUR : 3.0942 € ; score 82.95/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BOME-EUR : 0.0009043 € ; score 82.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.192946 | +79.77 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.48885 | +51.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.070493 | +43.01 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8696 | +20.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZEUS-EUR | 0.0024164 | +19.32 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.028285 | +16.25 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAD-EUR | 0.27377 | +15.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.045997 | +15.49 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.09151 | +15.18 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.805 | +14.88 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
