# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T14:34:16.653836+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.042 | entrée 7.500 | trend 8.750 | rang 7.946
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.732 | entrée 6.750 | trend 8.250 | rang 7.381
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.517 | entrée 4.500 | trend 8.550 | rang 6.645
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : PEPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.809 | entrée 7.700 | trend 7.900 | rang 7.532
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.946
2. SOL-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.862
3. USELESS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.607

## Accélération indépendante

- ONDO-EUR — BUILDING_ACCELERATION — score 5.954/10 — DETECTED_BUT_TOO_LATE
- ZIG-EUR — BUILDING_ACCELERATION — score 5.557/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- USELESS-EUR — ACTIVE_NOW — score mémoire 7.607/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ATH-EUR — ACTIVE_NOW — score mémoire 8.337/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 8.324/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 8.266/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.110/10 — sources V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.070/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.026/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — ACTIVE_NOW — score mémoire 7.976/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +45.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +38.60% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.09% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +27.63% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +27.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +22.02% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +21.96% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +21.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +19.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
