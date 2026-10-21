# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-21T02:08:02.209742+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ALT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.869 | entrée 5.850 | trend 8.450 | rang 7.290
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CTR-EUR | action LATENT_ACCELERATOR | opportunité 7.659 | entrée 5.300 | trend 8.600 | rang 7.101
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.450 | entrée 7.200 | trend 8.750 | rang 7.777
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.777
2. ALT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.290
3. CTR-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 7.101

## Accélération indépendante

- MOODENG-EUR — CONFIRMED_ACCELERATION — score 9.291/10 — DETECTED_BUT_TOO_LATE
- WHUF-EUR — CONFIRMED_ACCELERATION — score 9.147/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TOSHI-EUR — CONFIRMED_ACCELERATION — score 7.271/10 — DETECTED_BUT_TOO_LATE
- MEW-EUR — BUILDING_ACCELERATION — score 6.248/10 — DETECTED_BUT_TOO_LATE
- SUPER-EUR — BUILDING_ACCELERATION — score 5.837/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 5.289/10 — DETECTED_BUT_TOO_LATE
- TURBO-EUR — BUILDING_ACCELERATION — score 5.042/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STX-EUR — BUILDING_ACCELERATION — score 4.919/10 — DETECTED_BUT_TOO_LATE
- MMT-EUR — BUILDING_ACCELERATION — score 4.895/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.505/10 — sources ACCELERATION — MEMORY_ONLY
- MOODENG-EUR — ACTIVE_NOW — score mémoire 9.291/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WHUF-EUR — ACTIVE_NOW — score mémoire 9.147/10 — sources ACCELERATION — WATCH_ONLY
- POND-EUR — MEMORY_DECAY_24_72H — score mémoire 8.406/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- IOST-EUR — MEMORY_24H — score mémoire 7.706/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.510/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.290/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TOSHI-EUR — ACTIVE_NOW — score mémoire 7.271/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- IOST-EUR +42.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +32.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +24.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEW-EUR +22.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVX-EUR +21.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- COMP-EUR +21.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TOSHI-EUR +16.51% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SOSO-EUR +14.92% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +14.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOODENG-EUR +13.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
