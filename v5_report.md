# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-11T12:29:30.389034+00:00
État : OK | marchés EUR : 427 | V4 : 369 | données valides : 427
Récupération : 2026-10-11T12:28:57.506870+00:00 | âge ticker : 149.1 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- PYTH-EUR : 0.068379 € ; score 85.93/100 ; SURVEILLE ; seuil achat non atteint
- NOM-EUR : 0.0020025 € ; score 84.16/100 ; SURVEILLE ; LOW_LIQUIDITY
- BOME-EUR : 0.00099236 € ; score 80.26/100 ; SURVEILLE ; seuil achat non atteint
- RECALL-EUR : 0.03915 € ; score 79.21/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- AVNT-EUR : 0.12387 € ; score 77.08/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0099713 | +62.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.1026 | +58.94 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LUMIA-EUR | 0.136804 | +29.54 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CHIP-EUR | 0.059073 | +26.97 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TIA-EUR | 0.50903 | +18.19 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SENT-EUR | 0.021033 | +18.01 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| S-EUR | 0.043817 | +14.50 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.013993 | +11.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RLC-EUR | 0.94159 | +11.45 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.0352 | +11.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2136 scans ; 913964 observations ; 1656 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
