# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T05:52:38.183702+00:00
État : OK | marchés EUR : 428 | V4 : 392 | données valides : 428
Récupération : 2026-09-29T05:52:10.079233+00:00 | âge ticker : 141.1 s | durée : 141.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.8905 € | IGNITION | score 78.80/100 | entrée 6.40/10
  Entrée 2.8949 € ; stop 2.7718 € ; TP1 3.1411 € ; TP2 3.2641 € ; montant 243.04 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 5.412/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.040447 € ; score 89.57/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.3672 € ; score 86.61/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BCH-EUR : 269.51 € ; score 86.33/100 ; SURVEILLE ; seuil achat non atteint
- BAT-EUR : 0.07882 € ; score 84.87/100 ; SURVEILLE ; seuil achat non atteint
- SHIB-EUR : 4.9262e-06 € ; score 84.38/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.1114 | +36.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.104638 | +23.32 % | DETECTED_EARLY | NONE | NONE |
| CRV-EUR | 0.34709 | +19.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.26779 | +17.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.118831 | +16.04 % | DETECTED_EARLY | NONE | NONE |
| POND-EUR | 0.0015163 | +14.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.090462 | +11.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.23912 | +9.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.048625 | +8.99 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CVX-EUR | 1.9711 | +8.46 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1749 scans ; 748245 observations ; 1283 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
