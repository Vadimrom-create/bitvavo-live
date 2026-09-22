# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T10:21:29.533360+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T10:20:53.821996+00:00 | âge ticker : 152.0 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- QNT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- QNT-EUR : 59.75 € ; score 85.54/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- EGLD-EUR : 3.8892 € ; score 81.13/100 ; SURVEILLE ; SPREAD_RISK
- TAIKO-EUR : 0.08108 € ; score 80.43/100 ; SURVEILLE ; seuil achat non atteint
- SEI-EUR : 0.053422 € ; score 80.08/100 ; SURVEILLE ; seuil achat non atteint
- PIXEL-EUR : 0.0047727 € ; score 79.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0181 | +105.08 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0015142 | +92.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.11903 | +42.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056949 | +33.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.07102 | +24.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.4005 | +23.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CARV-EUR | 0.041311 | +19.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEPE-EUR | 4.3224e-06 | +19.53 % | DETECTED_EARLY | NONE | NONE |
| WIF-EUR | 0.2195 | +19.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46205 | +19.05 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1174 scans ; 502861 observations ; 479 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
