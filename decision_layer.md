# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-10T03:53:39.436152+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : BIRB-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.541 | entrée 6.000 | trend 7.700 | rang 6.501
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. BIRB-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.501

## Accélération indépendante

- XMN-EUR — CONFIRMED_ACCELERATION — score 7.474/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ZEUS-EUR — BUILDING_ACCELERATION — score 5.337/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CPOOL-EUR — BUILDING_ACCELERATION — score 5.207/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZIL-EUR — MEMORY_24H — score mémoire 9.775/10 — sources ACCELERATION — MEMORY_ONLY
- WIN-EUR — MEMORY_DECAY_24_72H — score mémoire 8.435/10 — sources ACCELERATION — MEMORY_ONLY
- USELESS-EUR — MEMORY_24H — score mémoire 8.089/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 7.572/10 — sources ACCELERATION — MEMORY_ONLY
- CHILLGUY-EUR — MEMORY_24H — score mémoire 7.541/10 — sources ACCELERATION — MEMORY_ONLY
- XMN-EUR — ACTIVE_NOW — score mémoire 7.474/10 — sources ACCELERATION — WATCH_ONLY
- OSMO-EUR — MEMORY_DECAY_24_72H — score mémoire 7.370/10 — sources ACCELERATION — MEMORY_ONLY
- TRUST-EUR — MEMORY_24H — score mémoire 7.087/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WHUF-EUR — MEMORY_DECAY_24_72H — score mémoire 6.938/10 — sources ACCELERATION — MEMORY_ONLY
- SCR-EUR — MEMORY_24H — score mémoire 6.796/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +15.36% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- INIT-EUR +9.89% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GRAM-EUR +6.84% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- AVAX-EUR +6.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ACU-EUR +6.42% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- KERNEL-EUR +5.97% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- BAT-EUR +5.82% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- SIGN-EUR +5.81% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +5.66% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- JUP-EUR +5.64% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
