# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T05:00:43.889763+00:00
État : OK | marchés EUR : 427 | V4 : 394 | données valides : 427
Récupération : 2026-09-28T05:00:11.126467+00:00 | âge ticker : 149.2 s | durée : 150.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ONDO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ALGO-EUR : 0.104213 € | IGNITION | score 89.56/100 | entrée 6.80/10
  Entrée 0.104281 € ; stop 0.10057 € ; TP1 0.111702 € ; TP2 0.115413 € ; montant 250.00 € ; risque théorique 10.62 € ; R/R net 1.51.
  Chase risk : 2.542/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RED-EUR : 0.14578 € ; score 90.83/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- DEEP-EUR : 0.020176 € ; score 89.46/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- RUNE-EUR : 0.65703 € ; score 87.02/100 ; SURVEILLE ; seuil achat non atteint
- PLUME-EUR : 0.0165035 € ; score 83.54/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.04176 € ; score 83.29/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 230.11 | +39.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 1.09355 | +27.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0046005 | +20.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.02889 | +20.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AUDIO-EUR | 0.01507 | +17.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.073262 | +15.92 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IRYS-EUR | 0.016744 | +13.35 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| ONDO-EUR | 0.524 | +12.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.30154 | +10.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.21618 | +10.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1673 scans ; 715739 observations ; 1234 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
