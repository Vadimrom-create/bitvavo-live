# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T08:38:20.506496+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T08:37:52.946701+00:00 | âge ticker : 144.4 s | durée : 145.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.23116 € | IGNITION | score 87.38/100 | entrée 7.25/10
  Entrée 0.23142 € ; stop 0.22266 € ; TP1 0.24893 € ; TP2 0.25769 € ; montant 250.00 € ; risque théorique 11.18 € ; R/R net 1.53.
  Chase risk : 3.807/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ALGO-EUR : 0.117092 € | IGNITION | score 82.20/100 | entrée 6.80/10
  Entrée 0.117401 € ; stop 0.111635 € ; TP1 0.128933 € ; TP2 0.134699 € ; montant 214.51 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 5.121/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAIA-EUR : 0.032819 € ; score 91.14/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7732 € ; score 87.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MOODENG-EUR : 0.04272 € ; score 86.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- DOGE-EUR : 0.086673 € ; score 86.81/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.29514 € ; score 86.60/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00073139 | +182.54 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.54465 | +48.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAND-EUR | 0.0564 | +45.25 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.11401 | +28.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.026432 | +16.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.091562 | +16.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.20298 | +14.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0022724 | +12.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.6352 | +11.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| USELESS-EUR | 0.22453 | +11.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1967 scans ; 841888 observations ; 1548 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
