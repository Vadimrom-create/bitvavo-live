# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-13T11:20:25.286112+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SXT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.311 | entrée 5.400 | trend 8.150 | rang 6.968
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SXT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.968
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.002

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 7.974/10 — DETECTED_BUT_TOO_LATE
- 0G-EUR — BUILDING_ACCELERATION — score 6.209/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 5.490/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- REQ-EUR — BUILDING_ACCELERATION — score 4.973/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — BUILDING_ACCELERATION — score 4.889/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ALIGN-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- HUMA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.245/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — ACTIVE_NOW — score mémoire 7.974/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.820/10 — sources ACCELERATION — MEMORY_ONLY
- SXT-EUR — ACTIVE_NOW — score mémoire 6.968/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- INIT-EUR — MEMORY_24H — score mémoire 6.767/10 — sources ACCELERATION — MEMORY_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 6.485/10 — sources DECISION_LAYER — MEMORY_ONLY
- CROSS-EUR — ACTIVE_NOW — score mémoire 6.478/10 — sources V4 — WATCH_ONLY
- CT-EUR — MEMORY_24H — score mémoire 6.476/10 — sources ACCELERATION — MEMORY_ONLY
- OPEN-EUR — MEMORY_24H — score mémoire 6.406/10 — sources DECISION_LAYER — MEMORY_ONLY

## Audit des plus fortes hausses

- DODO-EUR +26.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- 0G-EUR +8.15% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- OSMO-EUR +7.25% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- USELESS-EUR +6.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +6.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +6.17% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALLO-EUR +6.02% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZEUS-EUR +5.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NPC-EUR +5.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- O-EUR +5.54% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Gestion des positions détenues

Policy : STAGED_10_20_RUNNER_V1
- +10% : prise partielle 35%.
- +20% : seconde prise 35%.
- Runner conservé : 30%.
- Revue coût d'opportunité après 72 h ; sortie seulement avant la première partielle, proche/sous le PRU et avec momentum 15m affaibli.
- Pas de stop serré mécaniquement après une petite hausse ; le stop reste lié à l'invalidation structurelle.

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
