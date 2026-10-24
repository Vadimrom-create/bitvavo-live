# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-24T09:50:45.227401+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ELSA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.434 | entrée 5.900 | trend 8.350 | rang 6.961
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : INIT-EUR | action LATENT_ACCELERATOR | opportunité 7.548 | entrée 4.750 | trend 8.900 | rang 7.215
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : aucun candidat matériel

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INIT-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.215
2. ELSA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.961

## Accélération indépendante

- TREE-EUR — CONFIRMED_ACCELERATION — score 8.663/10 — DETECTED_BUT_TOO_LATE
- U-EUR — CONFIRMED_ACCELERATION — score 7.754/10 — DETECTED_BUT_TOO_LATE
- BREV-EUR — CONFIRMED_ACCELERATION — score 7.538/10 — DETECTED_BUT_TOO_LATE
- 2Z-EUR — CONFIRMED_ACCELERATION — score 7.503/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — BUILDING_ACCELERATION — score 6.035/10 — DETECTED_BUT_TOO_LATE
- HOME-EUR — BUILDING_ACCELERATION — score 5.751/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LINEA-EUR — BUILDING_ACCELERATION — score 5.479/10 — DETECTED_BUT_TOO_LATE
- ENSO-EUR — BUILDING_ACCELERATION — score 5.475/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 5.405/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DOS-EUR — BUILDING_ACCELERATION — score 5.335/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- SYN-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.689/10 — sources ACCELERATION — MEMORY_ONLY
- TREE-EUR — ACTIVE_NOW — score mémoire 8.663/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- BIRB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — ACTIVE_NOW — score mémoire 7.754/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- AXIS-EUR — MEMORY_24H — score mémoire 7.606/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — ACTIVE_NOW — score mémoire 7.538/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- 2Z-EUR — ACTIVE_NOW — score mémoire 7.503/10 — sources ACCELERATION — WATCH_ONLY
- EPIC-EUR — MEMORY_DECAY_24_72H — score mémoire 7.306/10 — sources ACCELERATION — MEMORY_ONLY
- INIT-EUR — ACTIVE_NOW — score mémoire 7.215/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- BIRB-EUR +126.85% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +94.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREE-EUR +54.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +28.71% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUST-EUR +24.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +18.21% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CPOOL-EUR +15.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LUMIA-EUR +15.16% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KERNEL-EUR +14.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +14.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
