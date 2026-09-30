# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T15:57:53.804461+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 429
Récupération : 2026-09-30T15:57:19.348272+00:00 | âge ticker : 149.9 s | durée : 151.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- GRT-EUR : 0.025989 € ; score 89.92/100 ; SURVEILLE ; seuil achat non atteint
- RECALL-EUR : 0.04315 € ; score 88.14/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0020041 € ; score 88.05/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 1.04174 € ; score 85.14/100 ; SURVEILLE ; seuil achat non atteint
- XAN-EUR : 0.0113442 € ; score 84.85/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5179 | +62.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.34498 | +44.34 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.45908 | +31.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.26436 | +21.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 263.674 | +19.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00778 | +17.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EPIC-EUR | 0.50103 | +16.75 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOM-EUR | 0.0020948 | +16.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| REZ-EUR | 0.0043509 | +15.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.079 | +14.86 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1848 scans ; 790718 observations ; 1390 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
