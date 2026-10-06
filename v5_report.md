# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T21:28:09.568439+00:00
État : OK | marchés EUR : 427 | V4 : 379 | données valides : 427
Récupération : 2026-10-06T21:27:34.943579+00:00 | âge ticker : 154.2 s | durée : 155.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- API3-EUR : 0.29659 € ; score 87.02/100 ; SURVEILLE ; seuil achat non atteint
- DIA-EUR : 0.15605 € ; score 83.84/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- RENDER-EUR : 1.8814 € ; score 82.23/100 ; SURVEILLE ; seuil achat non atteint
- ENSO-EUR : 0.8804 € ; score 82.01/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- MAGIC-EUR : 0.059906 € ; score 81.49/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.00626 | +73.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.71383 | +39.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 13.9421 | +30.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.079377 | +20.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RLC-EUR | 0.69399 | +15.70 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.0209086 | +14.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29349 | +11.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.17 | +11.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDU-EUR | 0.0601 | +10.87 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| VTHO-EUR | 0.00064458 | +9.31 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2097 scans ; 897335 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
