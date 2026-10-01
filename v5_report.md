# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T18:47:36.034045+00:00
État : OK | marchés EUR : 430 | V4 : 383 | données valides : 430
Récupération : 2026-10-01T18:47:04.172202+00:00 | âge ticker : 153.0 s | durée : 153.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.21337 € | IGNITION | score 86.62/100 | entrée 6.60/10
  Entrée 0.21344 € ; stop 0.20366 € ; TP1 0.23299 € ; TP2 0.24277 € ; montant 227.87 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.86/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PUMP-EUR : 0.0051507 € | IGNITION | score 83.76/100 | entrée 7.00/10
  Entrée 0.0051532 € ; stop 0.004915 € ; TP1 0.0056296 € ; TP2 0.0058678 € ; montant 226.15 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 5.532/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AZTEC-EUR : 0.015793 € ; score 87.89/100 ; SURVEILLE ; seuil achat non atteint
- STX-EUR : 0.34467 € ; score 87.85/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SPK-EUR : 0.021477 € ; score 87.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GALA-EUR : 0.0020593 € ; score 86.75/100 ; SURVEILLE ; seuil achat non atteint
- W-EUR : 0.012143 € ; score 86.08/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00063353 | +145.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.7843 | +81.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0775419 | +33.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04868 | +32.72 % | DETECTED_EARLY | NONE | NONE |
| ALICE-EUR | 0.18236 | +28.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43513 | +25.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SYN-EUR | 0.17812 | +23.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.031064 | +23.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.098963 | +20.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.009449 | +17.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1925 scans ; 823828 observations ; 1489 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
