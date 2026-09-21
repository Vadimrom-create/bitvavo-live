# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T14:22:12.407492+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : SOL-EUR | action ACHETE_MAINTENANT | opportunité 7.860 | entrée 7.700 | trend 7.950 | rang 7.514
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : MIRA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.981 | entrée 6.700 | trend 7.450 | rang 7.708
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : COW-EUR | action LATENT_ACCELERATOR | opportunité 8.547 | entrée 4.850 | trend 9.200 | rang 8.066
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : MERL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.320 | entrée 6.700 | trend 8.950 | rang 8.049
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. COW-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 8.066
2. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.049
3. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.979

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 6.679/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTC-EUR — BUILDING_ACCELERATION — score 5.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GIGA-EUR — BUILDING_ACCELERATION — score 5.936/10 — DETECTED_BUT_TOO_LATE
- ACX-EUR — BUILDING_ACCELERATION — score 5.597/10 — DETECTED_BUT_TOO_LATE
- SWELL-EUR — BUILDING_ACCELERATION — score 5.455/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 5.188/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_24H — score mémoire 9.925/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- TREAD-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ICX-EUR — MEMORY_24H — score mémoire 8.457/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 8.066/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 8.049/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +68.40% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +52.70% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +43.57% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +38.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FTT-EUR +32.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +29.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +29.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SUI-EUR +26.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +26.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AKT-EUR +24.62% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
