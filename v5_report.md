# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T18:44:29.132682+00:00
État : OK | marchés EUR : 426 | V4 : 379 | données valides : 426
Récupération : 2026-10-03T18:43:50.691036+00:00 | âge ticker : 157.0 s | durée : 158.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.52824 € ; score 82.88/100 ; SURVEILLE ; seuil achat non atteint
- MANA-EUR : 0.094 € ; score 82.49/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 159.53 € ; score 81.76/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- INIT-EUR : 0.0996 € ; score 80.71/100 ; SURVEILLE ; seuil achat non atteint
- FLUID-EUR : 1.4833 € ; score 79.54/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GLMR-EUR | 0.012385 | +64.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.99199 | +32.62 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FUN-EUR | 0.019859 | +28.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| STRK-EUR | 0.045942 | +23.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HFT-EUR | 0.00673 | +20.39 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PUMP-EUR | 0.0056633 | +20.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAND-EUR | 0.065039 | +18.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZAMA-EUR | 0.078155 | +17.78 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SUPER-EUR | 0.23171 | +16.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.8313 | +16.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 2049 scans ; 876860 observations ; 1624 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
