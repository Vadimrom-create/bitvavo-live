# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-04T18:01:17.204119+00:00
État : OK | marchés EUR : 426 | V4 : 350 | données valides : 426
Récupération : 2026-10-04T18:00:45.291051+00:00 | âge ticker : 153.3 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PEAQ-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MON-EUR : 0.030545 € ; score 91.77/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PEAQ-EUR : 0.0398 € ; score 90.08/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.21403 € ; score 86.46/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.08362 € ; score 85.76/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0168546 € ; score 85.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.131305 | +28.44 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDGE-EUR | 0.111585 | +24.23 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| BEAM-EUR | 0.0023142 | +22.95 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AKT-EUR | 0.7051 | +16.04 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOS-EUR | 0.62961 | +15.29 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AXS-EUR | 1.1999 | +12.79 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| POND-EUR | 0.0016181 | +12.24 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PHA-EUR | 0.068866 | +11.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0023448 | +11.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.021463 | +11.20 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2059 scans ; 881120 observations ; 1631 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
