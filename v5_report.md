# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T23:55:20.696257+00:00
État : OK | marchés EUR : 429 | V4 : 394 | données valides : 429
Récupération : 2026-09-29T23:54:47.813567+00:00 | âge ticker : 148.1 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETHFI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HUMA-EUR : 0.026055 € ; score 92.00/100 ; SURVEILLE ; WICK_SETUP
- CFG-EUR : 0.134831 € ; score 90.76/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.012171 € ; score 87.77/100 ; SURVEILLE ; WICK_SETUP
- RENDER-EUR : 1.683 € ; score 87.19/100 ; SURVEILLE ; seuil achat non atteint
- AVNT-EUR : 0.10902 € ; score 85.86/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.36771 | +34.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016797 | +32.16 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.1058 | +30.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.67922 | +29.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022311 | +23.96 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0051758 | +19.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.062878 | +17.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 235.877 | +16.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRIA-EUR | 0.004052 | +15.64 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| INIT-EUR | 0.090721 | +15.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1803 scans ; 771397 observations ; 1344 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
