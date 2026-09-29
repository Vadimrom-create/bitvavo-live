# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T08:45:32.098603+00:00
État : OK | marchés EUR : 428 | V4 : 394 | données valides : 428
Récupération : 2026-09-29T08:45:03.375767+00:00 | âge ticker : 149.2 s | durée : 150.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- VIRTUAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.9659 € | IGNITION | score 82.28/100 | entrée 7.15/10
  Entrée 9.9664 € ; stop 9.4931 € ; TP1 10.913 € ; TP2 11.3863 € ; montant 220.90 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 6.423/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- UNI-EUR : 7.9471 € | IGNITION | score 82.13/100 | entrée 7.40/10
  Entrée 7.9445 € ; stop 7.6232 € ; TP1 8.5871 € ; TP2 8.9084 € ; montant 250.00 € ; risque théorique 11.83 € ; R/R net 1.56.
  Chase risk : 4.732/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PLUME-EUR : 0.01594 € ; score 90.39/100 ; SURVEILLE ; seuil achat non atteint
- NEAR-EUR : 4.1866 € ; score 90.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.11162 € ; score 89.52/100 ; SURVEILLE ; seuil achat non atteint
- LDO-EUR : 0.40228 € ; score 89.30/100 ; SURVEILLE ; WICK_SETUP
- FIL-EUR : 0.9367 € ; score 88.57/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017244 | +40.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 11.3222 | +32.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35072 | +21.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.3211 | +20.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.093428 | +17.78 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CVX-EUR | 2.0197 | +15.08 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.60982 | +15.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.086251 | +14.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.25766 | +14.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYRUP-EUR | 0.20679 | +13.43 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1757 scans ; 751669 observations ; 1287 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
