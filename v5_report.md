# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T08:23:19.073695+00:00
État : OK | marchés EUR : 426 | V4 : 400 | données valides : 426
Récupération : 2026-09-23T08:22:17.008037+00:00 | âge ticker : 185.7 s | durée : 186.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- QNT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NPC-EUR : 0.0218173 € | IGNITION | score 90.08/100 | entrée 7.15/10
  Entrée 0.0218184 € ; stop 0.0207978 € ; TP1 0.0238596 € ; TP2 0.0248802 € ; montant 223.82 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 2.517/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 55.72 € ; score 83.92/100 ; SURVEILLE ; WICK_SETUP
- QNT-EUR : 66.119 € ; score 83.51/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : 84.492 € ; score 82.16/100 ; SURVEILLE ; seuil achat non atteint
- BABY-EUR : 0.011616 € ; score 81.75/100 ; SURVEILLE ; seuil achat non atteint
- RECALL-EUR : 0.04179 € ; score 81.55/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| CPOOL-EUR | 0.03403 | +39.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.32721 | +35.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.08871 | +34.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 311.88 | +33.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.16651 | +25.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.019114 | +24.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SENT-EUR | 0.020248 | +21.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.2683 | +21.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALLO-EUR | 0.279512 | +21.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0095985 | +20.99 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1255 scans ; 537367 observations ; 624 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
