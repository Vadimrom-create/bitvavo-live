# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T19:35:38.607349+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T19:34:39.010866+00:00 | âge ticker : 181.5 s | durée : 182.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- STX-EUR : INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : 0.0078881 € | IGNITION | score 89.00/100 | entrée 8.00/10
  Entrée 0.0078837 € ; stop 0.0075932 € ; TP1 0.0084647 € ; TP2 0.0087552 € ; montant 250.00 € ; risque théorique 10.93 € ; R/R net 1.52.
  Chase risk : 2.397/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ACH-EUR : 0.0051716 € ; score 90.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZRO-EUR : 1.0341 € ; score 89.24/100 ; SURVEILLE ; seuil achat non atteint
- BAT-EUR : 0.07301 € ; score 88.89/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- CC-EUR : 0.10032 € ; score 88.75/100 ; SURVEILLE ; seuil achat non atteint
- IO-EUR : 0.12968 € ; score 88.44/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0192 | +127.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0016752 | +117.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZETA-EUR | 0.053266 | +57.09 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.045751 | +43.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.109427 | +36.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30514 | +35.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0008672 | +33.44 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010297 | +32.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.234821 | +26.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.33001 | +25.67 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1106 scans ; 473893 observations ; 404 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
