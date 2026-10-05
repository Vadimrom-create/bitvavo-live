# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T22:33:27.512378+00:00
État : OK | marchés EUR : 427 | V4 : 373 | données valides : 427
Récupération : 2026-10-05T22:32:52.399063+00:00 | âge ticker : 151.5 s | durée : 152.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ENS-EUR : 6.152 € ; score 85.36/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.24319 € ; score 82.50/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.02258 € ; score 82.25/100 ; SURVEILLE ; seuil achat non atteint
- API3-EUR : 0.28121 € ; score 81.02/100 ; SURVEILLE ; SPREAD_RISK
- AXS-EUR : 1.1567 € ; score 80.65/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| RLC-EUR | 0.66495 | +105.60 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZEUS-EUR | 0.0035982 | +75.52 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAD-EUR | 0.32471 | +37.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.098561 | +25.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.8734 | +18.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 1.7779 | +18.42 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ORCA-EUR | 2.09362 | +18.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PNT-EUR | 0.057018 | +15.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05367 | +14.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0655738 | +13.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2083 scans ; 891357 observations ; 1648 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
