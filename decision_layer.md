# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T08:30:28.392736+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : TAIKO-EUR | action ACHETE_MAINTENANT | opportunité 8.031 | entrée 7.150 | trend 8.700 | rang 7.908
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : RED-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.064 | entrée 6.050 | trend 8.650 | rang 7.604
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 7.791 | entrée 5.550 | trend 8.700 | rang 7.617
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.270 | entrée 7.850 | trend 8.400 | rang 8.042
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.042
2. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.021
3. SUPER-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.972

## Accélération indépendante

- ICX-EUR — CONFIRMED_ACCELERATION — score 8.928/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 7.204/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CVC-EUR — CONFIRMED_ACCELERATION — score 7.161/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 4.844/10 — DETECTED_BUT_TOO_LATE
- ZAMA-EUR — BUILDING_ACCELERATION — score 4.780/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- TREAD-EUR — MEMORY_24H — score mémoire 9.367/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- FLOCK-EUR — MEMORY_24H — score mémoire 8.979/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — ACTIVE_NOW — score mémoire 8.928/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ICX-EUR +114.96% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZRC-EUR +88.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +46.86% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +38.55% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +24.23% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +23.86% — DETECTED_EARLY — couche NONE — action NONE
- USELESS-EUR +21.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +21.03% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CARV-EUR +17.70% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- FORM-EUR +17.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
