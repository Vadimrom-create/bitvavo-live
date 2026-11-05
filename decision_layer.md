# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-05T17:43:57.883767+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.407 | entrée 5.300 | trend 7.800 | rang 6.391
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.391

## Accélération indépendante

- ALIGN-EUR — CONFIRMED_ACCELERATION — score 8.589/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — CONFIRMED_ACCELERATION — score 6.680/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- IKA-EUR — BUILDING_ACCELERATION — score 5.328/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 5.018/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PUFFER-EUR — MEMORY_DECAY_24_72H — score mémoire 9.703/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 9.632/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — MEMORY_24H — score mémoire 9.096/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 8.951/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — ACTIVE_NOW — score mémoire 8.589/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- KMNO-EUR — MEMORY_DECAY_24_72H — score mémoire 8.306/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 7.995/10 — sources ACCELERATION — MEMORY_ONLY
- ARX-EUR — MEMORY_24H — score mémoire 7.773/10 — sources ACCELERATION — MEMORY_ONLY
- JTO-EUR — MEMORY_24H — score mémoire 7.710/10 — sources ACCELERATION — MEMORY_ONLY
- ESP-EUR — MEMORY_24H — score mémoire 7.492/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- ALIGN-EUR +30.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +22.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- EDGE-EUR +19.24% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +8.97% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +6.51% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +5.24% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ACT-EUR +4.88% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FLUID-EUR +4.63% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +3.80% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ICNT-EUR +3.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
