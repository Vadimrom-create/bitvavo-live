# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-27T23:10:48.432811+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.534 | entrée 5.950 | trend 8.300 | rang 7.150
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.150
2. MEGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.147
3. DOS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.337

## Accélération indépendante

- HAEDAL-EUR — BUILDING_ACCELERATION — score 6.448/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 6.084/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAD-EUR — BUILDING_ACCELERATION — score 4.801/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- U-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- GROVE-EUR — MEMORY_24H — score mémoire 7.991/10 — sources ACCELERATION — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.150/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 7.147/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.122/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 6.908/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 6.806/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- BABY-EUR — MEMORY_24H — score mémoire 6.780/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- AZTEC-EUR — MEMORY_24H — score mémoire 6.763/10 — sources ACCELERATION — MEMORY_ONLY
- PARTI-EUR — MEMORY_24H — score mémoire 6.756/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- GROVE-EUR +85.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +42.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ACU-EUR +21.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XAN-EUR +18.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +17.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +15.39% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +14.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- REZ-EUR +14.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +13.20% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRASS-EUR +12.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
