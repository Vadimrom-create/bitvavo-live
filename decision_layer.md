# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-04T08:11:58.776763+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BEAM-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.876 | entrée 5.600 | trend 8.000 | rang 6.715
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BEAM-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.715
2. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.565
3. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.318

## Accélération indépendante

- ADX-EUR — CONFIRMED_ACCELERATION — score 8.638/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 2Z-EUR — CONFIRMED_ACCELERATION — score 6.578/10 — DETECTED_BUT_TOO_LATE
- TREAD-EUR — BUILDING_ACCELERATION — score 5.713/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- BIRB-EUR — BUILDING_ACCELERATION — score 5.476/10 — DETECTED_BUT_TOO_LATE
- MEGA-EUR — BUILDING_ACCELERATION — score 5.355/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PTB-EUR — BUILDING_ACCELERATION — score 5.348/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.179/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAIKO-EUR — BUILDING_ACCELERATION — score 4.858/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RUNE-EUR — MEMORY_24H — score mémoire 9.243/10 — sources ACCELERATION — MEMORY_ONLY
- AXIS-EUR — MEMORY_24H — score mémoire 8.937/10 — sources ACCELERATION — MEMORY_ONLY
- ADX-EUR — ACTIVE_NOW — score mémoire 8.638/10 — sources ACCELERATION — WATCH_ONLY
- TAI-EUR — MEMORY_DECAY_24_72H — score mémoire 7.864/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.451/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — MEMORY_DECAY_24_72H — score mémoire 7.136/10 — sources ACCELERATION — MEMORY_ONLY
- BTT-EUR — MEMORY_DECAY_24_72H — score mémoire 6.830/10 — sources ACCELERATION — MEMORY_ONLY
- ZEUS-EUR — MEMORY_DECAY_24_72H — score mémoire 6.795/10 — sources ACCELERATION — MEMORY_ONLY
- ALIGN-EUR — MEMORY_24H — score mémoire 6.724/10 — sources ACCELERATION — MEMORY_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 6.715/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- USELESS-EUR +18.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FLUID-EUR +18.16% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- HOT-EUR +16.06% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- VVV-EUR +14.50% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +14.29% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +13.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOON-EUR +13.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WHUF-EUR +13.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZRO-EUR +12.73% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- PUMP-EUR +12.70% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
