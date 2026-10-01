# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T15:39:05.945610+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-01T15:38:29.365513+00:00 | âge ticker : 157.7 s | durée : 158.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- AAVE-EUR : 148.8 € | IGNITION | score 82.64/100 | entrée 6.95/10
  Entrée 148.86 € ; stop 143.01 € ; TP1 160.56 € ; TP2 166.41 € ; montant 250.00 € ; risque théorique 11.54 € ; R/R net 1.55.
  Chase risk : 2.056/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PROM-EUR : 5.8608 € ; score 93.44/100 ; SURVEILLE ; WICK_SETUP
- ZRO-EUR : 1.5171 € ; score 90.90/100 ; SURVEILLE ; seuil achat non atteint
- KAIA-EUR : 0.033112 € ; score 82.79/100 ; SURVEILLE ; seuil achat non atteint
- RE-EUR : 0.45571 € ; score 81.28/100 ; SURVEILLE ; seuil achat non atteint
- XDP-EUR : 0.017999 € ; score 79.92/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000537 | +105.43 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.4382 | +57.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.189 | +31.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0749112 | +31.38 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.414 | +24.92 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| MON-EUR | 0.028829 | +19.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.47484 | +18.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04461 | +18.61 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.173602 | +17.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.34281 | +14.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1916 scans ; 819958 observations ; 1482 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
