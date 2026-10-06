# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T20:54:32.318265+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-10-06T20:53:57.089380+00:00 | âge ticker : 148.5 s | durée : 149.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AKT-EUR : 0.6828 € ; score 92.17/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HNT-EUR : 0.46243 € ; score 84.81/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- RENDER-EUR : 1.9026 € ; score 81.37/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.7514 € ; score 80.52/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- BAND-EUR : 0.21474 € ; score 79.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0057141 | +62.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.71135 | +38.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 13.8987 | +30.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0785179 | +19.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RLC-EUR | 0.67866 | +16.55 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.06064 | +13.86 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29694 | +12.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.172 | +12.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NPC-EUR | 0.0203966 | +11.47 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| VTHO-EUR | 0.0006396 | +8.79 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2088 scans ; 893492 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
