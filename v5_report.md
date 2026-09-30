# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T08:58:42.608588+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T08:58:14.729297+00:00 | âge ticker : 144.4 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : 4.501 € | IGNITION | score 89.61/100 | entrée 7.85/10
  Entrée 4.5017 € ; stop 4.2252 € ; TP1 5.0546 € ; TP2 5.3311 € ; montant 175.94 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 3.118/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ICP-EUR : 3.0602 € ; score 94.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BONK-EUR : 3.4182e-06 € ; score 92.14/100 ; SURVEILLE ; WICK_SETUP
- ENA-EUR : 0.22664 € ; score 91.99/100 ; SURVEILLE ; WICK_SETUP
- WOO-EUR : 0.012255 € ; score 91.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DOT-EUR : 1.0842 € ; score 91.31/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.7067 | +96.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.10331 | +35.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008613 | +27.69 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.39921 | +24.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.071636 | +24.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.26 | +19.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.29998 | +15.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022472 | +14.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0050932 | +14.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00048516 | +14.54 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1829 scans ; 782551 observations ; 1364 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
