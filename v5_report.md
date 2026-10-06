# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T20:19:12.283064+00:00
État : OK | marchés EUR : 427 | V4 : 381 | données valides : 427
Récupération : 2026-10-06T20:18:36.473087+00:00 | âge ticker : 151.6 s | durée : 152.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WAL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AI-EUR : 0.019543 € ; score 88.07/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK, WICK_SETUP
- INJ-EUR : 7.1741 € ; score 86.84/100 ; SURVEILLE ; WICK_SETUP
- ILV-EUR : 3.6303 € ; score 85.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- RENDER-EUR : 1.9107 € ; score 82.25/100 ; SURVEILLE ; WICK_SETUP
- WAL-EUR : 0.033124 € ; score 80.84/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0053587 | +41.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 14.2011 | +33.33 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ORCA-EUR | 2.61325 | +32.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0781216 | +19.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| U-EUR | 0.0002519 | +14.34 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.382 | +13.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RLC-EUR | 0.68291 | +12.68 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.0204043 | +12.59 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29279 | +11.12 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.05916 | +10.17 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2088 scans ; 893492 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
