# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T23:09:19.941539+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T23:08:20.611154+00:00 | âge ticker : 174.2 s | durée : 174.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- JUP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- TREE-EUR : 0.04186 € ; score 90.96/100 ; SURVEILLE ; seuil achat non atteint
- FIL-EUR : 0.81686 € ; score 89.83/100 ; SURVEILLE ; seuil achat non atteint
- SLX-EUR : 0.06395 € ; score 81.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- 0G-EUR : 0.21816 € ; score 80.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MEW-EUR : 0.00042109 € ; score 79.71/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.10495 | +52.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.032076 | +25.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.042387 | +21.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017643 | +20.83 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NOM-EUR | 0.0017481 | +14.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.76774 | +11.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0455019 | +10.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.2895 | +10.02 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SUPER-EUR | 0.15395 | +9.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LSK-EUR | 0.30073 | +8.72 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1307 scans ; 559519 observations ; 669 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
