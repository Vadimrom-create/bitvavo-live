# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T19:31:36.097445+00:00
État : OK | marchés EUR : 426 | V4 : 385 | données valides : 426
Récupération : 2026-09-20T19:31:01.371438+00:00 | âge ticker : 152.1 s | durée : 153.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : 0.080097 € | IGNITION | score 81.29/100 | entrée 5.55/10
  Entrée 0.079948 € ; stop 0.076936 € ; TP1 0.085972 € ; TP2 0.088984 € ; montant 250.00 € ; risque théorique 11.14 € ; R/R net 1.53.
  Chase risk : 4.23/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RUNE-EUR : 0.48842 € ; score 91.54/100 ; SURVEILLE ; WICK_SETUP
- ATOM-EUR : 1.5313 € ; score 88.19/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MEGA-EUR : 0.03647 € ; score 85.26/100 ; SURVEILLE ; seuil achat non atteint
- T-EUR : 0.0044342 € ; score 85.10/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD
- COW-EUR : 0.13578 € ; score 83.39/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.033067 | +51.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0030298 | +26.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0007746 | +25.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SKL-EUR | 0.0043017 | +22.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.03332 | +18.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.21661 | +17.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.04295 | +16.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.050353 | +14.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.027565 | +14.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.5176 | +14.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1010 scans ; 432997 observations ; 246 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
