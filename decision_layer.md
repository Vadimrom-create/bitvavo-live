# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-02T08:30:53.284034+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.994 | entrée 6.400 | trend 8.200 | rang 6.894
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.894
2. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.415
3. HAEDAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.255

## Accélération indépendante

- ACU-EUR — CONFIRMED_ACCELERATION — score 9.208/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RUNE-EUR — CONFIRMED_ACCELERATION — score 8.445/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- INIT-EUR — BUILDING_ACCELERATION — score 6.318/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZKJ-EUR — BUILDING_ACCELERATION — score 5.477/10 — DETECTED_BUT_TOO_LATE
- HOT-EUR — BUILDING_ACCELERATION — score 5.297/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ACU-EUR — ACTIVE_NOW — score mémoire 9.208/10 — sources ACCELERATION — WATCH_ONLY
- RUNE-EUR — ACTIVE_NOW — score mémoire 8.445/10 — sources ACCELERATION — WATCH_ONLY
- ADX-EUR — MEMORY_DECAY_24_72H — score mémoire 7.813/10 — sources ACCELERATION — MEMORY_ONLY
- POWR-EUR — MEMORY_DECAY_24_72H — score mémoire 7.286/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 6.931/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 6.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- WIN-EUR — MEMORY_24H — score mémoire 6.783/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- U-EUR — MEMORY_DECAY_24_72H — score mémoire 6.777/10 — sources ACCELERATION — MEMORY_ONLY
- G-EUR — MEMORY_24H — score mémoire 6.751/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.455/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- GIGA-EUR +13.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HAEDAL-EUR +9.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +7.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ZKJ-EUR +6.67% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OGN-EUR +6.13% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +5.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +5.15% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +5.02% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GROVE-EUR +4.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +3.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
