# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T07:09:12.173768+00:00
État : OK | marchés EUR : 426 | V4 : 355 | données valides : 426
Récupération : 2026-10-05T07:08:06.166394+00:00 | âge ticker : 179.5 s | durée : 180.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SKY-EUR : 0.085414 € ; score 79.09/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- DEEP-EUR : 0.02195 € ; score 77.91/100 ; SURVEILLE ; SPREAD_RISK
- BAT-EUR : 0.09265 € ; score 77.31/100 ; SURVEILLE ; STABILITY_HOLD
- AAVE-EUR : 161.67 € ; score 76.59/100 ; SURVEILLE ; STABILITY_HOLD
- C-EUR : 0.091873 € ; score 76.04/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.173 | +69.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.094303 | +19.91 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.045916 | +15.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FET-EUR | 0.2269 | +14.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SCR-EUR | 0.025691 | +13.75 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BEAM-EUR | 0.0023407 | +13.35 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| HNT-EUR | 0.50664 | +12.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.63264 | +12.02 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ADA-EUR | 0.24237 | +11.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VIRTUAL-EUR | 0.77622 | +10.21 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2066 scans ; 884102 observations ; 1638 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
