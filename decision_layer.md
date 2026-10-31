# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-31T18:56:28.924845+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOLV-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.568 | entrée 5.650 | trend 8.700 | rang 6.910
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.910
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.783
3. PEPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.769

## Accélération indépendante

- U-EUR — CONFIRMED_ACCELERATION — score 9.449/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- STO-EUR — CONFIRMED_ACCELERATION — score 8.082/10 — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 8.004/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BTT-EUR — CONFIRMED_ACCELERATION — score 6.722/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.738/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 4.971/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- U-EUR — ACTIVE_NOW — score mémoire 9.449/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- RECALL-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- PROMPT-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION — WATCH_ONLY
- OSMO-EUR — MEMORY_24H — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- STO-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- LAPTOP-EUR — ACTIVE_NOW — score mémoire 8.004/10 — sources ACCELERATION — WATCH_ONLY
- GWEI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.893/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 7.637/10 — sources ACCELERATION — MEMORY_ONLY
- NIL-EUR — MEMORY_24H — score mémoire 7.182/10 — sources ACCELERATION — MEMORY_ONLY
- COW-EUR — MEMORY_24H — score mémoire 7.102/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +36.58% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- COW-EUR +20.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STX-EUR +18.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MORPHO-EUR +16.71% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RED-EUR +13.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INX-EUR +12.49% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- RSR-EUR +11.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PTB-EUR +11.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STO-EUR +10.84% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- LIGHTER-EUR +10.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
