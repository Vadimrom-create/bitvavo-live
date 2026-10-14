# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-14T10:34:05.517365+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : STX-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.916 | entrée 6.950 | trend 8.900 | rang 7.739
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.739
2. AZTEC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.261
3. PYTH-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.226

## Accélération indépendante

- AXL-EUR — CONFIRMED_ACCELERATION — score 8.441/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- RAD-EUR — CONFIRMED_ACCELERATION — score 7.564/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WAL-EUR — BUILDING_ACCELERATION — score 5.915/10 — DETECTED_BUT_TOO_LATE
- PNT-EUR — BUILDING_ACCELERATION — score 5.904/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — BUILDING_ACCELERATION — score 5.890/10 — DETECTED_BUT_TOO_LATE
- DRV-EUR — BUILDING_ACCELERATION — score 4.781/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- AXL-EUR — ACTIVE_NOW — score mémoire 8.441/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 7.739/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 7.568/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- RAD-EUR — ACTIVE_NOW — score mémoire 7.564/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- AVA-EUR — MEMORY_24H — score mémoire 7.431/10 — sources ACCELERATION — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.386/10 — sources ACCELERATION — MEMORY_ONLY
- AZTEC-EUR — ACTIVE_NOW — score mémoire 7.261/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- FARTCOIN-EUR — MEMORY_24H — score mémoire 7.230/10 — sources ACCELERATION — MEMORY_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.226/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- GNS-EUR +75.43% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WAL-EUR +39.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +19.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +16.87% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DEEP-EUR +15.40% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +14.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +13.47% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- TRAC-EUR +13.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- KMNO-EUR +10.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OP-EUR +9.46% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
