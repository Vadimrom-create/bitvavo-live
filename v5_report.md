# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T11:38:52.361687+00:00
État : OK | marchés EUR : 430 | V4 : 389 | données valides : 430
Récupération : 2026-10-02T11:38:23.580814+00:00 | âge ticker : 145.4 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- ORCA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : SPREAD_RISK, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.48294 € ; score 93.39/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 12.8644 € ; score 88.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HOT-EUR : 0.0004085 € ; score 88.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SENT-EUR : 0.018886 € ; score 87.72/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0079122 € ; score 87.48/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.059559 | +56.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.116598 | +29.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.52798 | +21.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.093556 | +19.64 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SCR-EUR | 0.026639 | +18.29 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.082222 | +16.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MAGIC-EUR | 0.053969 | +15.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.19904 | +14.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZK-EUR | 0.011993 | +13.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.229278 | +12.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1976 scans ; 845758 observations ; 1557 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
