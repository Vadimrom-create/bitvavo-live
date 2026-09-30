# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T05:24:49.982346+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T05:24:20.609007+00:00 | âge ticker : 145.9 s | durée : 146.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 3.0561 € | IGNITION | score 85.31/100 | entrée 6.90/10
  Entrée 3.0631 € ; stop 2.9373 € ; TP1 3.3146 € ; TP2 3.4404 € ; montant 250.00 € ; risque théorique 11.98 € ; R/R net 1.56.
  Chase risk : 1.636/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GALA-EUR : 0.0020031 € ; score 88.01/100 ; SURVEILLE ; seuil achat non atteint
- GRAM-EUR : 1.3335 € ; score 87.03/100 ; SURVEILLE ; seuil achat non atteint
- NIL-EUR : 0.072622 € ; score 86.39/100 ; SURVEILLE ; seuil achat non atteint
- TRAC-EUR : 0.34757 € ; score 85.49/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- YFI-EUR : 2149.7 € ; score 84.91/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.2977 | +53.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.37301 | +43.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.00175 | +31.58 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0024191 | +28.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.6362 | +22.07 % | DETECTED_EARLY | NONE | NONE |
| MEW-EUR | 0.0004963 | +21.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.32042 | +21.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.064033 | +17.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.092638 | +16.34 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PUMP-EUR | 0.0050351 | +15.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1819 scans ; 778261 observations ; 1355 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
