# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T05:14:47.571662+00:00
État : OK | marchés EUR : 428 | V4 : 395 | données valides : 428
Récupération : 2026-09-29T05:14:18.228484+00:00 | âge ticker : 150.5 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 2.8486 € | IGNITION | score 77.54/100 | entrée 6.90/10
  Entrée 2.8459 € ; stop 2.7024 € ; TP1 3.1329 € ; TP2 3.2763 € ; montant 209.62 € ; risque théorique 12.00 € ; R/R net 1.63.
  Chase risk : 5.073/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RUNE-EUR : 0.68736 € ; score 92.37/100 ; SURVEILLE ; seuil achat non atteint
- AUDIO-EUR : 0.013662 € ; score 88.43/100 ; SURVEILLE ; WIDE_SPREAD_RISK
- W-EUR : 0.01235 € ; score 85.42/100 ; SURVEILLE ; seuil achat non atteint
- MIOTA-EUR : 0.049146 € ; score 84.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- UNI-EUR : 7.5582 € ; score 84.99/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.0208 | +35.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.104631 | +24.88 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.121169 | +18.57 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.26302 | +17.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.34121 | +16.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.61908 | +12.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.089379 | +10.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.049146 | +9.64 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CVX-EUR | 1.9654 | +8.19 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| XLM-EUR | 0.19873 | +7.89 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1747 scans ; 747389 observations ; 1283 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
