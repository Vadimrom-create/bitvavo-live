# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T00:58:25.711480+00:00
État : OK | marchés EUR : 430 | V4 : 394 | données valides : 430
Récupération : 2026-10-01T00:57:54.842839+00:00 | âge ticker : 149.1 s | durée : 149.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- W-EUR : 0.011924 € ; score 92.52/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.44476 € ; score 91.90/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 1.03653 € ; score 90.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : 0.101437 € ; score 85.07/100 ; SURVEILLE ; seuil achat non atteint
- BIGTIME-EUR : 0.007805 € ; score 85.07/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.04 | +88.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35761 | +49.63 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GLMR-EUR | 0.008466 | +22.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TRAC-EUR | 0.4 | +20.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.33357 | +19.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.028214 | +18.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.43978 | +16.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0609696 | +14.37 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOM-EUR | 0.0021036 | +12.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOMI-EUR | 0.19749 | +11.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1875 scans ; 802328 observations ; 1429 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
