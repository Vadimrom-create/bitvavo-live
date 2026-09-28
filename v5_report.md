# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T17:03:33.934139+00:00
État : OK | marchés EUR : 428 | V4 : 403 | données valides : 427
Récupération : 2026-09-28T17:02:33.180338+00:00 | âge ticker : 179.4 s | durée : 180.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XDC-EUR : SPREAD_RISK, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CRO-EUR : 0.060541 € ; score 92.21/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- XDC-EUR : 0.030242 € ; score 86.65/100 ; SURVEILLE ; SPREAD_RISK, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 13.4015 € ; score 83.64/100 ; SURVEILLE ; seuil achat non atteint
- PEAQ-EUR : 0.0361 € ; score 81.60/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.71731 € ; score 80.09/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.110458 | +34.41 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 211.615 | +31.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.00191 | +15.55 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ALGO-EUR | 0.116957 | +13.33 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 9.7805 | +12.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.025827 | +11.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.01817 | +11.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0046863 | +9.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.02745 | +9.07 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.047909 | +8.98 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1707 scans ; 730269 observations ; 1261 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
