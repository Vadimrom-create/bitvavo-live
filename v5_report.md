# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T10:01:43.364995+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-30T10:00:48.565648+00:00 | âge ticker : 180.3 s | durée : 181.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- PEPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.35984 € | IGNITION | score 92.32/100 | entrée 6.90/10
  Entrée 0.35863 € ; stop 0.3424 € ; TP1 0.39109 € ; TP2 0.40732 € ; montant 230.34 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 5.204/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DOT-EUR : 1.0951 € | IGNITION | score 80.52/100 | entrée 7.00/10
  Entrée 1.0953 € ; stop 1.0502 € ; TP1 1.1854 € ; TP2 1.2305 € ; montant 249.83 € ; risque théorique 12.00 € ; R/R net 1.56.
  Chase risk : 3.782/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SYRUP-EUR : 0.20594 € ; score 92.78/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- PARTI-EUR : 0.02343 € ; score 90.33/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- KMNO-EUR : 0.038138 € ; score 90.30/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MANA-EUR : 0.080273 € ; score 90.09/100 ; SURVEILLE ; WICK_SETUP
- PROM-EUR : 5.5743 € ; score 89.82/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.5909 | +79.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.101289 | +31.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.39549 | +29.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GLMR-EUR | 0.00865 | +29.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PHA-EUR | 0.071 | +22.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.258 | +19.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TRAC-EUR | 0.38399 | +15.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GWEI-EUR | 0.021006 | +15.04 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0050588 | +14.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GNS-EUR | 0.48179 | +14.23 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1832 scans ; 783838 observations ; 1367 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
