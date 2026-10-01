# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T19:03:10.388411+00:00
État : OK | marchés EUR : 430 | V4 : 384 | données valides : 430
Récupération : 2026-10-01T19:02:30.462568+00:00 | âge ticker : 161.5 s | durée : 162.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- HUMA-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.21317 € | IGNITION | score 83.92/100 | entrée 6.85/10
  Entrée 0.21326 € ; stop 0.20397 € ; TP1 0.23184 € ; TP2 0.24112 € ; montant 238.05 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.743/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HUMA-EUR : 0.030016 € ; score 92.28/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- KSM-EUR : 4.5966 € ; score 87.87/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SKY-EUR : 0.074301 € ; score 86.52/100 ; SURVEILLE ; WICK_SETUP
- ATOM-EUR : 1.5262 € ; score 85.44/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AVAX-EUR : 9.7919 € ; score 83.44/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00062001 | +140.51 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.803 | +79.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04882 | +32.77 % | DETECTED_EARLY | NONE | NONE |
| CAP-EUR | 0.0768778 | +30.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.18303 | +28.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.031069 | +21.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.100533 | +21.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.50575 | +20.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.172856 | +20.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.43891 | +20.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1926 scans ; 824258 observations ; 1489 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
