# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-14T15:26:27.442673+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : ICNT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.586 | entrée 6.550 | trend 8.750 | rang 7.348
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FLUID-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.525 | entrée 5.850 | trend 8.550 | rang 7.301
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. ICNT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.348
2. FLUID-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.301
3. STX-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.221

## Accélération indépendante

- PONKE-EUR — CONFIRMED_ACCELERATION — score 9.495/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 8.033/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- QUID-EUR — CONFIRMED_ACCELERATION — score 7.680/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ESP-EUR — CONFIRMED_ACCELERATION — score 7.079/10 — DETECTED_BUT_TOO_LATE
- DUSK-EUR — CONFIRMED_ACCELERATION — score 6.915/10 — DETECTED_BUT_TOO_LATE
- GWEI-EUR — BUILDING_ACCELERATION — score 6.236/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- OGN-EUR — BUILDING_ACCELERATION — score 5.694/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- NES-EUR — MEMORY_24H — score mémoire 9.532/10 — sources ACCELERATION — MEMORY_ONLY
- PONKE-EUR — ACTIVE_NOW — score mémoire 9.495/10 — sources ACCELERATION — WATCH_ONLY
- PUFFER-EUR — ACTIVE_NOW — score mémoire 8.033/10 — sources ACCELERATION — WATCH_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 7.892/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- QUID-EUR — ACTIVE_NOW — score mémoire 7.680/10 — sources ACCELERATION — WATCH_ONLY
- RAD-EUR — MEMORY_24H — score mémoire 7.564/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- GNS-EUR — MEMORY_24H — score mémoire 7.386/10 — sources ACCELERATION — MEMORY_ONLY
- ICNT-EUR — ACTIVE_NOW — score mémoire 7.348/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- FLUID-EUR — ACTIVE_NOW — score mémoire 7.301/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FARTCOIN-EUR — MEMORY_24H — score mémoire 7.230/10 — sources ACCELERATION — MEMORY_ONLY

## Audit des plus fortes hausses

- WAL-EUR +33.37% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +17.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +15.66% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DEEP-EUR +14.57% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PNT-EUR +12.55% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GLMR-EUR +12.53% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +10.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GNS-EUR +9.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AXL-EUR +9.28% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +6.88% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
