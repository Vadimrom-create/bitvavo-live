# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T11:30:28.806148+00:00
État : OK | marchés EUR : 430 | V4 : 389 | données valides : 430
Récupération : 2026-10-01T11:29:55.986294+00:00 | âge ticker : 149.3 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GTC-EUR : 0.089097 € ; score 90.02/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- GRT-EUR : 0.025643 € ; score 89.50/100 ; SURVEILLE ; WICK_SETUP
- KSM-EUR : 4.5826 € ; score 89.16/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- RECALL-EUR : 0.042614 € ; score 86.62/100 ; SURVEILLE ; WICK_SETUP
- AVAX-EUR : 9.7626 € ; score 86.60/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00054429 | +114.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6116 | +67.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0027161 | +38.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0670482 | +21.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BTT-EUR | 3.7171e-07 | +19.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.33822 | +19.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028648 | +18.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0053182 | +16.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.46925 | +16.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HUMA-EUR | 0.030258 | +15.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1905 scans ; 815228 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
