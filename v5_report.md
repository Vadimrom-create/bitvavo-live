# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T09:39:56.645924+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T09:38:59.274747+00:00 | âge ticker : 179.9 s | durée : 180.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : 0.48559 € | IGNITION | score 84.87/100 | entrée 7.20/10
  Entrée 0.48556 € ; stop 0.46651 € ; TP1 0.52366 € ; TP2 0.54271 € ; montant 250.00 € ; risque théorique 11.52 € ; R/R net 1.54.
  Chase risk : 2.737/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RE-EUR : 0.4462 € ; score 86.97/100 ; SURVEILLE ; WICK_SETUP
- PIXEL-EUR : 0.0054507 € ; score 86.82/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- TRIA-EUR : 0.003627 € ; score 81.80/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- IMX-EUR : 0.15857 € ; score 81.25/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- PYTH-EUR : 0.068475 € ; score 80.99/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00077732 | +197.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.056455 | +47.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.115 | +29.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.53522 | +28.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MAGIC-EUR | 0.055222 | +16.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.091873 | +16.67 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SCR-EUR | 0.02614 | +15.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.029758 | +15.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.2005 | +13.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.078395 | +12.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1970 scans ; 843178 observations ; 1555 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
