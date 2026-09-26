# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T13:08:06.341884+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T13:07:07.128009+00:00 | âge ticker : 176.3 s | durée : 177.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 291.99 € | IGNITION | score 79.33/100 | entrée 6.90/10
  Entrée 291.88 € ; stop 278.76 € ; TP1 318.12 € ; TP2 331.24 € ; montant 231.69 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 5.101/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- KAS-EUR : 0.040034 € ; score 91.66/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GOAT-EUR : 0.017214 € ; score 91.54/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- JUP-EUR : 0.30957 € ; score 88.12/100 ; SURVEILLE ; WICK_SETUP
- GRAM-EUR : 1.2945 € ; score 88.03/100 ; SURVEILLE ; WICK_SETUP
- MIOTA-EUR : 0.045226 € ; score 85.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0020691 | +155.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.020234 | +65.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AMP-EUR | 0.0006056 | +36.67 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.062741 | +28.75 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.24237 | +21.48 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| EDGE-EUR | 0.102036 | +19.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.53 | +16.26 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RUNE-EUR | 0.65653 | +15.59 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| AERO-EUR | 0.80556 | +15.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ACE-EUR | 0.19188 | +13.14 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1533 scans ; 655959 observations ; 989 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
