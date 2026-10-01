# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T09:04:33.970107+00:00
État : OK | marchés EUR : 430 | V4 : 389 | données valides : 430
Récupération : 2026-10-01T09:03:59.153479+00:00 | âge ticker : 151.4 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- 0G-EUR : 0.278 € ; score 89.71/100 ; SURVEILLE ; SPREAD_RISK
- ENJ-EUR : 0.026011 € ; score 88.43/100 ; SURVEILLE ; STABILITY_HOLD
- ALICE-EUR : 0.15031 € ; score 83.30/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- ACE-EUR : 0.16598 € ; score 82.27/100 ; SURVEILLE ; WICK_SETUP
- REZ-EUR : 0.0041076 € ; score 81.62/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CT-EUR | 0.37782 | +58.08 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0027269 | +45.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.2759 | +36.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.34601 | +24.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0660707 | +21.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028577 | +19.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.43734 | +18.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DUSK-EUR | 0.085632 | +14.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JASMY-EUR | 0.0052726 | +14.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.46276 | +14.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1898 scans ; 812218 observations ; 1465 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
