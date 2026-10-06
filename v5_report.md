# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T20:38:13.185261+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-10-06T20:37:39.062510+00:00 | âge ticker : 150.1 s | durée : 151.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SOMI-EUR : 0.18779 € ; score 87.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WAL-EUR : 0.033207 € ; score 81.66/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.2413 € ; score 81.06/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.9068 € ; score 80.87/100 ; SURVEILLE ; seuil achat non atteint
- BAND-EUR : 0.21474 € ; score 80.70/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.005449 | +53.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.61052 | +32.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 14.0553 | +31.71 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0785134 | +18.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RLC-EUR | 0.68909 | +14.23 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29628 | +12.44 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.198 | +12.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NPC-EUR | 0.0203845 | +11.91 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05925 | +10.19 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.029808 | +8.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2088 scans ; 893492 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
