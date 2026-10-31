# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-10-31T08:52:06.693981+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SOLV-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.420 | entrée 6.200 | trend 8.700 | rang 7.250
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INIT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 6.941 | entrée 5.150 | trend 8.000 | rang 6.658
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. SOLV-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.250
2. INIT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.658
3. PARTI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.497

## Accélération indépendante

- OSMO-EUR — CONFIRMED_ACCELERATION — score 8.400/10 — DETECTED_BUT_TOO_LATE
- NIL-EUR — CONFIRMED_ACCELERATION — score 7.182/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- LSK-EUR — CONFIRMED_ACCELERATION — score 6.818/10 — DETECTED_BUT_TOO_LATE
- PROMPT-EUR — CONFIRMED_ACCELERATION — score 6.606/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- U-EUR — BUILDING_ACCELERATION — score 5.668/10 — DETECTED_BUT_TOO_LATE
- GIGA-EUR — BUILDING_ACCELERATION — score 5.359/10 — DETECTED_BUT_TOO_LATE
- HUMA-EUR — BUILDING_ACCELERATION — score 5.123/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- AXIS-EUR — BUILDING_ACCELERATION — score 4.832/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- RECALL-EUR — MEMORY_24H — score mémoire 9.168/10 — sources ACCELERATION — MEMORY_ONLY
- GWEI-EUR — MEMORY_24H — score mémoire 8.661/10 — sources ACCELERATION — MEMORY_ONLY
- OSMO-EUR — ACTIVE_NOW — score mémoire 8.400/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- XMN-EUR — MEMORY_24H — score mémoire 7.637/10 — sources ACCELERATION — MEMORY_ONLY
- SOLV-EUR — ACTIVE_NOW — score mémoire 7.250/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NIL-EUR — ACTIVE_NOW — score mémoire 7.182/10 — sources ACCELERATION — WATCH_ONLY
- HFT-EUR — MEMORY_24H — score mémoire 7.021/10 — sources ACCELERATION — MEMORY_ONLY
- PEPE-EUR — MEMORY_24H — score mémoire 6.997/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LSK-EUR — ACTIVE_NOW — score mémoire 6.818/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- BEAM-EUR — MEMORY_24H — score mémoire 6.795/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- HFT-EUR +28.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BIRB-EUR +20.33% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- LSK-EUR +18.64% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- GWEI-EUR +17.74% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BEAM-EUR +14.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POND-EUR +14.67% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CVC-EUR +13.91% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CAP-EUR +13.86% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- WOO-EUR +13.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- U-EUR +13.08% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
