# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T07:43:07.910713+00:00
État : OK | marchés EUR : 430 | V4 : 392 | données valides : 430
Récupération : 2026-10-01T07:42:35.528338+00:00 | âge ticker : 154.3 s | durée : 155.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVNT-EUR : 0.11212 € ; score 92.29/100 ; SURVEILLE ; seuil achat non atteint
- LRC-EUR : 0.009061 € ; score 90.50/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- DIA-EUR : 0.1524 € ; score 89.30/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- JUP-EUR : 0.28651 € ; score 89.10/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- BONK-EUR : 3.3078e-06 € ; score 87.17/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.5981 | +76.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3667 | +53.43 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0025053 | +34.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.35692 | +29.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.029176 | +22.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.48229 | +20.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0648006 | +20.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.42 | +17.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICX-EUR | 0.007342 | +14.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ESP-EUR | 0.097801 | +12.81 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1894 scans ; 810498 observations ; 1450 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
