# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T23:47:15.753258+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T23:46:43.373155+00:00 | âge ticker : 147.6 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0051769 € | IGNITION | score 79.71/100 | entrée 6.70/10
  Entrée 0.0051758 € ; stop 0.0049825 € ; TP1 0.0055624 € ; TP2 0.0057557 € ; montant 250.00 € ; risque théorique 11.05 € ; R/R net 1.53.
  Chase risk : 0.575/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WLD-EUR : 0.44827 € ; score 93.42/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- REZ-EUR : 0.0039625 € ; score 87.74/100 ; SURVEILLE ; seuil achat non atteint
- ONDO-EUR : 0.44031 € ; score 87.07/100 ; SURVEILLE ; WICK_SETUP
- PIXEL-EUR : 0.0052178 € ; score 86.50/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK
- ZK-EUR : 0.010771 € ; score 86.25/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000615 | +138.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.123634 | +48.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.6142 | +36.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.18654 | +25.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.44513 | +25.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04485 | +21.41 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0024469 | +18.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.164329 | +16.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20454 | +15.75 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.49552 | +14.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1941 scans ; 830708 observations ; 1509 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
