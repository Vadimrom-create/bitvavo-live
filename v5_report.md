# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T22:14:37.699462+00:00
État : OK | marchés EUR : 426 | V4 : 381 | données valides : 426
Récupération : 2026-09-20T22:13:36.779735+00:00 | âge ticker : 177.4 s | durée : 178.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- IOST-EUR : 0.0007631 € ; score 91.68/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- WAL-EUR : 0.027997 € ; score 89.23/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MIRA-EUR : 0.04498 € ; score 88.89/100 ; SURVEILLE ; seuil achat non atteint
- TIA-EUR : 0.36835 € ; score 88.32/100 ; SURVEILLE ; seuil achat non atteint
- SSV-EUR : 2.7008 € ; score 87.72/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.03101 | +40.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008064 | +31.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23664 | +28.25 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.03635 | +26.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.054315 | +23.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.7112 | +20.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.49896 | +19.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028531 | +18.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.8752 | +18.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.04863 | +17.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1021 scans ; 437683 observations ; 275 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
