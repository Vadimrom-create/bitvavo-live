# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T12:38:11.438253+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T12:37:47.216112+00:00 | âge ticker : 142.2 s | durée : 142.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SOL-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZORA-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- EIGEN-EUR : 0.20723 € ; score 89.15/100 ; SURVEILLE ; WICK_SETUP
- ZORA-EUR : 0.007501 € ; score 87.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAT-EUR : 0.00436 € ; score 87.25/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- AI-EUR : 0.01835 € ; score 87.09/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- ZRO-EUR : 1.0477 € ; score 86.09/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017431 | +98.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014299 | +81.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XMN-EUR | 0.000548 | +31.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.053551 | +28.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.072568 | +26.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AIOZ-EUR | 0.118588 | +24.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28419 | +21.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.2309 | +19.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.3803 | +17.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.2696e-06 | +15.71 % | DETECTED_EARLY | NONE | NONE |

Historique : 1184 scans ; 507121 observations ; 492 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
