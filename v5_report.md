# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T02:23:58.505647+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T02:23:23.226605+00:00 | âge ticker : 156.8 s | durée : 157.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.34105 € | IGNITION | score 78.81/100 | entrée 5.70/10
  Entrée 0.34351 € ; stop 0.32841 € ; TP1 0.37371 € ; TP2 0.38881 € ; montant 236.20 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 1.842/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PLUME-EUR : 0.0158073 € ; score 91.64/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.2166 € ; score 88.15/100 ; SURVEILLE ; seuil achat non atteint
- CHIP-EUR : 0.039502 € ; score 87.10/100 ; SURVEILLE ; seuil achat non atteint
- BRETT-EUR : 0.0050709 € ; score 84.60/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ZIG-EUR : 0.046006 € ; score 84.39/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 253.051 | +39.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.35255 | +35.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.0729 | +30.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016017 | +30.01 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| GRASS-EUR | 0.65465 | +29.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0051986 | +24.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00049914 | +23.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.090529 | +18.86 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.5359 | +17.02 % | DETECTED_EARLY | NONE | NONE |
| ZBCN-EUR | 0.0022887 | +16.44 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1810 scans ; 774400 observations ; 1353 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
