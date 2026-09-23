# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T23:00:59.796713+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T23:00:27.075281+00:00 | âge ticker : 152.6 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETH-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DATAIP-EUR : 0.1997 € ; score 89.42/100 ; SURVEILLE ; seuil achat non atteint
- EDEN-EUR : 0.052954 € ; score 85.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- SLX-EUR : 0.06395 € ; score 82.52/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- MOVR-EUR : 0.761 € ; score 81.14/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LTC-EUR : 54.227 € ; score 80.51/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.100584 | +46.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CPOOL-EUR | 0.032076 | +26.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.041982 | +20.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.017523 | +20.01 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NOM-EUR | 0.0017482 | +15.16 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.76897 | +12.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.15471 | +11.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0455019 | +10.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.30479 | +9.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOSO-EUR | 0.28789 | +9.41 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |

Historique : 1306 scans ; 559093 observations ; 669 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
