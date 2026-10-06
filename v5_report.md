# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T20:13:21.689952+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-10-06T20:12:48.502564+00:00 | âge ticker : 149.4 s | durée : 151.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AI-EUR : 0.019525 € ; score 87.60/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK, WICK_SETUP
- INJ-EUR : 7.1226 € ; score 86.49/100 ; SURVEILLE ; WICK_SETUP
- ILV-EUR : 3.62 € ; score 85.59/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RENDER-EUR : 1.9075 € ; score 80.40/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.033124 € ; score 80.24/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0053185 | +43.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 14.3876 | +35.31 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ORCA-EUR | 2.505 | +25.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0783245 | +19.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RLC-EUR | 0.69326 | +14.06 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.333 | +13.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| U-EUR | 0.0002492 | +13.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.0204169 | +12.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29279 | +11.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.029833 | +10.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2088 scans ; 893492 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
