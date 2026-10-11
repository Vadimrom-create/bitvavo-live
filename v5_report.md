# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-11T12:43:37.466450+00:00
État : OK | marchés EUR : 427 | V4 : 371 | données valides : 427
Récupération : 2026-10-11T12:43:04.991216+00:00 | âge ticker : 148.4 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- JUP-EUR : 0.32518 € ; score 91.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.1249 € ; score 78.78/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AERO-EUR : 0.87211 € ; score 78.72/100 ; SURVEILLE ; SPREAD_RISK
- AVAX-EUR : 9.3364 € ; score 78.70/100 ; SURVEILLE ; seuil achat non atteint
- NMR-EUR : 12.2211 € ; score 77.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0104275 | +62.93 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.10201 | +58.71 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CHIP-EUR | 0.059583 | +27.27 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LUMIA-EUR | 0.135716 | +24.13 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TIA-EUR | 0.51357 | +19.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SENT-EUR | 0.020792 | +16.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.96173 | +15.06 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| S-EUR | 0.04367 | +14.13 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.014024 | +12.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MAGIC-EUR | 0.10742 | +11.30 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2136 scans ; 913964 observations ; 1656 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
