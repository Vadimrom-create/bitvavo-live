# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T13:02:06.592164+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-01T13:01:32.482288+00:00 | âge ticker : 162.2 s | durée : 163.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.4851 € ; score 89.32/100 ; SURVEILLE ; seuil achat non atteint
- C-EUR : 0.081705 € ; score 86.06/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- WIF-EUR : 0.22067 € ; score 84.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EPIC-EUR : 0.4913 € ; score 84.02/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- KSM-EUR : 4.6264 € ; score 81.12/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00068005 | +166.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5737 | +83.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0026967 | +33.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43337 | +30.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0684308 | +23.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.029183 | +17.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33377 | +14.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.0052747 | +14.64 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| HEI-EUR | 0.140115 | +14.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.45866 | +13.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1909 scans ; 816948 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
