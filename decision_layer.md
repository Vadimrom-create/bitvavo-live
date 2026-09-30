# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-30T14:53:37.813349+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SPK-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.641 | entrée 6.400 | trend 8.450 | rang 7.565
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : KSM-EUR | action LATENT_ACCELERATOR | opportunité 7.897 | entrée 5.400 | trend 9.200 | rang 7.738
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : COMP-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.887 | entrée 6.000 | trend 9.000 | rang 7.828
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Tous les achats immédiats

Aucun ACHETE_MAINTENANT dans le classement complet.

## Top cross-sectionnel — aperçu non exhaustif

Ce top est une vue courte multi-buckets. Il ne doit jamais être utilisé comme liste exhaustive des achats immédiats.
1. COMP-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.828
2. HUMA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.826
3. HBAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.804

## Accélération indépendante

- STX-EUR — CONFIRMED_ACCELERATION — score 9.587/10 — DETECTED_BUT_TOO_LATE
- SOON-EUR — CONFIRMED_ACCELERATION — score 8.877/10 — DETECTED_BUT_TOO_LATE
- INIT-EUR — BUILDING_ACCELERATION — score 5.928/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- EDGE-EUR — BUILDING_ACCELERATION — score 5.647/10 — DETECTED_BUT_TOO_LATE
- GALA-EUR — BUILDING_ACCELERATION — score 5.227/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 4.919/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KITE-EUR — BUILDING_ACCELERATION — score 4.793/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- ARB-EUR — BUILDING_ACCELERATION — score 4.759/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- NOM-EUR — MEMORY_24H — score mémoire 9.770/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- STX-EUR — ACTIVE_NOW — score mémoire 9.587/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- CTR-EUR — MEMORY_24H — score mémoire 8.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SOON-EUR — ACTIVE_NOW — score mémoire 8.877/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- DGB-EUR — MEMORY_24H — score mémoire 8.670/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CVC-EUR — MEMORY_24H — score mémoire 8.565/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- LRC-EUR — MEMORY_24H — score mémoire 8.342/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ARK-EUR — MEMORY_24H — score mémoire 8.293/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- SPX-EUR — MEMORY_24H — score mémoire 8.198/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SOON-EUR +58.52% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- MOVR-EUR +56.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CT-EUR +38.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ARK-EUR +26.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOM-EUR +21.39% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- QNT-EUR +17.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NIL-EUR +16.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +12.19% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- GLMR-EUR +12.17% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- GTC-EUR +11.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION

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
