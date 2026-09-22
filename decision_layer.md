# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T10:21:29.533360+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : NEAR-EUR | action ACHETE_MAINTENANT | opportunité 7.554 | entrée 7.600 | trend 8.100 | rang 7.336
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.924 | entrée 6.150 | trend 8.700 | rang 7.740
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 7.707 | entrée 4.100 | trend 8.850 | rang 7.309
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAIKO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.043 | entrée 7.400 | trend 8.700 | rang 7.925
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAIKO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.925
2. COW-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.740
3. SEI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.691

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- USELESS-EUR — CONFIRMED_ACCELERATION — score 7.708/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — BUILDING_ACCELERATION — score 5.076/10 — DETECTED_BUT_TOO_LATE
- QNT-EUR — BUILDING_ACCELERATION — score 5.068/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 4.978/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 9.015/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 8.130/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 7.941/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TAIKO-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 7.708/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SEI-EUR — ACTIVE_NOW — score mémoire 7.691/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ICX-EUR +105.08% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +92.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +42.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +33.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +24.13% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +23.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +19.87% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- PEPE-EUR +19.53% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +19.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- TREAD-EUR +19.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
