# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T20:56:46.147365+00:00
État : OK | marchés EUR : 428 | V4 : 401 | données valides : 428
Récupération : 2026-09-28T20:56:15.493474+00:00 | âge ticker : 145.4 s | durée : 147.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.72408 € | IGNITION | score 90.90/100 | entrée 7.00/10
  Entrée 0.72431 € ; stop 0.69759 € ; TP1 0.77774 € ; TP2 0.80446 € ; montant 250.00 € ; risque théorique 10.94 € ; R/R net 1.52.
  Chase risk : 2.11/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AIOZ-EUR : 0.104771 € ; score 85.37/100 ; SURVEILLE ; seuil achat non atteint
- YFI-EUR : 2080.3 € ; score 84.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- MIOTA-EUR : 0.049316 € ; score 83.90/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- RUNE-EUR : 0.69185 € ; score 82.39/100 ; SURVEILLE ; WICK_SETUP
- EIGEN-EUR : 0.22039 € ; score 82.28/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.107635 | +29.70 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 216.955 | +26.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 10.2815 | +16.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.119072 | +14.80 % | DETECTED_EARLY | NONE | NONE |
| MIOTA-EUR | 0.049316 | +9.65 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LINK-EUR | 13.4083 | +8.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018145 | +8.78 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| TREAD-EUR | 0.97455 | +8.28 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XLM-EUR | 0.20112 | +5.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.02985 | +5.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1720 scans ; 735833 observations ; 1265 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
