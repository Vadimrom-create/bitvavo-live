# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T12:00:04.451386+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-24T11:59:33.923122+00:00 | âge ticker : 154.5 s | durée : 155.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 8.3648 € | IGNITION | score 81.93/100 | entrée 7.20/10
  Entrée 8.3763 € ; stop 8.0528 € ; TP1 9.0233 € ; TP2 9.3468 € ; montant 250.00 € ; risque théorique 11.37 € ; R/R net 1.54.
  Chase risk : 1.661/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- JUP-EUR : 0.25505 € ; score 91.52/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MOVR-EUR : 0.7728 € ; score 84.63/100 ; SURVEILLE ; seuil achat non atteint
- LAPTOP-EUR : 0.06072 € ; score 83.78/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 58.32 € ; score 82.89/100 ; SURVEILLE ; seuil achat non atteint
- DODO-EUR : 0.016052 € ; score 82.22/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021618 | +39.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.112256 | +32.08 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.34648 | +25.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARX-EUR | 0.21819 | +16.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0020166 | +15.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVC-EUR | 0.027952 | +11.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.3882 | +9.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28577 | +8.68 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.04463 | +7.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARK-EUR | 0.15334 | +7.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1353 scans ; 579115 observations ; 715 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
