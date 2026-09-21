# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T00:00:26.028393+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T23:59:50.195359+00:00 | âge ticker : 160.8 s | durée : 161.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.29109 € | IGNITION | score 90.10/100 | entrée 6.90/10
  Entrée 0.29223 € ; stop 0.28148 € ; TP1 0.31372 € ; TP2 0.32447 € ; montant 250.00 € ; risque théorique 10.91 € ; R/R net 1.52.
  Chase risk : 4.574/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- POL-EUR : 0.094603 € ; score 87.29/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PROVE-EUR : 0.19965 € ; score 86.96/100 ; SURVEILLE ; SPREAD_RISK
- WCT-EUR : 0.034904 € ; score 86.16/100 ; SURVEILLE ; seuil achat non atteint
- COW-EUR : 0.13828 € ; score 85.97/100 ; SURVEILLE ; seuil achat non atteint
- KITE-EUR : 0.1011 € ; score 84.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032899 | +50.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.25532 | +38.37 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PTB-EUR | 0.0008223 | +32.95 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| EPIC-EUR | 0.49632 | +23.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.053154 | +21.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.03478 | +19.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.02832 | +17.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CFG-EUR | 0.126574 | +16.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.6234 | +16.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LUNA2-EUR | 0.048 | +14.73 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 1032 scans ; 442369 observations ; 280 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
