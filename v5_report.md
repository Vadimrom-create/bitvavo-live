# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T21:23:25.340664+00:00
État : OK | marchés EUR : 429 | V4 : 395 | données valides : 429
Récupération : 2026-09-29T21:22:54.163322+00:00 | âge ticker : 154.7 s | durée : 155.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NOM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZRO-EUR : 1.4204 € ; score 91.97/100 ; SURVEILLE ; seuil achat non atteint
- NOM-EUR : 0.0018781 € ; score 90.18/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 8.0805 € ; score 86.71/100 ; SURVEILLE ; seuil achat non atteint
- NOS-EUR : 0.39457 € ; score 86.46/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- ROSE-EUR : 0.007965 € ; score 84.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GRASS-EUR | 0.67353 | +33.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016501 | +28.93 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.0894 | +27.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021755 | +21.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.3667 | +21.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.29095 | +20.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0051556 | +17.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0559 | +14.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.090211 | +14.10 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FUEL-EUR | 0.0006894 | +13.88 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1794 scans ; 767536 observations ; 1339 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
