# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T17:27:08.977620+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T17:26:38.419692+00:00 | âge ticker : 148.4 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : 0.24525 € | IGNITION | score 86.00/100 | entrée 7.50/10
  Entrée 0.24479 € ; stop 0.23423 € ; TP1 0.26591 € ; TP2 0.27647 € ; montant 240.06 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.856/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- GRAM-EUR : 1.4709 € | IGNITION | score 82.67/100 | entrée 7.20/10
  Entrée 1.4746 € ; stop 1.3983 € ; TP1 1.6271 € ; TP2 1.7034 € ; montant 204.91 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.582/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- DRIFT-EUR : 0.017545 € ; score 92.00/100 ; SURVEILLE ; seuil achat non atteint
- ACU-EUR : 0.12063 € ; score 91.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BEL-EUR : 0.116609 € ; score 89.39/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- DOT-EUR : 1.0977 € ; score 86.62/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- BIGTIME-EUR : 0.008433 € ; score 86.57/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 163.854 | +51.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.28012 | +46.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.01651 | +39.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016364 | +28.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GRASS-EUR | 0.5652 | +24.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.25134 | +24.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.006389 | +22.09 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013662 | +19.38 % | DETECTED_EARLY | NONE | NONE |
| GLMR-EUR | 0.007161 | +17.45 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AGI-EUR | 0.0069 | +15.81 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1633 scans ; 698659 observations ; 1161 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
