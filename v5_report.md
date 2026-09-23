# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T13:51:11.675902+00:00
État : OK | marchés EUR : 426 | V4 : 405 | données valides : 426
Récupération : 2026-09-23T13:50:38.855971+00:00 | âge ticker : 152.2 s | durée : 154.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- USELESS-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- KITE-EUR : 0.11948 € ; score 91.48/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NEIRO-EUR : 8.4955e-05 € ; score 90.16/100 ; SURVEILLE ; STABILITY_HOLD
- PROMPT-EUR : 0.019541 € ; score 87.71/100 ; SURVEILLE ; seuil achat non atteint
- VELO-EUR : 0.0041009 € ; score 84.94/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- AXS-EUR : 0.9875 € ; score 84.62/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.034139 | +42.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALLO-EUR | 0.308456 | +35.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MET-EUR | 0.33382 | +31.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.042709 | +26.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SENT-EUR | 0.02083 | +23.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.1596 | +19.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017089 | +18.59 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ZRO-EUR | 1.2875 | +18.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ACE-EUR | 0.17365 | +15.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CHR-EUR | 0.018126 | +14.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1273 scans ; 545035 observations ; 650 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
