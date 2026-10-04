# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T18:14:11.223013+00:00
État : OK | marchés EUR : 426 | V4 : 348 | données valides : 426
Récupération : 2026-10-04T18:13:37.229609+00:00 | âge ticker : 165.2 s | durée : 167.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEAQ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SKY-EUR : 0.083521 € ; score 84.86/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 159.99 € ; score 84.80/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.23287 € ; score 82.92/100 ; SURVEILLE ; seuil achat non atteint
- MON-EUR : 0.030468 € ; score 82.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HUMA-EUR : 0.031162 € ; score 82.86/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.133309 | +30.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDGE-EUR | 0.111616 | +24.26 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BEAM-EUR | 0.0023197 | +23.22 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AKT-EUR | 0.70683 | +17.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.62286 | +14.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AXS-EUR | 1.2112 | +13.86 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| POND-EUR | 0.0016297 | +13.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BAT-EUR | 0.0933 | +10.98 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PHA-EUR | 0.0686 | +10.55 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0023111 | +10.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2060 scans ; 881546 observations ; 1631 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
