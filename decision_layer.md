# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-23T19:34:42.372540+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : ELSA-EUR | action LATENT_ACCELERATOR | opportunité 7.692 | entrée 5.550 | trend 8.450 | rang 6.756
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KMNO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.760 | entrée 6.500 | trend 8.300 | rang 7.152
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. KMNO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.152
2. ELSA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.756
3. CVX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.622

## Accélération indépendante

- CTR-EUR — CONFIRMED_ACCELERATION — score 8.744/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — CONFIRMED_ACCELERATION — score 8.740/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IRYS-EUR — CONFIRMED_ACCELERATION — score 7.981/10 — DETECTED_BUT_TOO_LATE
- RECALL-EUR — CONFIRMED_ACCELERATION — score 7.053/10 — DETECTED_BUT_TOO_LATE
- CAP-EUR — CONFIRMED_ACCELERATION — score 6.826/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — CONFIRMED_ACCELERATION — score 6.577/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GMX-EUR — CONFIRMED_ACCELERATION — score 6.513/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZIL-EUR — BUILDING_ACCELERATION — score 6.459/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FLUID-EUR — BUILDING_ACCELERATION — score 6.185/10 — DETECTED_BUT_TOO_LATE
- ZORA-EUR — BUILDING_ACCELERATION — score 5.945/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 8.820/10 — sources ACCELERATION — MEMORY_ONLY
- CTR-EUR — ACTIVE_NOW — score mémoire 8.744/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SYN-EUR — ACTIVE_NOW — score mémoire 8.740/10 — sources ACCELERATION — WATCH_ONLY
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- UP-EUR — MEMORY_24H — score mémoire 8.160/10 — sources ACCELERATION — MEMORY_ONLY
- EPIC-EUR — MEMORY_24H — score mémoire 8.032/10 — sources ACCELERATION — MEMORY_ONLY
- IRYS-EUR — ACTIVE_NOW — score mémoire 7.981/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 7.921/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 7.743/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.722/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- IRYS-EUR +1021.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- BIRB-EUR +51.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +26.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +21.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +21.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +20.72% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +15.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +12.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RECALL-EUR +12.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- POWR-EUR +11.77% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
