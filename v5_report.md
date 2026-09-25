# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T07:50:39.650115+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-25T07:50:09.559481+00:00 | âge ticker : 146.6 s | durée : 148.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- BEAM-EUR : 0.0017863 € ; score 92.67/100 ; SURVEILLE ; SPREAD_RISK
- LTC-EUR : 62.876 € ; score 92.05/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MOODENG-EUR : 0.042646 € ; score 88.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KSM-EUR : 4.0332 € ; score 87.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- JTO-EUR : 0.44085 € ; score 85.97/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| TREAD-EUR | 0.755 | +52.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 87.613 | +38.94 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.101759 | +27.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.48971 | +26.13 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.18237 | +20.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.049513 | +19.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.085953 | +18.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.021581 | +18.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.20282 | +15.34 % | DETECTED_EARLY | NONE | NONE |
| LDO-EUR | 0.4015 | +14.96 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique : 1428 scans ; 611124 observations ; 817 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
