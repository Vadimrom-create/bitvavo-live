# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-03T06:17:38.415434+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AXS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.107 | entrée 6.300 | trend 9.000 | rang 7.798
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MAGIC-EUR | action LATENT_ACCELERATOR | opportunité 7.887 | entrée 5.200 | trend 8.650 | rang 7.560
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.586 | entrée 6.650 | trend 8.750 | rang 7.961
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.961
2. AAVE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.878
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.865

## Accélération indépendante

- SWEAT-EUR — CONFIRMED_ACCELERATION — score 6.607/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 9.737/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 9.039/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEOPLE-EUR — MEMORY_24H — score mémoire 9.036/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 8.978/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOSO-EUR — MEMORY_24H — score mémoire 8.156/10 — sources ACCELERATION — MEMORY_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.961/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CSPR-EUR — MEMORY_24H — score mémoire 7.942/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.865/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AXS-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SAND-EUR +70.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MANA-EUR +22.35% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ENJ-EUR +16.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +13.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ATH-EUR +12.43% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APE-EUR +10.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CHZ-EUR +9.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AXS-EUR +8.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IMX-EUR +8.43% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FOLD-EUR +7.82% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

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
