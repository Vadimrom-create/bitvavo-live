# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T04:17:54.567301+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T04:17:22.001642+00:00 | âge ticker : 146.9 s | durée : 147.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : 0.119612 € | IGNITION | score 82.02/100 | entrée 7.30/10
  Entrée 0.119692 € ; stop 0.115074 € ; TP1 0.128928 € ; TP2 0.133546 € ; montant 250.00 € ; risque théorique 11.36 € ; R/R net 1.54.
  Chase risk : 5.96/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- 2Z-EUR : 0.0587 € ; score 89.98/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- GRAM-EUR : 1.3706 € ; score 89.21/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.101007 € ; score 88.98/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 130.4 € ; score 88.41/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : 0.22028 € ; score 87.36/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.1089 | +37.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.104777 | +24.10 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.119612 | +16.92 % | DETECTED_EARLY | NONE | NONE |
| CRV-EUR | 0.33808 | +15.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.25752 | +14.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.59022 | +10.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XLM-EUR | 0.20038 | +8.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.088593 | +7.88 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| CAP-EUR | 0.048774 | +7.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 2.8744 | +7.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1744 scans ; 746105 observations ; 1280 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
