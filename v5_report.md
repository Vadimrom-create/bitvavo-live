# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T10:54:21.307369+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T10:53:46.081305+00:00 | âge ticker : 146.1 s | durée : 146.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- QNT-EUR : 60.167 € ; score 84.89/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.18967 € ; score 84.16/100 ; SURVEILLE ; STABILITY_HOLD
- RLC-EUR : 0.29786 € ; score 79.63/100 ; SURVEILLE ; SPREAD_RISK
- COW-EUR : 0.1401 € ; score 79.48/100 ; SURVEILLE ; seuil achat non atteint
- ALIGN-EUR : 0.005934 € ; score 79.45/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017833 | +103.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014698 | +87.19 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.1164 | +36.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| U-EUR | 0.0002911 | +34.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.05687 | +30.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FORM-EUR | 0.28776 | +24.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.22499 | +21.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.38517 | +19.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.069648 | +19.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2876e-06 | +17.81 % | DETECTED_EARLY | NONE | NONE |

Historique : 1176 scans ; 503713 observations ; 479 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
