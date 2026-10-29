# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-29T22:03:58.622017+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.270 | entrée 5.500 | trend 8.150 | rang 6.906
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.906
2. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.281

## Accélération indépendante

- TRX-EUR — CONFIRMED_ACCELERATION — score 8.541/10 — DETECTED_BUT_TOO_LATE
- ICNT-EUR — CONFIRMED_ACCELERATION — score 6.884/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- GROVE-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- SOON-EUR — MEMORY_24H — score mémoire 8.747/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 8.599/10 — sources ACCELERATION — MEMORY_ONLY
- TRX-EUR — ACTIVE_NOW — score mémoire 8.541/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 8.101/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.846/10 — sources ACCELERATION — MEMORY_ONLY
- AGI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.739/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 7.713/10 — sources ACCELERATION — MEMORY_ONLY
- MEGA-EUR — MEMORY_24H — score mémoire 7.016/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- PARTI-EUR +48.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- LSK-EUR +18.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HYPE-EUR +14.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRX-EUR +11.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLEND-EUR +6.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VSN-EUR +5.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +3.65% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +3.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MERL-EUR +3.56% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HUMA-EUR +3.16% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
