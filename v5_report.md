# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T23:32:03.166236+00:00
État : OK | marchés EUR : 426 | V4 : 384 | données valides : 426
Récupération : 2026-09-20T23:31:29.301115+00:00 | âge ticker : 154.7 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : 0.0212862 € | IGNITION | score 90.88/100 | entrée 7.40/10
  Entrée 0.0212542 € ; stop 0.0204442 € ; TP1 0.0228742 € ; TP2 0.0236842 € ; montant 250.00 € ; risque théorique 11.24 € ; R/R net 1.53.
  Chase risk : 2.419/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- JUP-EUR : 0.2555 € | IGNITION | score 80.12/100 | entrée 6.90/10
  Entrée 0.2562 € ; stop 0.24568 € ; TP1 0.27723 € ; TP2 0.28775 € ; montant 250.00 € ; risque théorique 11.98 € ; R/R net 1.56.
  Chase risk : 4.789/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- COW-EUR : 0.13725 € ; score 93.97/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.015802 € ; score 92.01/100 ; SURVEILLE ; LOW_LIQUIDITY
- JTO-EUR : 0.43286 € ; score 89.84/100 ; SURVEILLE ; WICK_SETUP
- A-EUR : 0.078033 € ; score 88.55/100 ; SURVEILLE ; LOW_LIQUIDITY
- BCH-EUR : 221.87 € ; score 87.52/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032325 | +48.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008311 | +36.07 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23744 | +28.68 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.055025 | +24.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49247 | +20.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028793 | +19.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.049979 | +19.46 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| S-EUR | 0.034174 | +17.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CFG-EUR | 0.126204 | +16.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.5988 | +15.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1029 scans ; 441091 observations ; 278 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
