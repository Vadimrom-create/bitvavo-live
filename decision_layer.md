# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-28T13:10:02.679547+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : W-EUR | action ACHETE_MAINTENANT | opportunité 9.352 | entrée 7.100 | trend 8.650 | rang 8.275
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : SNX-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.959 | entrée 6.150 | trend 7.400 | rang 7.598
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : IMX-EUR | action LATENT_ACCELERATOR | opportunité 8.291 | entrée 5.150 | trend 8.900 | rang 7.697
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.492 | entrée 6.700 | trend 8.650 | rang 7.953
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

1. W-EUR — ACHETE_MAINTENANT — rank 8.275 — opportunité 9.352 — entrée 7.100 — trend 8.650
2. LINK-EUR — ACHETE_MAINTENANT — rank 8.045 — opportunité 9.293 — entrée 7.700 — trend 8.550
3. KAS-EUR — ACHETE_MAINTENANT — rank 7.846 — opportunité 8.155 — entrée 7.250 — trend 8.700
4. RENDER-EUR — ACHETE_MAINTENANT — rank 7.689 — opportunité 8.309 — entrée 7.100 — trend 8.100
5. BCH-EUR — ACHETE_MAINTENANT — rank 7.570 — opportunité 8.530 — entrée 6.950 — trend 7.550
6. NEAR-EUR — ACHETE_MAINTENANT — rank 7.549 — opportunité 8.007 — entrée 6.900 — trend 8.250
7. XLM-EUR — ACHETE_MAINTENANT — rank 7.323 — opportunité 8.187 — entrée 6.850 — trend 8.300
8. ONDO-EUR — ACHETE_MAINTENANT — rank 7.307 — opportunité 7.876 — entrée 6.900 — trend 7.750
9. GMT-EUR — ACHETE_MAINTENANT — rank 7.306 — opportunité 8.828 — entrée 7.000 — trend 6.750

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. W-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.275
2. LINK-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.045
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.953

## Accélération indépendante

- AGI-EUR — CONFIRMED_ACCELERATION — score 8.533/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — CONFIRMED_ACCELERATION — score 6.515/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — BUILDING_ACCELERATION — score 6.306/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 5.839/10 — DETECTED_BUT_TOO_LATE
- ALT-EUR — BUILDING_ACCELERATION — score 5.107/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LINK-EUR — ACTIVE_NOW — score mémoire 8.045/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- XLM-EUR — ACTIVE_NOW — score mémoire 7.323/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- WMTX-EUR — MEMORY_24H — score mémoire 9.914/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 9.434/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.779/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AGI-EUR — ACTIVE_NOW — score mémoire 8.533/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FUEL-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 8.275/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SAGA-EUR — MEMORY_24H — score mémoire 8.221/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FRAX-EUR — MEMORY_DECAY_24_72H — score mémoire 8.138/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- XDP-EUR +69.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- QNT-EUR +44.13% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +25.32% — DETECTED_EARLY — couche NONE — action NONE
- PUMP-EUR +18.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRT-EUR +15.26% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOON-EUR +13.36% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- NMR-EUR +13.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ALGO-EUR +11.81% — DETECTED_EARLY — couche NONE — action NONE
- MON-EUR +11.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +9.59% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
