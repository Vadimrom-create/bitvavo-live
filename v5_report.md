# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T22:30:27.750379+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T22:29:56.469079+00:00 | âge ticker : 154.4 s | durée : 156.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AIOZ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.24988 € | IGNITION | score 90.44/100 | entrée 7.65/10
  Entrée 0.2501 € ; stop 0.24103 € ; TP1 0.26824 € ; TP2 0.2773 € ; montant 250.00 € ; risque théorique 10.78 € ; R/R net 1.51.
  Chase risk : 3.215/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.034701 € ; score 90.40/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.37671 € ; score 89.29/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SSV-EUR : 2.6997 € ; score 87.54/100 ; SURVEILLE ; seuil achat non atteint
- ENS-EUR : 5.6845 € ; score 87.04/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.006659 € ; score 86.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.03078 | +39.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24853 | +34.69 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0008073 | +31.95 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.055285 | +25.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.035125 | +21.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49301 | +19.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028666 | +19.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6948 | +19.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.127231 | +18.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AVAX-EUR | 9.8596 | +17.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1023 scans ; 438535 observations ; 275 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
