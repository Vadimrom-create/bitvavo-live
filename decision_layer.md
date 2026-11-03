# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-03T08:05:38.923405+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : PARTI-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.249 | entrée 5.500 | trend 7.750 | rang 6.807
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.807
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.793
3. WIN-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.457

## Accélération indépendante

- AXIS-EUR — CONFIRMED_ACCELERATION — score 8.332/10 — DETECTED_BUT_TOO_LATE
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.881/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- GNS-EUR — CONFIRMED_ACCELERATION — score 7.467/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- XMN-EUR — CONFIRMED_ACCELERATION — score 7.152/10 — DETECTED_BUT_TOO_LATE
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.845/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — CONFIRMED_ACCELERATION — score 6.810/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PONKE-EUR — BUILDING_ACCELERATION — score 6.464/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ACT-EUR — BUILDING_ACCELERATION — score 5.422/10 — DETECTED_BUT_TOO_LATE
- KMNO-EUR — BUILDING_ACCELERATION — score 5.401/10 — DETECTED_BUT_TOO_LATE
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.198/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ACU-EUR — MEMORY_24H — score mémoire 9.208/10 — sources ACCELERATION — MEMORY_ONLY
- RUNE-EUR — MEMORY_24H — score mémoire 8.445/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — ACTIVE_NOW — score mémoire 8.332/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- TAI-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources ACCELERATION — WATCH_ONLY
- GNS-EUR — ACTIVE_NOW — score mémoire 7.467/10 — sources ACCELERATION — WATCH_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 7.152/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SOLV-EUR — MEMORY_24H — score mémoire 6.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — ACTIVE_NOW — score mémoire 6.845/10 — sources ACCELERATION — WATCH_ONLY
- ZEUS-EUR — ACTIVE_NOW — score mémoire 6.810/10 — sources ACCELERATION — WATCH_ONLY
- PARTI-EUR — ACTIVE_NOW — score mémoire 6.807/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- XMN-EUR +40.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +15.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICNT-EUR +15.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +11.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +9.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RUNE-EUR +9.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IRYS-EUR +9.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MEGA-EUR +8.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +6.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRUST-EUR +4.47% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
