# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-11-26T02:31:13.560431+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DODO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.186 | entrée 6.300 | trend 7.900 | rang 6.643
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. DODO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.643
2. AI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.412
3. VVV-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 5.913

## Accélération indépendante

- SLX-EUR — CONFIRMED_ACCELERATION — score 8.993/10 — DETECTED_BUT_TOO_LATE
- KAS-EUR — BUILDING_ACCELERATION — score 6.186/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- WIF-EUR — BUILDING_ACCELERATION — score 6.046/10 — DETECTED_BUT_TOO_LATE
- ELSA-EUR — BUILDING_ACCELERATION — score 5.804/10 — DETECTED_BUT_TOO_LATE
- CFG-EUR — BUILDING_ACCELERATION — score 5.698/10 — DETECTED_BUT_TOO_LATE
- ME-EUR — BUILDING_ACCELERATION — score 5.061/10 — DETECTED_BUT_TOO_LATE
- HNT-EUR — BUILDING_ACCELERATION — score 4.942/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- CHR-EUR — BUILDING_ACCELERATION — score 4.770/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- THQ-EUR — MEMORY_24H — score mémoire 9.864/10 — sources ACCELERATION — MEMORY_ONLY
- NES-EUR — MEMORY_24H — score mémoire 9.564/10 — sources ACCELERATION — MEMORY_ONLY
- SLX-EUR — ACTIVE_NOW — score mémoire 8.993/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- IRYS-EUR — MEMORY_DECAY_24_72H — score mémoire 7.139/10 — sources ACCELERATION, DECISION_LAYER — MEMORY_ONLY
- KITE-EUR — MEMORY_24H — score mémoire 6.764/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- DODO-EUR — ACTIVE_NOW — score mémoire 6.643/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AI-EUR — ACTIVE_NOW — score mémoire 6.412/10 — sources ACCELERATION, DECISION_LAYER — WATCH_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 6.374/10 — sources ACCELERATION — MEMORY_ONLY
- MOVE-EUR — MEMORY_24H — score mémoire 6.253/10 — sources ACCELERATION — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 6.186/10 — sources ACCELERATION — WATCH_ONLY

## Audit des plus fortes hausses

- MANTRA-EUR +69.78% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SSV-EUR +58.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOVE-EUR +46.60% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MMT-EUR +46.02% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BIGTIME-EUR +37.93% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- BLUR-EUR +24.14% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- SLX-EUR +23.42% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- NES-EUR +21.56% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VVV-EUR +21.49% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- MOODENG-EUR +18.77% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE

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
