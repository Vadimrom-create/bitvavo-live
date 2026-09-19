# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T10:44:55.950952+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : ONDO-EUR | action ACHETE_MAINTENANT | opportunité 8.868 | entrée 7.800 | trend 7.650 | rang 7.869
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : SOL-EUR | action LATENT_ACCELERATOR | opportunité 7.639 | entrée 4.500 | trend 8.250 | rang 7.254
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.955 | entrée 6.300 | trend 8.750 | rang 7.805
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.869
2. APT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.857
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.805

## Accélération indépendante

- SUI-EUR — BUILDING_ACCELERATION — score 5.352/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- SUI-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- TAO-EUR — ACTIVE_NOW — score mémoire 7.405/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- KAS-EUR — ACTIVE_NOW — score mémoire 8.368/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 8.355/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.239/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.209/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 8.179/10 — sources V4 — WATCH_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.067/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AIOZ-EUR — MEMORY_24H — score mémoire 7.913/10 — sources V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +43.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +37.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +35.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +31.76% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +31.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +28.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- HEI-EUR +26.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +25.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIG-EUR +25.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +24.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
