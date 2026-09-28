# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T17:43:18.983697+00:00
État : OK | marchés EUR : 428 | V4 : 403 | données valides : 427
Récupération : 2026-09-28T17:42:48.047476+00:00 | âge ticker : 150.8 s | durée : 153.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- XDC-EUR : 0.030596 € | IGNITION | score 92.23/100 | entrée 7.10/10
  Entrée 0.030737 € ; stop 0.029518 € ; TP1 0.033175 € ; TP2 0.034394 € ; montant 250.00 € ; risque théorique 11.63 € ; R/R net 1.55.
  Chase risk : 3.884/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- CC-EUR : 0.11652 € | IGNITION | score 88.52/100 | entrée 6.85/10
  Entrée 0.11651 € ; stop 0.11079 € ; TP1 0.12795 € ; TP2 0.13367 € ; montant 214.58 € ; risque théorique 12.00 € ; R/R net 1.62.
  Chase risk : 0.277/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AERO-EUR : 0.71921 € ; score 92.23/100 ; SURVEILLE ; WICK_SETUP
- BAT-EUR : 0.08 € ; score 90.96/100 ; SURVEILLE ; seuil achat non atteint
- RUNE-EUR : 0.69947 € ; score 90.19/100 ; SURVEILLE ; WICK_SETUP
- RPL-EUR : 1.7197 € ; score 88.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LINK-EUR : 13.383 € ; score 83.74/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.113606 | +38.17 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 217.758 | +35.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.119 | +14.81 % | DETECTED_EARLY | NONE | NONE |
| IKA-EUR | 0.0018757 | +12.72 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MIOTA-EUR | 0.049087 | +11.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 9.6286 | +9.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.004634 | +8.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MON-EUR | 0.025315 | +8.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDC-EUR | 0.030596 | +8.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LINK-EUR | 13.383 | +7.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1709 scans ; 731125 observations ; 1264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
