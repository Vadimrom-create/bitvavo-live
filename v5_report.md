# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T04:20:28.311977+00:00
État : OK | marchés EUR : 426 | V4 : 373 | données valides : 426
Récupération : 2026-09-21T04:19:57.459298+00:00 | âge ticker : 150.0 s | durée : 150.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0037894 € | IGNITION | score 64.25/100 | entrée 5.60/10
  Entrée 0.0037994 € ; stop 0.0036633 € ; TP1 0.0040716 € ; TP2 0.0042077 € ; montant 250.00 € ; risque théorique 10.67 € ; R/R net 1.51.
  Chase risk : 2.683/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WAL-EUR : 0.028516 € ; score 93.74/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.034715 € ; score 93.67/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : 0.017157 € ; score 91.08/100 ; SURVEILLE ; seuil achat non atteint
- MORPHO-EUR : 2.43703 € ; score 89.27/100 ; SURVEILLE ; WICK_SETUP
- MERL-EUR : 0.023156 € ; score 85.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0011956 | +96.61 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZETA-EUR | 0.059017 | +75.24 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| FTT-EUR | 0.25929 | +42.09 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.030356 | +28.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.8333 | +26.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.054276 | +22.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VVV-EUR | 28.0586 | +21.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46577 | +19.05 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49659 | +17.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| S-EUR | 0.033677 | +17.86 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1046 scans ; 448333 observations ; 301 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
