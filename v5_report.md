# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-11T13:34:36.839972+00:00
État : OK | marchés EUR : 427 | V4 : 367 | données valides : 427
Récupération : 2026-10-11T13:33:31.531611+00:00 | âge ticker : 176.9 s | durée : 178.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AVNT-EUR : 0.12511 € ; score 81.05/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AERO-EUR : 0.86909 € ; score 79.28/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.7746 € ; score 78.85/100 ; SURVEILLE ; seuil achat non atteint
- W-EUR : 0.015555 € ; score 78.74/100 ; SURVEILLE ; seuil achat non atteint
- JUP-EUR : 0.32678 € ; score 76.67/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0098893 | +54.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.097332 | +50.67 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CHIP-EUR | 0.059922 | +28.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LUMIA-EUR | 0.129061 | +24.75 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TIA-EUR | 0.51296 | +18.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MAGIC-EUR | 0.112628 | +16.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.66215 | +15.49 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| S-EUR | 0.044237 | +15.14 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| SENT-EUR | 0.020129 | +13.82 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZK-EUR | 0.014076 | +12.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2136 scans ; 913964 observations ; 1656 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
