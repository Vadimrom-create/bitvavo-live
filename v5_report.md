# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T23:17:55.004381+00:00
État : OK | marchés EUR : 426 | V4 : 383 | données valides : 426
Récupération : 2026-09-20T23:17:22.213412+00:00 | âge ticker : 154.0 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25333 € | IGNITION | score 89.94/100 | entrée 7.15/10
  Entrée 0.25321 € ; stop 0.24317 € ; TP1 0.27329 € ; TP2 0.28332 € ; montant 250.00 € ; risque théorique 11.63 € ; R/R net 1.55.
  Chase risk : 4.542/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PROVE-EUR : 0.19828 € ; score 92.17/100 ; SURVEILLE ; seuil achat non atteint
- PUNDIX-EUR : 0.09921 € ; score 88.43/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK
- CATI-EUR : 0.057375 € ; score 87.74/100 ; SURVEILLE ; seuil achat non atteint
- TRUMP-EUR : 1.8067 € ; score 85.36/100 ; SURVEILLE ; seuil achat non atteint
- JTO-EUR : 0.43175 € ; score 85.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032223 | +48.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008166 | +33.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.2397 | +29.90 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.054347 | +21.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49192 | +20.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028734 | +19.57 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.049334 | +17.92 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.033927 | +16.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6091 | +15.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.8566 | +15.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1027 scans ; 440239 observations ; 278 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
