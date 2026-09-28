# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T18:24:33.270007+00:00
État : OK | marchés EUR : 428 | V4 : 403 | données valides : 427
Récupération : 2026-09-28T18:23:59.083319+00:00 | âge ticker : 152.6 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.031131 € | IGNITION | score 90.62/100 | entrée 7.30/10
  Entrée 0.031152 € ; stop 0.029541 € ; TP1 0.034373 € ; TP2 0.035984 € ; montant 205.01 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 4.281/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CFG-EUR : 0.138869 € ; score 90.55/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.68356 € ; score 83.64/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.20509 € ; score 83.58/100 ; SURVEILLE ; WICK_SETUP
- CC-EUR : 0.11663 € ; score 82.18/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 13.3976 € ; score 80.85/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.112966 | +35.66 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 209.476 | +29.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.121545 | +15.16 % | DETECTED_EARLY | NONE | NONE |
| MIOTA-EUR | 0.049107 | +11.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| XDC-EUR | 0.031131 | +9.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.8151 | +8.85 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.025421 | +7.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.0017909 | +7.62 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.3976 | +7.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XLM-EUR | 0.20509 | +7.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1711 scans ; 731981 observations ; 1264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
