# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T03:47:56.056456+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-02T03:47:20.604077+00:00 | âge ticker : 158.3 s | durée : 159.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 156.66 € ; score 94.26/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ESP-EUR : 0.09276 € ; score 89.78/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.22813 € ; score 87.54/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.03744 € ; score 86.80/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.03051 € ; score 84.11/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00062436 | +142.11 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.137756 | +64.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.030709 | +41.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.43751 | +25.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.0473 | +20.23 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.164498 | +18.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.17283 | +16.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0023607 | +13.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20274 | +13.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TOWNS-EUR | 0.0021028 | +11.98 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1953 scans ; 835868 observations ; 1518 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
