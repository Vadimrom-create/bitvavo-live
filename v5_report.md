# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T02:43:17.040082+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-28T02:42:43.143985+00:00 | âge ticker : 151.8 s | durée : 152.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GRAM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.50305 € | IGNITION | score 77.27/100 | entrée 7.55/10
  Entrée 0.50259 € ; stop 0.48363 € ; TP1 0.5405 € ; TP2 0.55946 € ; montant 250.00 € ; risque théorique 11.15 € ; R/R net 1.53.
  Chase risk : 2.312/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RAY-EUR : 1.84205 € ; score 89.01/100 ; SURVEILLE ; STABILITY_HOLD
- AVNT-EUR : 0.11801 € ; score 88.61/100 ; SURVEILLE ; WICK_SETUP
- GRAM-EUR : 1.4491 € ; score 87.08/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RSR-EUR : 0.0015188 € ; score 86.35/100 ; SURVEILLE ; seuil achat non atteint
- SKL-EUR : 0.0040387 € ; score 84.30/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 237.687 | +61.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.1234 | +34.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRT-EUR | 0.029997 | +25.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006419 | +22.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IRYS-EUR | 0.017436 | +19.29 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SEI-EUR | 0.07549 | +18.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0045524 | +17.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.58067 | +15.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMX-EUR | 0.16656 | +12.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| JASMY-EUR | 0.0046432 | +11.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1666 scans ; 712750 observations ; 1216 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
