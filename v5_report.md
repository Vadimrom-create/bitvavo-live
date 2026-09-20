# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T19:52:47.918786+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 426
Récupération : 2026-09-20T19:52:12.711372+00:00 | âge ticker : 155.3 s | durée : 156.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AIOZ-EUR : 0.0806 € | IGNITION | score 83.53/100 | entrée 6.30/10
  Entrée 0.079949 € ; stop 0.076911 € ; TP1 0.086025 € ; TP2 0.089063 € ; montant 250.00 € ; risque théorique 11.22 € ; R/R net 1.53.
  Chase risk : 4.835/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COW-EUR : 0.13527 € ; score 93.31/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.1992 € ; score 88.15/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MEGA-EUR : 0.03687 € ; score 86.85/100 ; SURVEILLE ; seuil achat non atteint
- PUMP-EUR : 0.0036892 € ; score 86.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- T-EUR : 0.0044501 € ; score 85.97/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.03304 | +51.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.26405 | +43.65 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0007934 | +27.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.034799 | +23.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELR-EUR | 0.0032016 | +23.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6243 | +17.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AVAX-EUR | 9.7664 | +15.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.051375 | +15.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STRK-EUR | 0.042632 | +15.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.027561 | +14.84 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1012 scans ; 433849 observations ; 249 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
