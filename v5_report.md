# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T17:58:59.289880+00:00
État : OK | marchés EUR : 428 | V4 : 402 | données valides : 427
Récupération : 2026-09-28T17:58:28.073148+00:00 | âge ticker : 148.9 s | durée : 149.7 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.03084 € | IGNITION | score 90.52/100 | entrée 7.45/10
  Entrée 0.030848 € ; stop 0.029512 € ; TP1 0.03352 € ; TP2 0.034856 € ; montant 239.25 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.137/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- CC-EUR : 0.11762 € | IGNITION | score 86.00/100 | entrée 6.85/10
  Entrée 0.11739 € ; stop 0.11098 € ; TP1 0.13021 € ; TP2 0.13662 € ; montant 195.40 € ; risque théorique 12.00 € ; R/R net 1.66.
  Chase risk : 3.268/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MAGIC-EUR : 0.047017 € ; score 90.76/100 ; SURVEILLE ; seuil achat non atteint
- JASMY-EUR : 0.0045069 € ; score 90.06/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SYRUP-EUR : 0.1915 € ; score 84.78/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINEA-EUR : 0.0026797 € ; score 84.06/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- AERO-EUR : 0.72627 € ; score 84.02/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.114029 | +37.99 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 217.866 | +35.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.120129 | +15.26 % | DETECTED_EARLY | NONE | NONE |
| IKA-EUR | 0.0019109 | +14.83 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MIOTA-EUR | 0.050569 | +14.54 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 9.7149 | +9.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.025544 | +9.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDC-EUR | 0.03084 | +8.97 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LINK-EUR | 13.2855 | +7.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0046079 | +6.09 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1710 scans ; 731553 observations ; 1264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
