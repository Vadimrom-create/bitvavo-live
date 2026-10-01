# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T12:38:28.503270+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-01T12:37:52.060436+00:00 | âge ticker : 159.8 s | durée : 160.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WOO-EUR : 0.01215 € ; score 90.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- EPIC-EUR : 0.48827 € ; score 90.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PEPE-EUR : 3.8967e-06 € ; score 88.12/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.113319 € ; score 88.04/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : 0.21999 € ; score 86.79/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.0008 | +214.08 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6383 | +82.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0027009 | +35.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43464 | +31.17 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0671201 | +21.60 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.029444 | +20.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33294 | +16.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.005288 | +16.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOS-EUR | 0.46012 | +13.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0051925 | +13.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1908 scans ; 816518 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
