# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-06T10:05:29.960935+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TRUST-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.670 | entrée 6.350 | trend 7.900 | rang 6.602
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. TRUST-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.602
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.347

## Accélération indépendante

- WHUF-EUR — CONFIRMED_ACCELERATION — score 8.439/10 — DETECTED_BUT_TOO_LATE
- THE-EUR — CONFIRMED_ACCELERATION — score 6.735/10 — DETECTED_BUT_TOO_LATE
- INX-EUR — CONFIRMED_ACCELERATION — score 6.729/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 6.386/10 — DETECTED_BUT_TOO_LATE
- MAV-EUR — BUILDING_ACCELERATION — score 5.616/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- NES-EUR — BUILDING_ACCELERATION — score 5.499/10 — DETECTED_BUT_TOO_LATE
- UP-EUR — BUILDING_ACCELERATION — score 5.020/10 — DETECTED_BUT_TOO_LATE
- BIGTIME-EUR — BUILDING_ACCELERATION — score 4.873/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- BIRB-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- TRIA-EUR — MEMORY_24H — score mémoire 9.163/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- WHUF-EUR — ACTIVE_NOW — score mémoire 8.439/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EDGE-EUR — MEMORY_DECAY_24_72H — score mémoire 8.063/10 — sources ACCELERATION — MEMORY_ONLY
- ARX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.711/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 6.855/10 — sources ACCELERATION — MEMORY_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 6.775/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_DECAY_24_72H — score mémoire 6.745/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- BIRB-EUR +44.26% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CYBER-EUR +42.07% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +26.30% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ALIGN-EUR +23.23% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PROMPT-EUR +15.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +11.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- THE-EUR +9.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACT-EUR +9.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +8.93% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ARX-EUR +8.01% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
