# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T21:17:44.636743+00:00
État : OK | marchés EUR : 428 | V4 : 401 | données valides : 428
Récupération : 2026-09-28T21:16:44.952826+00:00 | âge ticker : 179.0 s | durée : 181.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.73 € | IGNITION | score 92.81/100 | entrée 7.30/10
  Entrée 0.7309 € ; stop 0.6972 € ; TP1 0.79829 € ; TP2 0.83199 € ; montant 226.65 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 2.73/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HUMA-EUR : 0.02506 € ; score 92.88/100 ; SURVEILLE ; seuil achat non atteint
- 2Z-EUR : 0.059191 € ; score 90.83/100 ; SURVEILLE ; SPREAD_RISK
- ARPA-EUR : 0.0095416 € ; score 84.83/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- ATOM-EUR : 1.54 € ; score 84.21/100 ; SURVEILLE ; WICK_SETUP
- RUNE-EUR : 0.69352 € ; score 83.35/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.107492 | +28.31 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 217.661 | +25.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 10.1776 | +15.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.118853 | +13.64 % | DETECTED_EARLY | NONE | NONE |
| MIOTA-EUR | 0.049048 | +9.46 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| IKA-EUR | 0.0018231 | +9.29 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LINK-EUR | 13.478 | +8.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.98197 | +7.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.30356 | +6.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.24535 | +6.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1721 scans ; 736261 observations ; 1266 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
