# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T00:31:05.829630+00:00
État : OK | marchés EUR : 428 | V4 : 398 | données valides : 428
Récupération : 2026-09-29T00:30:34.674241+00:00 | âge ticker : 154.6 s | durée : 155.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- BCH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.20376 € | IGNITION | score 94.34/100 | entrée 8.00/10
  Entrée 0.20372 € ; stop 0.19586 € ; TP1 0.21944 € ; TP2 0.2273 € ; montant 250.00 € ; risque théorique 11.36 € ; R/R net 1.54.
  Chase risk : 2.444/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XDC-EUR : 0.030458 € ; score 91.22/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2011 € ; score 89.51/100 ; SURVEILLE ; seuil achat non atteint
- ICP-EUR : 2.7635 € ; score 87.86/100 ; SURVEILLE ; seuil achat non atteint
- NPC-EUR : 0.020849 € ; score 87.10/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.43332 € ; score 86.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.0097 | +30.65 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.10656 | +25.88 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.26125 | +13.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.119937 | +13.31 % | DETECTED_EARLY | NONE | NONE |
| LINK-EUR | 13.747 | +10.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018365 | +10.27 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NPC-EUR | 0.020849 | +8.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.32916 | +8.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.016674 | +6.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.00506 | +6.70 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1732 scans ; 740969 observations ; 1271 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
