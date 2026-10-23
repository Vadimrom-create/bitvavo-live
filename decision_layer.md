# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-23T10:31:31.713349+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PHA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.890 | entrée 6.550 | trend 8.000 | rang 6.667
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.667
2. AVA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.667
3. PROM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.386

## Accélération indépendante

- UP-EUR — CONFIRMED_ACCELERATION — score 8.648/10 — DETECTED_BUT_TOO_LATE
- MIRA-EUR — BUILDING_ACCELERATION — score 5.607/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 5.190/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AI-EUR — BUILDING_ACCELERATION — score 4.761/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 8.820/10 — sources ACCELERATION — MEMORY_ONLY
- UP-EUR — ACTIVE_NOW — score mémoire 8.648/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EPIC-EUR — MEMORY_24H — score mémoire 8.032/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 7.921/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 7.742/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.722/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.699/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_DECAY_24_72H — score mémoire 7.166/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 7.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — MEMORY_24H — score mémoire 7.065/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +88.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +40.96% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +24.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +15.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GROVE-EUR +12.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +11.22% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PEPE-EUR +10.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEW-EUR +9.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +8.94% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KERNEL-EUR +8.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
