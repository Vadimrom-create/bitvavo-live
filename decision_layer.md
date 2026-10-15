# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-15T05:47:23.451298+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : ICNT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.831 | entrée 6.750 | trend 8.700 | rang 7.508
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICNT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.508
2. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.150
3. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.780

## Accélération indépendante

- MAGIC-EUR — CONFIRMED_ACCELERATION — score 9.346/10 — DETECTED_BUT_TOO_LATE
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 7.538/10 — DETECTED_BUT_TOO_LATE
- MLN-EUR — CONFIRMED_ACCELERATION — score 7.405/10 — DETECTED_BUT_TOO_LATE
- ACU-EUR — BUILDING_ACCELERATION — score 6.195/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- HFT-EUR — BUILDING_ACCELERATION — score 6.001/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TRAC-EUR — BUILDING_ACCELERATION — score 6.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- VVV-EUR — BUILDING_ACCELERATION — score 5.737/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- SWELL-EUR — BUILDING_ACCELERATION — score 5.652/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RLC-EUR — BUILDING_ACCELERATION — score 5.397/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- O-EUR — BUILDING_ACCELERATION — score 4.835/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NES-EUR — MEMORY_24H — score mémoire 9.532/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — MEMORY_24H — score mémoire 9.495/10 — sources ACCELERATION — MEMORY_ONLY
- MAGIC-EUR — ACTIVE_NOW — score mémoire 9.346/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- EPIC-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION — MEMORY_ONLY
- CAP-EUR — MEMORY_24H — score mémoire 7.893/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 7.813/10 — sources ACCELERATION — MEMORY_ONLY
- QUID-EUR — MEMORY_24H — score mémoire 7.680/10 — sources ACCELERATION — MEMORY_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 7.564/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- PUFFER-EUR — ACTIVE_NOW — score mémoire 7.538/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ICNT-EUR — ACTIVE_NOW — score mémoire 7.508/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- PUFFER-EUR +84.52% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WAL-EUR +21.61% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +15.44% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZK-EUR +14.95% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +14.41% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MLN-EUR +13.82% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +13.11% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DUSK-EUR +11.10% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IKA-EUR +8.35% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- RSR-EUR +8.09% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

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
