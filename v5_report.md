# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T19:45:26.261256+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-25T19:44:53.726119+00:00 | âge ticker : 147.4 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SENT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RPL-EUR : 1.8292 € ; score 91.30/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- XLM-EUR : 0.19274 € ; score 89.69/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.02013 € ; score 89.29/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : 0.40785 € ; score 88.56/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- 2Z-EUR : 0.052246 € ; score 87.69/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.073448 | +67.13 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.20984 | +28.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.014686 | +27.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.48157 | +22.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.08818 | +20.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.22846 | +18.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.73056 | +18.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.062803 | +16.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.02278 | +16.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.11574 | +15.29 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1467 scans ; 627777 observations ; 880 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
