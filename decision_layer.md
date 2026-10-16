# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-16T18:09:16.597194+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.822 | entrée 5.350 | trend 9.200 | rang 7.612
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.612
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.380
3. WAL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.855

## Accélération indépendante

- STRAX-EUR — CONFIRMED_ACCELERATION — score 7.054/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WHUF-EUR — BUILDING_ACCELERATION — score 6.033/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — BUILDING_ACCELERATION — score 5.103/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GNS-EUR — MEMORY_24H — score mémoire 9.754/10 — sources ACCELERATION — MEMORY_ONLY
- ZRO-EUR — MEMORY_24H — score mémoire 8.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ETHFI-EUR — MEMORY_DECAY_24_72H — score mémoire 8.808/10 — sources ACCELERATION — MEMORY_ONLY
- BANANA-EUR — MEMORY_DECAY_24_72H — score mémoire 8.443/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_DECAY_24_72H — score mémoire 8.443/10 — sources ACCELERATION — MEMORY_ONLY
- BAT-EUR — MEMORY_24H — score mémoire 8.396/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- COW-EUR — MEMORY_DECAY_24_72H — score mémoire 8.358/10 — sources ACCELERATION — MEMORY_ONLY
- PUFFER-EUR — MEMORY_24H — score mémoire 8.241/10 — sources ACCELERATION — MEMORY_ONLY
- HOME-EUR — MEMORY_DECAY_24_72H — score mémoire 8.030/10 — sources ACCELERATION — MEMORY_ONLY
- EDGE-EUR — MEMORY_24H — score mémoire 7.962/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- POND-EUR +22.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICNT-EUR +20.16% — DETECTED_TOO_LATE — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AMP-EUR +19.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TIA-EUR +17.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- XMN-EUR +17.31% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SOLV-EUR +10.03% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- STRAX-EUR +8.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +6.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- APE-EUR +6.23% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CT-EUR +5.93% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

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
