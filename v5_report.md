# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T03:52:36.240836+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-26T03:52:01.688723+00:00 | âge ticker : 154.2 s | durée : 155.1 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CAKE-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- CAKE-EUR : 2.4668 € ; score 90.24/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : 0.037565 € ; score 89.06/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LPT-EUR : 1.505 € ; score 88.92/100 ; SURVEILLE ; seuil achat non atteint
- MANTRA-EUR : 0.004194 € ; score 86.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LINK-EUR : 12.3439 € ; score 85.48/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0014647 | +88.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.072204 | +65.63 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.24609 | +44.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.035221 | +32.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AERO-EUR | 0.77748 | +26.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WMTX-EUR | 0.022624 | +21.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.104732 | +21.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENA-EUR | 0.23533 | +20.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.73952 | +17.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.50812 | +16.82 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1500 scans ; 641868 observations ; 943 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
