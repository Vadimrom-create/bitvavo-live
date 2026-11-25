# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-25T01:00:11.491382+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : DODO-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.656 | entrée 6.650 | trend 8.550 | rang 7.369
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KITE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.859 | entrée 6.150 | trend 8.050 | rang 6.737
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.369
2. KITE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.737
3. AI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.545

## Accélération indépendante

- IRYS-EUR — CONFIRMED_ACCELERATION — score 7.372/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- POND-EUR — BUILDING_ACCELERATION — score 6.325/10 — DETECTED_BUT_TOO_LATE
- AI-EUR — BUILDING_ACCELERATION — score 5.837/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 5.584/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — BUILDING_ACCELERATION — score 5.479/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — BUILDING_ACCELERATION — score 4.857/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- MMT-EUR — MEMORY_24H — score mémoire 9.836/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — MEMORY_DECAY_24_72H — score mémoire 8.089/10 — sources ACCELERATION — MEMORY_ONLY
- LISTA-EUR — MEMORY_24H — score mémoire 7.747/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- IRYS-EUR — ACTIVE_NOW — score mémoire 7.372/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.369/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KITE-EUR — ACTIVE_NOW — score mémoire 6.737/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AI-EUR — ACTIVE_NOW — score mémoire 6.545/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- ZRC-EUR — MEMORY_DECAY_24_72H — score mémoire 6.440/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 6.325/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- FIDA-EUR — MEMORY_24H — score mémoire 6.234/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +46.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIGTIME-EUR +14.48% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +8.23% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LISTA-EUR +8.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AI-EUR +7.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TAI-EUR +7.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WIN-EUR +6.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- QKC-EUR +6.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SHELL-EUR +6.38% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZIG-EUR +6.27% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
