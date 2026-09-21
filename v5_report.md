# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T03:42:57.795789+00:00
État : OK | marchés EUR : 426 | V4 : 371 | données valides : 426
Récupération : 2026-09-21T03:42:26.942492+00:00 | âge ticker : 145.0 s | durée : 145.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- COMP-EUR : 19.532 € ; score 90.91/100 ; SURVEILLE ; seuil achat non atteint
- KAS-EUR : 0.034869 € ; score 90.10/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AZTEC-EUR : 0.014444 € ; score 89.32/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK
- MANA-EUR : 0.07239 € ; score 89.21/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP, STABILITY_HOLD
- GRT-EUR : 0.019986 € ; score 88.53/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PTB-EUR | 0.0011717 | +90.83 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| SAGA-EUR | 0.031226 | +36.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FTT-EUR | 0.24914 | +36.53 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.055265 | +27.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.030666 | +25.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 3.764 | +23.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VVV-EUR | 28.3211 | +22.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EPIC-EUR | 0.49858 | +21.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.46797 | +19.57 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| PEAQ-EUR | 0.030551 | +18.74 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1044 scans ; 447481 observations ; 299 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
