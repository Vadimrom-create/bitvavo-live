# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T09:58:43.997586+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T09:58:13.675946+00:00 | âge ticker : 145.7 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- NPC-EUR : 0.020997 € | IGNITION | score 84.45/100 | entrée 7.05/10
  Entrée 0.0210065 € ; stop 0.0199948 € ; TP1 0.0230299 € ; TP2 0.0240416 € ; montant 218.21 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 6.084/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NEAR-EUR : 3.9225 € | IGNITION | score 76.71/100 | entrée 7.35/10
  Entrée 3.917 € ; stop 3.7587 € ; TP1 4.2335 € ; TP2 4.3918 € ; montant 250.00 € ; risque théorique 11.82 € ; R/R net 1.56.
  Chase risk : 3.93/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PROVE-EUR : 0.20284 € ; score 91.69/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- ACH-EUR : 0.0051565 € ; score 88.19/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- XVG-EUR : 0.0026384 € ; score 86.35/100 ; SURVEILLE ; SPREAD_RISK
- TRUMP-EUR : 1.8912 € ; score 84.84/100 ; SURVEILLE ; seuil achat non atteint
- TAI-EUR : 0.003627 € ; score 84.56/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017788 | +103.83 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.00156 | +98.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.119119 | +42.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.057559 | +37.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WIF-EUR | 0.22283 | +22.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.39072 | +21.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CARV-EUR | 0.041373 | +20.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEPE-EUR | 4.3451e-06 | +20.19 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.46142 | +19.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.039766 | +17.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1173 scans ; 502435 observations ; 474 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
