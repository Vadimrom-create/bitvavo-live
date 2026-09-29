# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T04:55:36.444961+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T04:55:05.663210+00:00 | âge ticker : 144.4 s | durée : 145.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.8587 € | IGNITION | score 86.56/100 | entrée 7.45/10
  Entrée 2.86 € ; stop 2.6985 € ; TP1 3.1829 € ; TP2 3.3444 € ; montant 189.66 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 3.517/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- W-EUR : 0.012352 € ; score 85.98/100 ; SURVEILLE ; seuil achat non atteint
- ARB-EUR : 0.17385 € ; score 85.12/100 ; SURVEILLE ; WICK_SETUP
- RSR-EUR : 0.0014345 € ; score 85.08/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0018877 € ; score 84.46/100 ; SURVEILLE ; WICK_SETUP
- DOGE-EUR : 0.081903 € ; score 83.96/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.782 | +33.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.106061 | +26.70 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.26658 | +18.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.121968 | +17.96 % | DETECTED_EARLY | NONE | NONE |
| CRV-EUR | 0.34334 | +16.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CELO-EUR | 0.090646 | +11.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.601 | +9.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.0488 | +8.87 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0017901 | +7.08 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| XLM-EUR | 0.19851 | +6.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1746 scans ; 746961 observations ; 1283 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
