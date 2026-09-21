# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T01:02:59.123557+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 426
Récupération : 2026-09-21T01:02:32.181136+00:00 | âge ticker : 143.0 s | durée : 143.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- APT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ETHFI-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SYRUP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.054186 € ; score 93.18/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ZIL-EUR : 0.0030791 € ; score 90.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ETHFI-EUR : 0.64515 € ; score 90.85/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ENS-EUR : 5.8099 € ; score 90.32/100 ; SURVEILLE ; seuil achat non atteint
- MOODENG-EUR : 0.039366 € ; score 87.83/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.031865 | +41.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.000819 | +32.42 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23975 | +29.93 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.055748 | +26.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.4931 | +25.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.0349 | +21.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CFG-EUR | 0.130911 | +20.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7067 | +19.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028755 | +19.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.047602 | +14.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1035 scans ; 443647 observations ; 285 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
