# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T15:43:34.615814+00:00
État : OK | marchés EUR : 428 | V4 : 402 | données valides : 427
Récupération : 2026-09-28T15:43:00.176750+00:00 | âge ticker : 149.1 s | durée : 151.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XDC-EUR : 0.030293 € ; score 83.55/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MON-EUR : 0.025257 € ; score 82.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MIOTA-EUR : 0.047292 € ; score 79.75/100 ; SURVEILLE ; seuil achat non atteint
- ZBT-EUR : 0.074242 € ; score 78.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.068955 € ; score 78.51/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.108126 | +32.09 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 194.859 | +22.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0019203 | +15.56 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AZTEC-EUR | 0.016555 | +14.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.116733 | +13.80 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 9.7269 | +13.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.027636 | +11.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.025257 | +9.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDC-EUR | 0.030293 | +8.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.047292 | +7.27 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1703 scans ; 728557 observations ; 1250 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
