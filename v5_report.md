# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T10:23:12.955842+00:00
État : OK | marchés EUR : 427 | V4 : 392 | données valides : 427
Récupération : 2026-09-28T10:22:38.303145+00:00 | âge ticker : 146.8 s | durée : 148.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- GRAM-EUR : 1.4881 € | IGNITION | score 84.53/100 | entrée 7.25/10
  Entrée 1.4941 € ; stop 1.4013 € ; TP1 1.6797 € ; TP2 1.7725 € ; montant 174.18 € ; risque théorique 12.00 € ; R/R net 1.70.
  Chase risk : 5.507/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- CC-EUR : 0.11562 € | IGNITION | score 75.01/100 | entrée 5.85/10
  Entrée 0.11559 € ; stop 0.1115 € ; TP1 0.12376 € ; TP2 0.12785 € ; montant 250.00 € ; risque théorique 10.56 € ; R/R net 1.50.
  Chase risk : 0/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XDC-EUR : 0.030284 € ; score 84.90/100 ; SURVEILLE ; seuil achat non atteint
- IMX-EUR : 0.1577 € ; score 81.23/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.071549 € ; score 80.83/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- SKY-EUR : 0.070601 € ; score 79.68/100 ; SURVEILLE ; WICK_SETUP
- ALGO-EUR : 0.112151 € ; score 79.60/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 199.135 | +31.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.099195 | +18.94 % | DETECTED_EARLY | NONE | NONE |
| AUDIO-EUR | 0.014717 | +13.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.027946 | +13.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.030284 | +9.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.112151 | +8.16 % | DETECTED_EARLY | NONE | NONE |
| IMX-EUR | 0.1577 | +7.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.047562 | +6.41 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AZTEC-EUR | 0.015792 | +6.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0041788 | +6.10 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1688 scans ; 722144 observations ; 1242 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
