# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T22:56:48.742371+00:00
État : OK | marchés EUR : 428 | V4 : 400 | données valides : 428
Récupération : 2026-09-28T22:56:15.974030+00:00 | âge ticker : 147.9 s | durée : 149.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ETC-EUR : 8.1138 € ; score 90.05/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.011699 € ; score 87.04/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- CRV-EUR : 0.32205 € ; score 86.63/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.72226 € ; score 85.64/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- GRAM-EUR : 1.3819 € ; score 84.17/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.7237 | +43.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.108147 | +30.37 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.11847 | +14.30 % | DETECTED_EARLY | NONE | NONE |
| MIOTA-EUR | 0.048872 | +9.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0018186 | +9.20 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.35 | +8.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016646 | +6.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.24236 | +6.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NPC-EUR | 0.0204775 | +5.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.049574 | +5.63 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1727 scans ; 738829 observations ; 1270 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
