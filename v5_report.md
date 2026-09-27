# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T22:38:51.471395+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T22:38:18.391293+00:00 | âge ticker : 154.4 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SNX-EUR : 0.23737 € ; score 89.43/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- ORCA-EUR : 1.55946 € ; score 84.93/100 ; SURVEILLE ; SPREAD_RISK
- C-EUR : 0.0813 € ; score 84.17/100 ; SURVEILLE ; WICK_SETUP
- AAVE-EUR : 135.12 € ; score 83.98/100 ; SURVEILLE ; STABILITY_HOLD
- ACE-EUR : 0.1726 € ; score 83.01/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 224.554 | +90.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.28649 | +41.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006908 | +34.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.9986 | +31.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.030642 | +26.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| W-EUR | 0.013623 | +19.68 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.004417 | +15.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006839 | +13.91 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOM-EUR | 0.0020735 | +13.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.007176 | +11.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1652 scans ; 706772 observations ; 1186 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
