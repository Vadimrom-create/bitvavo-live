# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T03:23:31.455269+00:00
État : OK | marchés EUR : 426 | V4 : 373 | données valides : 426
Récupération : 2026-09-21T03:22:57.544298+00:00 | âge ticker : 154.4 s | durée : 155.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAO-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.15894 € | IGNITION | score 80.31/100 | entrée 7.25/10
  Entrée 0.15871 € ; stop 0.14987 € ; TP1 0.17638 € ; TP2 0.18522 € ; montant 191.99 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 3.094/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MET-EUR : 0.22293 € ; score 87.78/100 ; SURVEILLE ; LOW_LIQUIDITY
- AXL-EUR : 0.042772 € ; score 87.21/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- ANIME-EUR : 0.002797 € ; score 83.90/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.20637 € ; score 83.57/100 ; SURVEILLE ; seuil achat non atteint
- MERL-EUR : 0.022965 € ; score 82.80/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0011642 | +89.15 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.25628 | +40.44 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.031489 | +40.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.055191 | +26.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.4427 | +23.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NEAR-EUR | 3.7909 | +22.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.02994 | +21.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49573 | +20.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46551 | +19.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.03363 | +16.93 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1043 scans ; 447055 observations ; 298 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
