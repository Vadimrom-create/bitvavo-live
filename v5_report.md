# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T04:35:56.740452+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-09-27T04:35:26.459627+00:00 | âge ticker : 146.5 s | durée : 147.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RENDER-EUR : 1.7662 € ; score 93.64/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TNSR-EUR : 0.035582 € ; score 92.06/100 ; SURVEILLE ; seuil achat non atteint
- ENA-EUR : 0.23554 € ; score 90.97/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.30173 € ; score 90.47/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : 0.12572 € ; score 90.34/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 161.862 | +86.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.25678 | +43.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006285 | +40.26 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.016705 | +24.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RUNE-EUR | 0.71581 | +22.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRC-EUR | 0.0012691 | +20.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00695 | +19.52 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 2Z-EUR | 0.059936 | +19.28 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AGI-EUR | 0.006151 | +18.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TAIKO-EUR | 0.09518 | +17.14 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1588 scans ; 679444 observations ; 1079 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
