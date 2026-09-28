# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T21:34:44.439439+00:00
État : OK | marchés EUR : 428 | V4 : 402 | données valides : 428
Récupération : 2026-09-28T21:34:13.495478+00:00 | âge ticker : 153.3 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- VIRTUAL-EUR : 0.72155 € ; score 91.54/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.0676e-06 € ; score 81.87/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.007408 € ; score 81.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.070676 € ; score 80.79/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.69103 € ; score 80.76/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.109 | +30.82 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.119162 | +14.57 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 10.0083 | +13.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018363 | +10.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.98526 | +9.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048726 | +9.15 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LINK-EUR | 13.4006 | +8.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 214.738 | +6.85 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DGB-EUR | 0.0041958 | +6.64 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AZTEC-EUR | 0.01718 | +6.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1722 scans ; 736689 observations ; 1266 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
