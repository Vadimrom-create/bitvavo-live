# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T21:50:51.937170+00:00
État : OK | marchés EUR : 428 | V4 : 402 | données valides : 428
Récupération : 2026-09-28T21:50:15.836240+00:00 | âge ticker : 152.8 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.070409 € ; score 88.93/100 ; SURVEILLE ; seuil achat non atteint
- CAP-EUR : 0.0492449 € ; score 87.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- DATAIP-EUR : 0.1964 € ; score 85.44/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.030077 € ; score 79.67/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- RUNE-EUR : 0.68808 € ; score 79.29/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 11.91 | +34.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.107369 | +28.96 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.117673 | +13.32 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.99013 | +12.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.04904 | +9.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0018245 | +9.38 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.3168 | +8.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AZTEC-EUR | 0.016898 | +6.27 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0492449 | +5.57 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SOON-EUR | 0.30381 | +5.06 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1723 scans ; 737117 observations ; 1267 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
