# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-12T17:33:32.495541+00:00
État : OK | marchés EUR : 427 | V4 : 378 | données valides : 427
Récupération : 2026-10-12T17:32:18.678341+00:00 | âge ticker : 198.4 s | durée : 199.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- STX-EUR : 0.36315 € ; score 76.23/100 ; SURVEILLE ; seuil achat non atteint
- CYBER-EUR : 0.34768 € ; score 74.70/100 ; SURVEILLE ; SPREAD_RISK
- TIA-EUR : 0.48985 € ; score 73.30/100 ; SURVEILLE ; seuil achat non atteint
- PARTI-EUR : 0.030896 € ; score 72.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZK-EUR : 0.013204 € ; score 72.11/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.27065 | +67.86 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RSR-EUR | 0.0020266 | +38.54 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OSMO-EUR | 0.04351 | +36.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CTK-EUR | 0.15093 | +30.34 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| W-EUR | 0.019021 | +12.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAFE-EUR | 0.116139 | +11.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PYTH-EUR | 0.076681 | +10.88 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CT-EUR | 0.31624 | +10.05 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OGN-EUR | 0.0325 | +9.92 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CYBER-EUR | 0.34768 | +9.53 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2146 scans ; 918234 observations ; 1658 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
