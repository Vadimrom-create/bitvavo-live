# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T22:04:33.324373+00:00
État : OK | marchés EUR : 428 | V4 : 401 | données valides : 428
Récupération : 2026-09-28T22:03:58.869588+00:00 | âge ticker : 148.6 s | durée : 150.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MLN-EUR : 1.3133 € ; score 89.20/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP
- PYTH-EUR : 0.070731 € ; score 86.74/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- C-EUR : 0.079202 € ; score 84.84/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- W-EUR : 0.011883 € ; score 84.00/100 ; SURVEILLE ; seuil achat non atteint
- DATAIP-EUR : 0.195 € ; score 81.08/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.1836 | +37.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.10753 | +29.68 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.118705 | +14.88 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.99664 | +9.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.04828 | +9.01 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0018056 | +8.24 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.2487 | +8.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 208.183 | +6.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.016519 | +5.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0490275 | +5.11 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1724 scans ; 737545 observations ; 1268 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
