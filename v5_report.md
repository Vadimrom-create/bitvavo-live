# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T23:24:21.369505+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-20T23:23:46.010754+00:00 | âge ticker : 158.1 s | durée : 158.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : 0.021199 € | IGNITION | score 85.40/100 | entrée 7.40/10
  Entrée 0.021199 € ; stop 0.0204262 € ; TP1 0.0227446 € ; TP2 0.0235174 € ; montant 250.00 € ; risque théorique 10.83 € ; R/R net 1.52.
  Chase risk : 1.48/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- JUP-EUR : 0.25199 € | IGNITION | score 83.14/100 | entrée 7.30/10
  Entrée 0.25349 € ; stop 0.24317 € ; TP1 0.27413 € ; TP2 0.28445 € ; montant 250.00 € ; risque théorique 11.89 € ; R/R net 1.56.
  Chase risk : 4.542/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- POL-EUR : 0.094315 € ; score 88.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.17259 € ; score 86.62/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- COW-EUR : 0.13725 € ; score 85.71/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.2508 € ; score 83.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- REZ-EUR : 0.0033091 € ; score 82.54/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.0327 | +50.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008295 | +35.81 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23993 | +30.03 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.054634 | +23.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.05053 | +20.78 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49222 | +20.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028862 | +20.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.034012 | +17.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6036 | +15.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.8989 | +15.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1028 scans ; 440665 observations ; 278 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
