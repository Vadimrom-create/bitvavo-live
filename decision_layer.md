# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-29T03:19:04.778037+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : AZTEC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.679 | entrée 6.450 | trend 8.400 | rang 7.527
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : MIOTA-EUR | action LATENT_ACCELERATOR | opportunité 8.198 | entrée 5.450 | trend 8.450 | rang 7.630
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : LINK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.993 | entrée 6.700 | trend 9.200 | rang 8.009
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. LINK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.009
2. XDC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.898
3. MIOTA-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.630

## Accélération indépendante

- CELO-EUR — CONFIRMED_ACCELERATION — score 7.077/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NMR-EUR — BUILDING_ACCELERATION — score 5.624/10 — DETECTED_BUT_TOO_LATE
- FLUX-EUR — BUILDING_ACCELERATION — score 5.399/10 — DETECTED_BUT_TOO_LATE
- RE-EUR — BUILDING_ACCELERATION — score 4.914/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 8.844/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- IMU-EUR — MEMORY_24H — score mémoire 8.632/10 — sources ACCELERATION — MEMORY_ONLY
- VIRTUAL-EUR — MEMORY_24H — score mémoire 8.271/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 8.100/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LINK-EUR — ACTIVE_NOW — score mémoire 8.009/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIXBT-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- XDC-EUR — ACTIVE_NOW — score mémoire 7.898/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ME-EUR — MEMORY_24H — score mémoire 7.735/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- NMR-EUR +43.94% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HBAR-EUR +24.10% — DETECTED_EARLY — couche NONE — action NONE
- ALGO-EUR +15.57% — DETECTED_EARLY — couche NONE — action NONE
- 0G-EUR +13.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CRV-EUR +12.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARX-EUR +10.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CELO-EUR +9.90% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IKA-EUR +8.98% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- SYRUP-EUR +6.83% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AZTEC-EUR +6.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
