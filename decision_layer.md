# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-22T19:11:27.447837+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.621 | entrée 6.650 | trend 7.850 | rang 6.842
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.842
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.800
3. CVX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.787

## Accélération indépendante

- VELO-EUR — CONFIRMED_ACCELERATION — score 7.742/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNO-EUR — CONFIRMED_ACCELERATION — score 6.511/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AVA-EUR — BUILDING_ACCELERATION — score 5.478/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.229/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — BUILDING_ACCELERATION — score 5.072/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARK-EUR — BUILDING_ACCELERATION — score 4.956/10 — DETECTED_BUT_TOO_LATE
- PEAQ-EUR — BUILDING_ACCELERATION — score 4.951/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AUDIO-EUR — BUILDING_ACCELERATION — score 4.920/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ORCA-EUR — MEMORY_24H — score mémoire 8.261/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.898/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — ACTIVE_NOW — score mémoire 7.742/10 — sources ACCELERATION — WATCH_ONLY
- ZAMA-EUR — MEMORY_DECAY_24_72H — score mémoire 7.507/10 — sources ACCELERATION — MEMORY_ONLY
- HFT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.444/10 — sources ACCELERATION — MEMORY_ONLY
- METIS-EUR — MEMORY_24H — score mémoire 7.328/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 7.027/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 6.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 6.842/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- OSMO-EUR +11.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +10.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +9.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KERNEL-EUR +9.17% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- IRYS-EUR +8.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +7.83% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +6.10% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PHA-EUR +5.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DODO-EUR +3.97% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DOS-EUR +3.73% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
