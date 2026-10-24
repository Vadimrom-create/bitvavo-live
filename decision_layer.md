# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-24T19:27:33.068408+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.470 | entrée 6.150 | trend 8.900 | rang 7.405
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.405
2. ELSA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.172
3. CTR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.615

## Accélération indépendante

- ARX-EUR — CONFIRMED_ACCELERATION — score 7.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXIS-EUR — BUILDING_ACCELERATION — score 6.202/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PROMPT-EUR — BUILDING_ACCELERATION — score 5.500/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ELSA-EUR — BUILDING_ACCELERATION — score 5.234/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- EPIC-EUR — MEMORY_24H — score mémoire 10.000/10 — sources ACCELERATION — MEMORY_ONLY
- PTB-EUR — MEMORY_24H — score mémoire 9.557/10 — sources ACCELERATION — MEMORY_ONLY
- SYN-EUR — MEMORY_24H — score mémoire 8.740/10 — sources ACCELERATION — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.689/10 — sources ACCELERATION — MEMORY_ONLY
- TREE-EUR — MEMORY_24H — score mémoire 8.663/10 — sources ACCELERATION — MEMORY_ONLY
- CHIP-EUR — MEMORY_24H — score mémoire 7.845/10 — sources ACCELERATION — MEMORY_ONLY
- BIRB-EUR — MEMORY_DECAY_24_72H — score mémoire 7.796/10 — sources ACCELERATION — MEMORY_ONLY
- U-EUR — MEMORY_24H — score mémoire 7.754/10 — sources ACCELERATION — MEMORY_ONLY
- 0G-EUR — MEMORY_24H — score mémoire 7.620/10 — sources ACCELERATION — MEMORY_ONLY
- BREV-EUR — MEMORY_24H — score mémoire 7.538/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- EPIC-EUR +29.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ANIME-EUR +20.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIRB-EUR +16.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +14.84% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- UP-EUR +13.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXIS-EUR +11.69% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- U-EUR +9.73% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CAP-EUR +8.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TREE-EUR +8.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ICNT-EUR +7.68% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
