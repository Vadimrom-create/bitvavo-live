# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-18T06:01:16.254817+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DUSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.266 | entrée 5.450 | trend 8.550 | rang 7.074
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DUSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.074
2. TIA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.922
3. RSR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.625

## Accélération indépendante

- PUFFER-EUR — BUILDING_ACCELERATION — score 5.834/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEGA-EUR — BUILDING_ACCELERATION — score 5.737/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- S-EUR — BUILDING_ACCELERATION — score 4.819/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AXL-EUR — MEMORY_24H — score mémoire 9.132/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZRC-EUR — MEMORY_24H — score mémoire 8.245/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GTC-EUR — MEMORY_24H — score mémoire 7.849/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CPOOL-EUR — MEMORY_24H — score mémoire 7.716/10 — sources ACCELERATION — MEMORY_ONLY
- ALT-EUR — MEMORY_24H — score mémoire 7.202/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- WAL-EUR — MEMORY_24H — score mémoire 7.187/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- BTT-EUR — MEMORY_DECAY_24_72H — score mémoire 7.178/10 — sources ACCELERATION — MEMORY_ONLY
- DUSK-EUR — ACTIVE_NOW — score mémoire 7.074/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- PROM-EUR — MEMORY_24H — score mémoire 7.030/10 — sources ACCELERATION — MEMORY_ONLY
- KMNO-EUR — MEMORY_24H — score mémoire 6.986/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- U-EUR +28.09% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- AVA-EUR +26.91% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SAND-EUR +15.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GTC-EUR +15.22% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ZEUS-EUR +13.79% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- OSMO-EUR +11.76% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BTT-EUR +8.95% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PUFFER-EUR +8.62% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- DOS-EUR +5.80% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- REQ-EUR +4.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
