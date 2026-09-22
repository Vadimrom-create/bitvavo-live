# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T03:15:37.253333+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-22T03:15:03.016627+00:00 | âge ticker : 153.0 s | durée : 154.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ORCA-EUR : 1.32042 € ; score 88.76/100 ; SURVEILLE ; SPREAD_RISK
- GRT-EUR : 0.020637 € ; score 86.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MERL-EUR : 0.023859 € ; score 86.32/100 ; SURVEILLE ; seuil achat non atteint
- TAIKO-EUR : 0.08058 € ; score 85.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ASTER-EUR : 0.63164 € ; score 82.96/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.016018 | +85.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0012975 | +65.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.058237 | +56.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.056749 | +53.64 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| AIOZ-EUR | 0.113431 | +42.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.047538 | +41.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3919e-06 | +25.68 % | DETECTED_EARLY | NONE | NONE |
| FORM-EUR | 0.28584 | +25.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.33862 | +22.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.21581 | +21.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1144 scans ; 490081 observations ; 445 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
