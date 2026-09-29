# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T09:02:13.629763+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T09:01:42.045987+00:00 | âge ticker : 156.5 s | durée : 157.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.031376 € | IGNITION | score 87.80/100 | entrée 6.90/10
  Entrée 0.031387 € ; stop 0.03026 € ; TP1 0.033641 € ; TP2 0.034767 € ; montant 250.00 € ; risque théorique 10.70 € ; R/R net 1.51.
  Chase risk : 4.334/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SYRUP-EUR : 0.20743 € | IGNITION | score 78.88/100 | entrée 7.65/10
  Entrée 0.2072 € ; stop 0.19974 € ; TP1 0.22211 € ; TP2 0.22957 € ; montant 250.00 € ; risque théorique 10.72 € ; R/R net 1.51.
  Chase risk : 4.305/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- TIA-EUR : 0.39908 € ; score 87.20/100 ; SURVEILLE ; WICK_SETUP
- KAIA-EUR : 0.030247 € ; score 87.04/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- NEO-EUR : 2.2414 € ; score 86.71/100 ; SURVEILLE ; seuil achat non atteint
- ARB-EUR : 0.18052 € ; score 86.37/100 ; SURVEILLE ; WICK_SETUP
- BONK-EUR : 3.1788e-06 € ; score 85.96/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017763 | +40.70 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 11.0955 | +28.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35118 | +22.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.095128 | +19.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.31652 | +19.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.087246 | +17.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.26406 | +16.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICP-EUR | 2.9668 | +14.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CVX-EUR | 2.0055 | +13.96 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SYRUP-EUR | 0.20743 | +13.47 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1758 scans ; 752097 observations ; 1287 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
