# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-03T21:56:12.502447+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.768 | entrée 6.100 | trend 7.800 | rang 6.520
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.520
2. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.469

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 6.724/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — BUILDING_ACCELERATION — score 5.975/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RUNE-EUR — MEMORY_24H — score mémoire 9.243/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 8.332/10 — sources ACCELERATION — MEMORY_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 7.881/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.467/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.152/10 — sources ACCELERATION — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.128/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_24H — score mémoire 6.845/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_24H — score mémoire 6.810/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 6.724/10 — sources ACCELERATION — WATCH_ONLY
- ACU-EUR — MEMORY_DECAY_24_72H — score mémoire 6.633/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- HOT-EUR +20.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +18.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RUNE-EUR +16.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +14.67% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LIGHTER-EUR +12.06% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- TREAD-EUR +11.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IRYS-EUR +11.32% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KMNO-EUR +11.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +10.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUMP-EUR +9.96% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
