# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-23T00:46:55.660367+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ELSA-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.458 | entrée 6.050 | trend 8.450 | rang 7.207
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : AVA-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.795 | entrée 5.150 | trend 7.900 | rang 6.543
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ELSA-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.207
2. AVA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.543
3. PHA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.448

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 7.722/10 — DETECTED_BUT_TOO_LATE
- GNS-EUR — CONFIRMED_ACCELERATION — score 7.062/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CPOOL-EUR — MEMORY_24H — score mémoire 8.820/10 — sources ACCELERATION — MEMORY_ONLY
- ORCA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.168/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 7.742/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 7.722/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- U-EUR — MEMORY_24H — score mémoire 7.699/10 — sources ACCELERATION — MEMORY_ONLY
- METIS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.245/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- BEAM-EUR — MEMORY_24H — score mémoire 7.238/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ELSA-EUR — ACTIVE_NOW — score mémoire 7.207/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICNT-EUR — MEMORY_24H — score mémoire 7.112/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 7.065/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GROVE-EUR +30.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +27.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +9.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CTR-EUR +9.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEW-EUR +7.65% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GNS-EUR +7.12% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AGI-EUR +6.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +4.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +4.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- DODO-EUR +4.32% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
