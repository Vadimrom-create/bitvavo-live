# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T15:58:12.901872+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-01T15:57:46.310536+00:00 | âge ticker : 143.9 s | durée : 144.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TRX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 149.92 € | IGNITION | score 83.89/100 | entrée 6.80/10
  Entrée 149.97 € ; stop 144.35 € ; TP1 161.21 € ; TP2 166.83 € ; montant 250.00 € ; risque théorique 11.09 € ; R/R net 1.53.
  Chase risk : 2.041/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KITE-EUR : 0.13377 € ; score 92.61/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- RUNE-EUR : 0.6951 € ; score 91.29/100 ; SURVEILLE ; SPREAD_RISK
- PROM-EUR : 5.9085 € ; score 89.67/100 ; SURVEILLE ; WICK_SETUP
- LPT-EUR : 1.519 € ; score 88.72/100 ; SURVEILLE ; WICK_SETUP
- ASTER-EUR : 0.65695 € ; score 87.06/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00054999 | +110.40 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.5937 | +70.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0755334 | +32.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.18499 | +27.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.42501 | +22.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NOS-EUR | 0.48797 | +21.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.178316 | +20.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04533 | +19.83 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.029152 | +19.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVE-EUR | 0.009377 | +14.42 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1917 scans ; 820388 observations ; 1482 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
