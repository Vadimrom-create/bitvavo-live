# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T04:23:11.933843+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T04:22:44.908757+00:00 | âge ticker : 149.7 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.082758 € | IGNITION | score 87.10/100 | entrée 7.60/10
  Entrée 0.08273 € ; stop 0.079093 € ; TP1 0.090004 € ; TP2 0.093641 € ; montant 236.18 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.704/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ZRX-EUR : 0.104304 € ; score 89.00/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- MOODENG-EUR : 0.042623 € ; score 88.72/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PROVE-EUR : 0.19778 € ; score 88.03/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- LINK-EUR : 11.3065 € ; score 87.66/100 ; SURVEILLE ; seuil achat non atteint
- DOGS-EUR : 4.5123e-05 € ; score 87.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.01895 | +119.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0013654 | +75.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.057574 | +46.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.115 | +44.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.0465 | +36.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.6502e-06 | +33.68 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.22338 | +26.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CARV-EUR | 0.041295 | +22.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FORM-EUR | 0.27581 | +21.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DOGE-EUR | 0.091699 | +19.64 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1148 scans ; 491785 observations ; 454 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
