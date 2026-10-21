# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-21T07:32:02.607562+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ALT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.272 | entrée 5.650 | trend 8.450 | rang 7.065
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ALT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.065
2. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.891
3. BAT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.654

## Accélération indépendante

- W-EUR — CONFIRMED_ACCELERATION — score 7.838/10 — DETECTED_BUT_TOO_LATE
- IRYS-EUR — CONFIRMED_ACCELERATION — score 6.833/10 — DETECTED_BUT_TOO_LATE
- APT-EUR — BUILDING_ACCELERATION — score 5.341/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STX-EUR — BUILDING_ACCELERATION — score 5.231/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CTSI-EUR — BUILDING_ACCELERATION — score 4.982/10 — DETECTED_BUT_TOO_LATE
- BAT-EUR — BUILDING_ACCELERATION — score 4.939/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUMP-EUR — BUILDING_ACCELERATION — score 4.806/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.505/10 — sources ACCELERATION — MEMORY_ONLY
- MOODENG-EUR — MEMORY_24H — score mémoire 9.291/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — MEMORY_24H — score mémoire 9.147/10 — sources ACCELERATION — MEMORY_ONLY
- AMP-EUR — MEMORY_24H — score mémoire 8.353/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- W-EUR — ACTIVE_NOW — score mémoire 7.838/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IOST-EUR — MEMORY_24H — score mémoire 7.706/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.510/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.345/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- TOSHI-EUR — MEMORY_24H — score mémoire 7.271/10 — sources ACCELERATION — MEMORY_ONLY
- ALT-EUR — ACTIVE_NOW — score mémoire 7.065/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- IOST-EUR +73.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +38.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +30.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +28.98% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEW-EUR +26.34% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PARTI-EUR +24.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CVX-EUR +23.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- COMP-EUR +22.99% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +18.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +14.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
