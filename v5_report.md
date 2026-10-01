# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T08:49:30.814088+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 430
Récupération : 2026-10-01T08:48:55.560944+00:00 | âge ticker : 155.2 s | durée : 156.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- 0G-EUR : 0.27811 € ; score 86.21/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- ALICE-EUR : 0.15024 € ; score 83.30/100 ; SURVEILLE ; WICK_SETUP
- PTB-EUR : 0.0008423 € ; score 82.46/100 ; SURVEILLE ; WICK_SETUP
- TNSR-EUR : 0.035405 € ; score 82.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HUMA-EUR : 0.029091 € ; score 81.98/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.3636 | +52.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0027566 | +47.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.4236 | +43.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.34549 | +24.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.43248 | +22.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0650778 | +19.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028591 | +19.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DUSK-EUR | 0.08744 | +17.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.46579 | +17.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0053146 | +16.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1897 scans ; 811788 observations ; 1462 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
