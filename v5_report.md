# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-14T22:44:29.955642+00:00
État : OK | marchés EUR : 427 | V4 : 372 | données valides : 427
Récupération : 2026-10-14T22:43:25.884611+00:00 | âge ticker : 186.0 s | durée : 186.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- OP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- STX-EUR : 0.38131 € ; score 80.97/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.076818 € ; score 78.48/100 ; SURVEILLE ; WICK_SETUP
- ICNT-EUR : 0.09846 € ; score 77.28/100 ; SURVEILLE ; seuil achat non atteint
- FLUID-EUR : 2.186 € ; score 75.74/100 ; SURVEILLE ; STABILITY_HOLD
- TIA-EUR : 0.49609 € ; score 75.11/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| WAL-EUR | 0.056904 | +65.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AVA-EUR | 0.2512 | +19.00 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| DEEP-EUR | 0.022281 | +17.81 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OSMO-EUR | 0.043795 | +17.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.036278 | +16.32 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.081199 | +14.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AXL-EUR | 0.055465 | +14.04 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PYTH-EUR | 0.076818 | +9.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.00158 | +8.97 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.009086 | +7.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2162 scans ; 925066 observations ; 1658 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
